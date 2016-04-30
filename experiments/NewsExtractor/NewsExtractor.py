
#Any parser that supports xpath is all that is required
import lxml.html
import helper
import pickle

from classifier.TitleClassifier import TitleClassifier
from sklearn.feature_extraction import DictVectorizer
from helper import *


class NewsExtractor:
	def __init__(self):
		"""Use this space to load trained classifier instances"""
		self.title_classifier_instance = TitleClassifier()
		# self.content_classifier_instance = pickle.load(file('models/Best_content.dat'))
		# self.date_classifier_instance = pickle.load(file('models/Best_date.dat'))
		self.title_feature_vectorizer = pickle.load(file('models/Best_title_dictvectorizer.dat'))
		# self.content_feature_vectorizer = pickle.load(file('models/Best_content_dictvectorizer.dat'))
		# self.date_feature_vectorizer = pickle.load(file('models/Best_date_dictvectorizer.dat'))

		self.title = ''
		self.content = ''
		self.date = ''


	def predict(self,filename=None):
		if not filename:
			print 'Please provide a url or a filepath'
			return ;
		try:
			#Find encoding send it via the parser
			tree = lxml.html.parse(filename)
		except:
			print 'Unable to parse'
			return
		textnodes = helper.get_ordered_path_and_text(tree)
		X = self.title_feature_vectorizer.transform(extract_features(textnodes, tree, 'Title'))
		
		Y_t = self.title_classifier_instance.predict(X)
		#Y_c = self.content_classifier_instance.predict(X)
		#Y_d = self.date_classifier_instance.predict(X)

		
		for i, (_,_,val) in enumerate(textnodes):
			if Y_t[i] == 1:
				self.title+= val
			# if Y_c[i] == 1:
			# 	self.content+= each
			# if Y_d[i] == 1:
			# 	self.date += each
		return
if __name__== '__main__':
	NW = NewsExtractor()
	NW.predict('http://www.dailythanthi.com/News/Districts/Chennai/2016/04/27013547/TASMAC-make-money--Attempted-robberyGuardianCut-and.vpf')
	print '---**'*10
	print 'TITLE is %s ' %unicode(NW.title)
