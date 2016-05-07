# `NewsExtractor` 

`NewsExtractor` is a classifier that extracts title, date and content from webnews articles

It is implemented using python's `scikitlearn`  machine libraries
 and [`lxmls html parser`](http://lxml.de/parsing.html)


## Usage

The files in this repository can be  used for collecting data, training a model and classifying a webnews article. 

###Collecting data
The data is collected using a chrome extension which is present @ chromeextension/. Read this to know how to use the extension to collect data. The chrome extension helps you collect unique xpath expressions of 'Title', 'Date' and 'Content'.

###Learning
To collect features from the annotated data 
```run bash prepare_data.sh <featurename>```
where featurename is a valid classname in experiments/NewsExtractor/feature.py
This aligns the ground truth data, extracts required features for the examples and places them in data/<featurename> as numpy matrix.
Ensure you are connected to the internet. This may take 5-10 minutes based on your internt speed.
NewsExtractor/prepare.py 
Play around with the ipython notebooks present in experiments/NewsExtractor/Model to learn a machine learning classifier. 

##Classification
After you are done learning place the required pickle files (vectorizer and classifier) in models and ensure NewsExtractor.py loads the right model. The software comes with a default model also.

The classifier exposes a function ``` NE.predict(filename) ```  that predicts the title, date and content where a filename can be a URL or a filename in your filesystem.

###Example usage
```
NW = NewsExtractor()
	NW.predict('http://www.dailythanthi.com/News/Districts/Chennai/2016/04/27013547/TASMAC-make-money--Attempted-robberyGuardianCut-and.vpf')
	print '---**'*10
	print 'Title is %s ' %unicode(NW.title)
	print '---**'*10
	print 'Published date is %s ' %unicode(NW.date)
	print '---**'*10
	print 'Content is %s ' %unicode(NW.content)
```


### Benchmarking
run ```bash eval.sh``` to run the compare Newspaper,LibExtract,Goose and Boilerpipe . Ensure that these modules are installed in your machine. The evaluation runs for 100 files computing fscores for each document (Bag of words assumption). These fscores are finally recorded in Body_eval.txt and Title_eval.txt

