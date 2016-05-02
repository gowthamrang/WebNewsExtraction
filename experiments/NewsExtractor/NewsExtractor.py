
#Any parser that supports xpath is all that is required
import lxml.html
import helper
import pickle

from classifier.TitleClassifier import TitleClassifier
from sklearn.feature_extraction import DictVectorizer

########################################################
import random
from time import time
from sklearn.svm import SVC
from sklearn.feature_selection import chi2
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.grid_search import RandomizedSearchCV
from operator import itemgetter
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint as sp_randint
from sklearn.cross_validation import StratifiedKFold

########################################################

class NewsExtractor:
	def __init__(self):
		"""Use this space to load trained classifier instances"""
		#self.title_classifier_instance = TitleClassifier()
		self.title_classifier_instance = pickle.load(file('models/Title.classifier'))
		self.content_classifier_instance = pickle.load(file('models/Content.classifier'))
		self.date_classifier_instance = pickle.load(file('models/Date.classifier'))


		self.title_feature_vectorizer = pickle.load(file('models/Title_featurevectorizer.dat'))
		self.content_feature_vectorizer = pickle.load(file('models/Content_featurevectorizer.dat'))
		self.date_feature_vectorizer = pickle.load(file('models/Date_featurevectorizer.dat'))

		self.title = ''
		self.content = ''
		self.date = ''


	def predict(self,filename=None):
		if not filename:
			print 'Please provide a url or a filepath'
			return ;
		try:

		 	#TODO Find encoding using chardet send it via the parser
			tree = lxml.html.parse(filename)
		except:
			print 'Unable to parse'
			return
		textnodes = helper.get_ordered_path_and_text(tree)
		X_t = self.title_feature_vectorizer.transform(helper.extract_features(textnodes, tree, 'Title'))
		X_d = self.date_feature_vectorizer.transform(helper.extract_features(textnodes, tree, 'Date'))
		X_c = self.content_feature_vectorizer.transform(helper.extract_features(textnodes, tree, 'Content'))
		
		Y_t = self.title_classifier_instance.predict(X_t)
		Y_d = self.date_classifier_instance.predict(X_d)
		Y_c = self.content_classifier_instance.predict(X_c)

		
		for i, (_,_,val) in enumerate(textnodes):
			if Y_t[i] == 1:
				self.title+= val
			
			if Y_d[i] == 1:
				self.date += val
			if Y_c[i] == 1:
				self.content+= val
		return
if __name__== '__main__':
	NW = NewsExtractor()
	NW.predict('http://www.dailythanthi.com/News/Districts/Chennai/2016/04/27013547/TASMAC-make-money--Attempted-robberyGuardianCut-and.vpf')
	print '---**'*10
	print 'Title'
	print '---**'*10
	
	print '%s ' %unicode(NW.title)
	print '---**'*10
	print 'Date'
	print '---**'*10
	
	print '%s ' %unicode(NW.date)
	print '---**'*10
	print 'Content'
	print '---**'*10
	print ' %s ' %unicode(NW.content)
