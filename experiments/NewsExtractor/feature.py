import re
from nltk.tag import pos_tag
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
############################
class Title:

    def set_probable_title(self, tree):
        self.title = None
        good_candidate = []
        try:            
            for each in tree.xpath("//meta"): 
                d = dict(each.items())    
                if 'property' in d and ('title' in d['property'] or 'headline' in d['property']):
                    good_candidate.append(d['content'])
            if len(set(good_candidate))>1:
                self.title = None
            else:
                self.title =  good_candidate[0]
                print 'Goodie from META', self.title
        except:
            self.title = None
        self.bestvalue, self.editscore = None, 100
        try:
            good_candidate = tree.xpath('//title/text()')
        except:
            good_candidate = None

        if good_candidate and not self.title:          
            self.title = good_candidate[0] if good_candidate[0] is not None else None
        
        print 'Goodie' ,self.title
        return



    def __init__(self, tree, textnodes=[]):
        self.set_probable_title(tree)
        if self.title != None:
            remember = [(100,None)]         
            for parentpath,_,textvalue in textnodes:
                remember.append((EditDistance(textvalue,self.title), textvalue))
            self.editscore, self.bestvalue = min(remember)
            #print sorted(remember)[:100]
            print 'HERE YE %s %d' %(self.bestvalue,self.editscore)
        return;

    def features(self,parentpath,textvalue,tree):
        feature = {}
        if self.bestvalue:
            feature['isbestTitle'] =  1 if self.bestvalue == textvalue else 0
        tag = tree.xpath(parentpath)[0].tag
        feature['isheading'] = 1 if type(tag)==str  and tag in ['h1','h2','h3','h4'] else  0
        return feature

#########################
class Date:
    def set_probable_title(self,tree):
        self.title = None
        good_candidate = []
        try:            
            for each in tree.xpath("//meta"): 
                d = dict(each.items())    
                if 'property' in d and ('title' in d['property'] or 'headline' in d['property']):
                    good_candidate.append(d['content'])
            if len(set(good_candidate))>1:
                self.title = None
            else:
                self.title =  good_candidate[0]
                print 'Goodie from META', self.title
        except:
            self.title = None
        self.bestvalue, self.editscore = None, 100
        try:
            good_candidate = tree.xpath('//title/text()')
        except:
            good_candidate = None

        if good_candidate and not self.title:          
            self.title = good_candidate[0] if good_candidate[0] is not None else None
        
        print 'Goodie' ,self.title
        return

    def probable_title(self, textnodes,tree):
        if self.title != None:
            remember = [(100,None)]         
            for i,(parentpath,_,textvalue) in enumerate(textnodes):
                remember.append((EditDistance(textvalue,self.title),i, textvalue))
            _,self.titlepos,_ = min(remember)
        return 
            



    def __init__(self,tree,textnodes=[]):
        self.date_mon_year_pattern = re.compile(r'([0-9]+[/\-. ][0-9]+?[/\-. ][0-9]+)')
        self.yearpattern = re.compile(r'([0-9]{4}?[,.])')
        self.date_mon_pattern = re.compile(r'([0-9]{1,2}?[,.])')

        self.titlepos = 0
        self.days = {
        'monday':0,
        'tueday':0,
        'wedday':0,
        'thursday':0,
        'friday':0,
        'satday':0,
        'sunday':0
        }
        self.months = {
        'jan':0,
        'feb':0,
        'mar':0,
        'april':0,
        'may':0,
        'june':0,
        'july':0,
        'aug':0,
        'sept':0,
        'oct':0,
        'nov':0,
        'dec':0
        }
        self.set_probable_title(tree)
        self.probable_title(textnodes, tree)
        self.curpos = 0
        self.maxnodes = len(textnodes)
        return


    def features(self,parentpath,textvalue,tree):
        if self.curpos > self.maxnodes:
            self.curpos =  0
        feature = {}
        match = re.search(self.date_mon_year_pattern, textvalue )
        if match:
            feature['regexp']= 1
            print 'Regexp Match %s' %textvalue
        match = re.search(self.yearpattern, textvalue )
        if match:
            feature['isyear']= 1
            

        match = re.search(self.date_mon_pattern, textvalue )
        if match:
            feature['isdate_mon']= 1

        newtext = ''.join(c if c.isalnum() else '' for c in textvalue)
        
        for each in self.months:
            if not each in newtext.lower():
                continue
            feature['ismonth'] = 1
            break;

        for each in self.days:
            if not each in newtext.lower():
                continue
            feature['isday'] = 1
            break;
        #closeness to best title
        feature['distance_from_title'] = abs(self.curpos-self.titlepos)
        def temp(x):
                for each in ['copyright', 'published', 'updated']: 
                    if each in x:
                        return 1
                return 0
        feature['keywords'] = temp(textvalue.lower())
        feature['length'] = len(textvalue.split(" "))
        feature['bias'] = 1
        feature['time'] = 1 if 'a.m' in textvalue.lower() or 'p.m' in textvalue.lower() else 0
        self.curpos+=1

        return feature

##########################




class BOW:
    def __init__(self):
        
        self.stopwords = {each:0 for each in ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]}
        self.stemmer = SnowballStemmer("english")


    def features(self,parentpath,textvalue,tree):
        features = {}

        for each in word_tokenize(textvalue):
            if each.isalpha() and each.lower() not in self.stopwords:

                features["BOW_"+self.stemmer.stem(each.lower())] = 1;
        return features






