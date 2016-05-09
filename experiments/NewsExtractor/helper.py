import sys
import os
import urllib2
import cookielib
import json
import lxml.html
import numpy as np
import pickle
import codecs

from sklearn.feature_extraction import DictVectorizer
import feature

def get_ordered_path_and_text(tree):
    print 'Get Inordered Nodes'
    texts = tree.xpath('//text()')
    textnodes = []
    for each in texts:
        if len(each.strip())==0:
            continue
        path = tree.getpath(each.getparent())
        #Known hidden tags
        tag = path.split('/')[-1]
        visibile = True
        for e in  ['meta', 'script', 
        'style', 'title','date', 
        'img', 'video' ,'figure', 
        'source', 'samp', 'progress', 
        'noscript','nav', 'iframe', 
        'footer', 'address', 'figcaption']: 
            if e.lower() in tag:
                visibile = False
                break
        
        if visibile:
            assert(tree.xpath(path)[0].tail == each or tree.xpath(path)[0].text==each)
            if tree.xpath(path)[0].tail == each:
                textnodes.append((path,u'tail',each))
            else:
                textnodes.append((path,u'text',each))
    return textnodes

def get_tree(url):
    return lxml.html.parse(url)

def extract_labels(textnodes, fname):
    print 'Extracting Labels'
    ftitle, ftitle_nonode, fbody, fbody_nonode, fdate, fdate_nonode = fname
    #Y = [0]*2*len(textnodes) #One for tail and one for text
    Y = [0]*len(textnodes) 
    try:
        with codecs.open(ftitle,'r', "utf-8") as fp:
            data_title = json.load(fp)
    except(ValueError):
        print 'No Title %s' %ftitle
        data_title = []

    try:
        with codecs.open(fbody,'r', "utf-8") as fp:
            data_body = json.load(fp)
    except(ValueError):
        print 'No Body %s' %fbody
        data_body = []
    try:
        with codecs.open(fdate,'r', "utf-8") as fp:
            data_date = json.load(fp)
    except(ValueError):
        print 'No Date %s' %fdate
        data_date = []

    #print data[:3]
    d_t = {x[0]+'_'+x[1]:y for x,y in data_title}
    d_b = {x[0]+'_'+x[1]:y for x,y in data_body}
    d_d = {x[0]+'_'+x[1]:y for x,y in data_date}
    # print data
    # print ftitle
    # print fbody
    cnt_t = 0
    cnt_b = 0
    cnt_d = 0
    con = False
    #_,_,_ = textnodes[0]
    for i,temp in enumerate(textnodes):
        parentpath,location,value = temp
        #path is (parentpath,location)
        #print parentpath+'_'+location
        if unicode(parentpath+'_'+location) in d_t:
            Y[i]=1
            # print 'Number %d' %i
            # print value
            cnt_t+=1
        #Content and date overlap sometimes!! to allow that to happen
        if unicode(parentpath+'_'+location) in d_b:
            Y[i] = 2
            cnt_b+=1
            #print '--***'*20
            #print value
        if unicode(parentpath+'_'+location) in d_d:
            Y[i] = 3
            
            cnt_d+=1
    # print fname
    # for each in textnodes:
    #     print each, tree.xpath(each)
    
    try:

        assert(cnt_t == len(d_t) and cnt_b == len(d_b)and cnt_d == len(d_d))
    except:
        print d_d
        for each in textnodes:
            print each
        raw_input()

    return Y,d_t

#You may want to edit this function if you want to change the parser
def extract_features(textnodes, tree, featname='Content'):
    X = []
    if featname == 'Content':
        f = feature.Content(tree)
    elif featname == 'bow':
        f = feature.BOW()
    elif featname == 'Title':
        f = feature.Title(tree,textnodes=textnodes)
    elif featname == 'Date':
        f = feature.Date(tree,textnodes=textnodes)
    else:
        f = None
    i=0
    for parentpath,location,value in textnodes:
        #print tree.xpath(each)
        
        i+=1
        X.append(f.features(parentpath , value, tree))
    # print zip(X,textnodes)
    return X

