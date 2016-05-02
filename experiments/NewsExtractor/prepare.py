import sys
import json
import codecs

import cookielib
import urllib2

import helper
###################################
import lxml.html
###################################

def _match(tree, values, strict=True):
    """ Find a unique match when strict is enabled, otherwise 
    just match all nodes with the same text value """
    assert(len(values)>0)
    xpath = {}
    res = []
    textnodes = helper.get_ordered_path_and_text(tree)
    for path,location, v in textnodes:
        value = v.replace('\n','').replace('\r','').replace(' ','')
        if len(value)==0:
            continue
        if value and value not in xpath:
            xpath[value] = []
        xpath[value].append(path)
    for v in values:
        each = v.replace('\n','').replace('\r','').replace(' ','')
        if len(each)==0:
            continue
        if each in xpath and len(xpath[each])==1:
            parent = tree.xpath(xpath[each][0])[0]
            if parent.tail and parent.tail.replace('\n','').replace('\r','').replace(' ','')== each:
                res.append(( (xpath[each][0], u'tail'), parent.tail))
            else:
                res.append(( (xpath[each][0], u'text'), parent.text))
        else:
            if each not in xpath:
                print 'Cannot map %s No Entry at ' %(each)                
                if len(each.strip())>0:
                    print '---***---+++'*10
                    for _,_,val in textnodes:
                        print val
                        print '---------'*10
                    print '---***---+++'*10
                    raw_input()
            else:
                if not strict:
                    for parent in tree.xpath(xpath[each][0]):
                        if parent.tail and parent.tail.replace('\n','').replace('\r','').replace(' ','')== each:
                            res.append(( (xpath[each][0], u'tail'), parent.tail))
                        else:
                            res.append(( (xpath[each][0], u'text'), parent.text))
                    print 'Including ambiguous labels :- Strict mode disabled!'
                else:
                    print 'Cannot map "%s" of length %d with '%(each[:10], len(each))
                    for every in xpath[each]:
                        parent = tree.xpath(every)[0]
                        print '%s or %s @ %s ' %(parent.tail, parent.text,every)
                    print 'Excluding from labelling as truth ambiguous mapping!'
    #print res
    return True, res




def _clean(groundtruthpath, id, url, preparedirectory,strict=True):
        fnametruth = groundtruthpath +id+'.WithNode.groundtruth'
        con = False
        try:
            data = json.load(codecs.open(fnametruth,'r', "utf-8"))
            _, values = zip(*data)

            jar = cookielib.FileCookieJar("cookies")
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            request = urllib2.Request(
                    url,
                    headers={'User-agent': 'Mozilla/5.0'})

            try:
                result = opener.open(
                            request
                            )
            except Exception:
                result = None
                print 'Unable to parse ... check this place'

            doc = lxml.html.parse(result) #############################PARSER###################
        
            success, truth = _match(doc ,values,strict)
        except(ValueError):
            success,truth = True,[]
        except(IOError):
            print 'File %s Not found ' %fnametruth 
            print 'Press Enter to continue, and R to remember the choice'
            if con:
                x =  raw_input()
                con = (x == 'R')
            success, truth = True, []

        if success:
            fname = preparedirectory +id+'.groundtruth'
            name = preparedirectory +id+'.WithNode.groundtruth'
            print 'WORKED id %s is OK' %id
            with codecs.open(name,'w', "utf-8") as outfile:
                json.dump(truth, outfile)
                #print truth
            fp = codecs.open(fname,'w', "utf-8")
            fp.write('Dummy file')
        else:
            print 'FAILED !!! %s' %id
        return
#######################################


def prepare(directory, preparedirectory, urls, fids):
    groundtruthpath = directory
    preparedpath =  preparedirectory
    for each,url in zip(fids,urls):
        _clean(groundtruthpath +'/Title/', each, url, preparedirectory+'/Title/', strict=False)
        _clean(groundtruthpath +'/Publish_date/', each, url, preparedirectory+'/Publish_date/', strict=False)
        _clean(groundtruthpath +'/Body/', each, url, preparedirectory+'/Body/')


def help():
    print """
    HELP:
    The purpose of this file is to clean the raw data collected from the chrom extension that
    comes with this file and match the nodes selected using the chrome browser with  the nodes
    that can be parsed using the used parser.
    USAGE:
    python prepare.py <hashfile.csv> <raw data from chrome extn source> <prepare data destination>
    <hashfile.csv> should contain the details of the allowed fileids with their corresponding URL"""

if __name__ == '__main__':    
    help();
    print 'python prepare.py %s %s %s' %(sys.argv[1],sys.argv[2], sys.argv[3])
    urls, fids = helper.getexamples(sys.argv[1], sys.argv[2])
    print 'Preparing %d Files' %len(fids)
    prepare(sys.argv[2], sys.argv[3], urls, fids)

