import re
#data = pd.read_csv(r'D:/Research/mypy/datasets/all/main.csv')

reg = "([A-Z]\s{0})([a-z]+)*(\s{1}[0-9]{4})(\s(\,))(\s{1}[0-9]+)\s(\,+)(\s{1}[0-9]+)(\;+)\s(doi:10.(\d)+/([^(\s\>\"\<)])+)"
pubstr =  "Appl. Sci. 2018 , 8 , 378; doi:10.3390/app8030378 www.mdpi.com/journal/applsci"
#pubstr = "Entropy 2017 , 19 , 10; doi:10.3390/e19010010 www.mdpi.com/journal/entropy"
try:
    
    search = re.search(reg,pubstr).start()

    search = 1
except:
    search = 0
_Publisherinfo = []
if search == 1:
    _Publisherinfo = re.findall(reg,pubstr)
    journalname = _Publisherinfo[0][0]+_Publisherinfo[0][1]
    publicationyear = _Publisherinfo[0][2]
    issue = _Publisherinfo[0][5]
    volume = _Publisherinfo[0][7]
    doi = _Publisherinfo[0][9]
    print(journalname)
    print(publicationyear)
    print(issue)
    print(volume)
    print(doi)
    
    print (_Publisherinfo)