def getexamples(trainfile, directory, strict=False):

        groundtruthpath = directory
        print 'groundtruthpath %s' %groundtruthpath
        #trainfile = 'data/train/field.csv'
        fids_dict = {}
        for each in os.listdir(groundtruthpath+'/Title'):
            res = each.split('.')[0]
            if res in fids_dict:
                fids_dict[res] += 1
            else:
                fids_dict[res] = 1

        for each in os.listdir(groundtruthpath+'/Publish_date'):
            res = each.split('.')[0]
            if res in fids_dict:
                fids_dict[res] += 1
            else:
                fids_dict[res] = 1
        print fids_dict
        for each in os.listdir(groundtruthpath+'/Body'):
            res = ''
            res = each.split('.')[0]                
            if res in fids_dict:
                fids_dict[res] += 1
            else:
                fids_dict[res] = 1
        print fids_dict

        for each in fids_dict.keys():  
            if not strict:
                if fids_dict[each] < 4: #Atleast 2 entries are found
                    del fids_dict[each]
            else:
                if fids_dict[each] !=6:  # Accept absent File as Null title only if specified
                    del fids_dict[each]

        print "keys %s" %fids_dict
        print len(fids_dict)
        urls = []
        fid = []
        td = open(trainfile)
        tmp =  []
        for each in td.readlines():
            k = each.strip().split(',');
            if k[0] in fids_dict :
                urls.append(k[1])
                fid.append(k[0]) 
            tmp.append(k[0])

        print len(fid)
        print 'Chopping off  to 10... experiment remove if you want to run on full data set'
        #return urls[:10],fid[:10]
        #return urls[:],fid[:50]
        return urls,fid





if  __name__ == '__main__':
    print 'python helper.py ../../data/temp ../../data/<feature>'
    featname = sys.argv[3]
    urls,fids = getexamples('../../data/train/field.csv', sys.argv[1])

    #data = zip(urls,fid)
    #urls,fids = zip(*data)
    directory = sys.argv[1]
    ftitle = map(lambda x: directory+'/Title/'+x+'.WithNode.groundtruth', fids)
    ftitle_nonode = map(lambda x: directory+'/Title/'+x+'.groundtruth', fids)
    fbody = map(lambda x: directory+'/Body/'+x+'.WithNode.groundtruth', fids)
    fbody_nonode = map(lambda x: directory+'/Body/'+x+'.groundtruth', fids)
    fdate = map(lambda x: directory+'/Publish_date/'+x+'.WithNode.groundtruth', fids)
    fdate_nonode = map(lambda x: directory+'/Publish_date/'+x+'.groundtruth', fids)
    fnames = zip(ftitle, ftitle_nonode, fbody, fbody_nonode, fdate, fdate_nonode)
    idval = 0
    

    feat = DictVectorizer(sparse=False)
    featlist = []
    for eachurl,fname in zip(urls,fnames):            
        print fname            
        tree = get_tree(eachurl)
        #textnodes = get_text_nodelist_dfs(tree)
        textnodes = get_ordered_path_and_text(tree)
        #_,_ = extract_labels(textnodes, fname)
        featlist.extend(extract_features(textnodes, tree, featname))
    
    
    feat.fit(featlist)
    with open(sys.argv[2]+'/train/featurenames.json', 'w') as outfile:
                    json.dump(feat.feature_names_,outfile)
    pickle.dump(feat,file(sys.argv[2]+'/train/featurevectorizer.dat','w'))

    
    for eachurl,fname in zip(urls,fnames):
        tree = get_tree(eachurl)
        #textnodes = get_text_nodelist_dfs(tree)
        textnodes = get_ordered_path_and_text(tree)
        textnodes_val = []
        textnodes_val.extend(each for _,_,each in textnodes)
        Y,_ = extract_labels(textnodes, fname)

        #feat1 = pickle.load(file('thisfeature.data','r')) #Testin
        X = feat.transform(extract_features(textnodes, tree, featname))
        print 'Shape of X ', X.shape
        x_tilde = []
        for each in range(X.shape[0]): 
            x_tilde.append([])
            x_tilde[-1].extend([Y[each],])
            x_tilde[-1].extend(X[each,:])  
        x_tilde = np.array(x_tilde)
        
        np.save(sys.argv[2]+'/train/example_'+str(fname[0].split('/')[-1].split('.')[0]), np.array(x_tilde))
        with open(sys.argv[2]+'/train/example_'+str(fname[0].split('/')[-1].split('.')[0])+'.json', 'w') as outfile:
                json.dump(textnodes_val, outfile)



    print 'Done creating training and test split'
