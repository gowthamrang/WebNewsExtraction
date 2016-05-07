from NewsExtractor import helper, NewsExtractor
from goose import Goose
from readability.readability import Document
from boilerpipe.extract import Extractor
from libextract.api import extract


import newspaper
import codecs
import os
import sys
import urllib


import numpy as np



from nltk import word_tokenize
from collections import defaultdict



def fscore(words1,words2):
    d1 = defaultdict(float)
    d2 = defaultdict(float)
    p,r = 0.0001,0.0001
    s1 = 0.0001
    s2 = 0.0001
    for each in words1:
        d1[each]+=1
        s1+=1
    
    for each in words2:
        d2[each]+=1
        s2+=1
    
    for each in d1:
        p += min(d1[each],d2[each])
        r += min(d1[each],d2[each])
    p/=s1
    r/=s2
    
    #return p,r,2*p*r/(p+r)
    return 2*p*r/(p+r)



indir = sys.argv[1]
# outdir = sys.argv[2]
trainfile = sys.argv[2]
print indir
urls ,fids = helper.getexamples(trainfile, indir, strict=False)
urls,fids = urls[:100],fids[:100]

body_score = []
title_score = []
NW = NewsExtractor.NewsExtractor()

for eachurl,eachfid in zip(urls,fids):
	fname_title_truth = indir+ '/Title/'+ str(eachfid)+'.groundtruth'
	fname_content_truth = indir+ '/Body/'+str(eachfid) + '.groundtruth'
	try:
		with codecs.open(fname_content_truth, 'r', "utf-8") as outfile:
			data = ' '.join(outfile.readlines())
	except:
		continue

	try:
		with codecs.open(fname_title_truth, 'r', "utf-8") as outfile:
				title_true = ' '.join(outfile.readlines())
	except:
		title_true = '_'

	print fname_content_truth

	body_score.append([])
	title_score.append([])
	data = word_tokenize(data)
	title_true = word_tokenize(title_true)
	###############################################################################
	print 'Goose ...'
	goose = Goose()
	article = goose.extract(eachurl)
	body_score[-1].append(fscore(word_tokenize(article.cleaned_text), data))
	title_score[-1].append(fscore(word_tokenize(article.title), title_true))

	########################################################################################
	print 'Readability...'
	try:			
		html = urllib.urlopen(eachurl).read()
		content = Document(html).summary()
		title = Document(html).short_title()
	except:
		print 'Failed URl %s' %eachurl
		content = '_'
		title = '_'
	body_score[-1].append(fscore(word_tokenize(content), data))
	title_score[-1].append(fscore(word_tokenize(title), title_true))
	############################################################################################
	print 'Boilerpipe...'
	try:			
		article = Extractor(url=eachurl)
		title = '_'
		#title = article.getTitle()
		content = article.getHTML()
	except:
		print 'Failed URl %s' %eachurl
		content = '_'
		title = '_'
	body_score[-1].append(fscore(word_tokenize(content), data))
	title_score[-1].append(fscore(word_tokenize(title), title_true))
	######################################################################################
	print 'libextract...'
	# html = urllib.urlopen(eachurl).read()
	textnodes = list(extract(html))
	try:
		content = ' '.join(each.text_content() for each in textnodes[:5])
	except:
		print 'Not combining unicode %s' %eachurl
		content = '_'
	title = '_'
	body_score[-1].append(fscore(word_tokenize(content), data))
	title_score[-1].append(fscore(word_tokenize(title), title_true))
	#####################################################################################
	print 'NewsExtractor ....'
	NW.predict(eachurl)
	title = NW.title
	content = NW.content
	if  fscore(word_tokenize(title), title_true)<0.7:
		print 'OOOPS.......'
		print '---*--'*10
		print title
		print title_true
		raw_input()
	body_score[-1].append(fscore(word_tokenize(content), data))
	title_score[-1].append(fscore(word_tokenize(title), title_true))
	# #######################################################################################
	print 'Newspaper ....'
	try:
		s = newspaper.Article(eachurl)
		s.download()
		s.parse()
		content = s.text
		title = s.title
	except:
		print 'Downloading has failed %s ' %(eachurl)
		content = '_'
		title = '_'
	body_score[-1].append(fscore(word_tokenize(content), data))
	title_score[-1].append(fscore(word_tokenize(title), title_true))
	#####################################################################################

	print body_score[-1]
	print title_score[-1]

body_score1 = np.matrix(body_score)
title_score1 = np.matrix(title_score)
body_score.append(np.mean(body_score1,axis=0))
with open('Body_Eval.txt', 'w') as outfile:
	for each in body_score: outfile.write(str(each)+'\n')



title_score.append(np.mean(title_score1,axis=0))
with open('Title_Eval.txt', 'w') as outfile:
	for each in title_score: outfile.write(str(each)+'\n')