class One:
    def __init__(self,tree):
        self.Open_class = {each.strip():0 for each in'NN,NNP,NNPS, NNS, POS , PDT, VB, VBD , VBG, VBN, VBP, VBZ'.split(',')}
        self.title = tree.xpath('//title')
        self.title = self.title[0].text if self.title else ''
        self.lastbestnode = -1
        self.lastbestvalue = -100
        self. spamwords = {'click':0, 'recommend':0, 
        'share':0, 'subscribe':0, 'comment':0, 'like':0, 'read':0, 'information':0, 'info':0,
        'reach':0, 'copyright':0 }

        return


    def features(self,parentpath,textvalue,tree):
        features = {}
        parent_split = parentpath.split('/')
        for each in parent_split:
            features['ancestorTag'] = each.split('[')[0] #just get the tag from <tag>[34] if [34] exists
        
        parent = tree.xpath(parentpath)[0]
        prev = parent.getprevious()
        next = parent.getnext()
        features['parent_tag'] = parent_split[-1]
        if not textvalue or len(textvalue.strip())==0 :
            return {}
        features['word_count'] = len(textvalue.strip().split(" "))
        
        fw = functional_word_ratio(textvalue,tree, self.Open_class)
        af = appearance_features(parentpath.split('/'),tree)
        rdf = {}
        if features['parent_tag']!= 'title':
            rdf, self.lastbestnode,self.lastbestvalue = distance_from_probable_title(textnode,tree,self.lastbestnode,self.lastbestvalue, self.title)
        
        for each in af: features[each] = af[each]
        for each in fw: features[each] = fw[each]
        for each in rdf: features[each] = rdf[each]
        features['mspam'] = marketing_keyword_spam(textvalue, self.spamwords)
        #short-neighbourhood

        features['previous_tag'] = prev.tag if prev is not None and type(prev.tag)==str else '__empty__'
        features['next_tag'] = next.tag if next is not None and type(next.tag)==str else '__empty__'

        #long-term
        #how long are we past main content?
        #how long are we past title ?
        return features


def marketing_keyword_spam(val, spamwords):
    #bigram
    if not val:
        return 0
    
    #pos_tag is 2nd person
    for each in word_tokenize(val[0]):
        if each in spamwords:
            return 1
    return 0





#Take care of unicode nonsense
#Edit Dis on words
def EditDistance(x,reference):
        if x is None or reference is None:
            return 100 #Reasonably high value so that it is not ecplised
        #editdistance
        if abs(len(x)-len(reference))>100:
            return 100
        x,reference = x.lower(),reference.lower()
        #p,q = x.split(),reference.split()
        p,q = word_tokenize(x), word_tokenize(reference)

        if len(p)==0 or len(q)==0:
            return len(p)+len(q)
        #print 'Matching', x
        editdistance = [ [0 for j in range(len(q)+1)] for i in range(len(p)+1)]
        #empty string
        for i in range(len(editdistance)): editdistance[i][0] = i
        for i in range(len(editdistance[0])): editdistance[0][i] = i

        for i in range(1,len(p)+1):
            for j in range(1,len(q)+1):
                editdistance[i][j] = editdistance[i-1][j-1] if p[i-1]==q[j-1] else min([editdistance[i][j-1]+1, editdistance[i-1][j]+1, editdistance[i-1][j-1]+1])
        return editdistance[-1][-1]

# #Relative location feature
def distance_from_probable_title(textnode,tree,lastbestnode,lastbestvalue, title):
    val = tree.xpath(textnode)
    edit = 100
    if title == '' or not val:
        return  {'Title_editdistance':edit}, 0,100
        #return {'distance_from_title':0, 'Title_editdistance':1000}, 0, 0
    val = val[0]
    if abs(len(val)-len(title))>100:
        lastbestnode+=1
        return  {'Title_editdistance':100}, 0,100
        #return {'distance_from_title':lastbestnode, 'Title_editdistance':100}, lastbestnode, lastbestvalue
    edit = EditDistance(val,title)

    if lastbestvalue >= edit:
        lastbestnode = 0
        lastbestvalue = edit
    return  {'Title_editdistance':edit}, 0,100
#   return {'distance_from_title':lastbestnode, 'Title_editdistance':edit}, lastbestnode, lastbestvalue


#only font
def appearance_features(parentpath, tree):
    parent = tree.xpath(parentpath)
    attributes = parent[0].items() if parent else  []
    properties = {}
    for name,value in attributes:
        if 'font' in name or 'display' in name:
            properties[name]= value
        if 'class'  in name or 'id'  in name:
            temp = ''.join(c for c in value if c.isalnum() or c.isspace()).split() #UNICODE COMPATIBLE ?
            if 'headline'   in temp or 'title' in temp:
                properties['class'] = 'header'
            elif 'content' in temp or 'article' in temp or 'body' in temp:
                properties['class'] = 'content'

    if properties !={}: print properties
    return properties


def character_count(textnode,tree):
    return len(tree.xpath(textnode)[0]) if tree.xpath(textnode)  else 0

# #lanuage features
def functional_word_ratio(textvalue,tree, Open_class):
    tags =  pos_tag(word_tokenize(textvalue))
    d = sum([1 if each not in Open_class else 0 for _,each in tags])
    return {'functional_word_count':d , 'functional_word_ratio':d/(len(tags)+0.00001)}
