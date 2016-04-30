class TitleClassifier:
    
    def __init__(self):
        """Predicts for a single news article only"""
        pass
    
    def predict(self,X):        
        assert(X.shape[1] == 2)
        rowno = 0
        res = -1
        gotit = False
        for goodmatch,isheading in X:            
            if goodmatch == 1 and isheading==1:
                res = rowno
                break;
            if goodmatch==1 or isheading == 1 and not gotit:
                res = rowno
                gotit  = True
            rowno+=1
        Y = [0]*X.shape[0]
        print res
        if res>=0:
            Y[res] = 1
        return Y