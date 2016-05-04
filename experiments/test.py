import os
from NewsExtractor import NewsExtractor
if __name__== '__main__':
	print os.path.realpath(__file__)

	NW = NewsExtractor.NewsExtractor()
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
