from fontsmapping import get_fontmapping 
import re
import pandas as pd 
def get_features(data):
    _firstchar = data["Text"].values
    hasTable = []
    hasFigure = []
    hasAck = []
    hasRef = []
    hasR = []
    hasAbstract = []
    hasAt = []
    allcap = []
    _fonttype = data["fonts_type"].values
    
    data = get_fontmapping(data)
    
    for i in range(len(_firstchar)):
        try: 
            if _firstchar == None:
                _firstchar = 'a'
        except:
            _firstchar = 'a'
           
    #    try:
    #        b = re.search("TABLE", _firstchar[i][0:5].upper()).start()
    #        b = 1
    #    except:
    #        b = 0    
    #    hasTable.append(b) 
        try:
            b = re.search("FIG.", _firstchar[i][0:4].upper()).start()
            b = 1
        except:
            b = 0
        hasFigure.append(b)
        try:
            b = int(_firstchar[i].isupper())
        except:
            b = 0
        allcap.append(b)            
        try:
            b = re.search("ACK", _firstchar[i][0:3].upper()).start()
            b = 1
        except:
            b = 0    
        hasAck.append(b) 
        try:
            b = re.search("RE", _firstchar[i][0:2].upper()).start()
            b = 1
        except:
            b = 0    
            hasRef.append(b) 
        try:
            b = re.search("R", _firstchar[i][0:1].upper()).start()
            b = 1
        except:
            b = 0    
        hasR.append(b) 
        try:
            b = re.search("@", _firstchar[i][0:1].upper())
            b = 1
        except:
            b = 0    
        hasAt.append(b) 
        try:
            b = re.search("(TAB|TABLE|Tab|Table)(.(\s)|\s)[(1-9)\d{0,1}|MDCLXVI](.|\s|\n)", _firstchar[i].upper()).start()
            b = 1
        except:
            b = 0    
        hasTable.append(b) 
        try:
            b = re.search("ABSTRACT", _firstchar[i].upper()).start()
            b = 1
        except:
            b = 0    
        hasAbstract.append(b) 
        

        
    da = pd.DataFrame({'pageno' : data['pageno'], 'top' : data['top'], 'fonts_size' : data['fonts_size']  
                 ,'hasAck':hasAck ,'hasAt'  :hasAt 
                 , 'Allcap':allcap 
                 , 'hasTable' : hasTable,'hasFigure' : hasFigure, 
                 #'fonts_type' : data['fonts_type'],
          'hasRef' : hasRef , 'hasR':hasR  , 'hasAbstract' : hasAbstract   ,'Text' : data["Text"]         })

    isbold = []
    isItalic = []


    for i in range(len(_fonttype)):
        try:
            b = re.search("(BOLD|CMBX|\-B|TIMESB|\.B)", _fonttype[i].upper()).start()
            b = 1
        except:
            b = 0
        isbold.append (b)
        try:
            it = re.search("(ITAL|CMMI|\-I|IT|TIMESI|\.I)", _fonttype[i].upper()).start()
            it = 1
        except:
            it = 0
        isItalic.append(it)

    
    da["italic"] = isItalic
    da["Bold"] = isbold


    return da