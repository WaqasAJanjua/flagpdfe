import pandas as pd 
import time
import joblib

from featureseng import get_features
from ann import ann_buildmodel
#from buildmetadata import buildmetadata

fdr = [
  's',
  'm',
  'a',
  'e',
  'i']

data = pd.read_csv(r'datasets/all/main.csv')


   #Block_No	Seq_num	pageno	toppage	top	left	height	width	fonts_type	fonts_size		Text
y = data["LABEL"]
#del data["File"]
del data["LABEL"]
 
print('Features Extraction for Model')
da = get_features(data)
del da["Text"]
X = da
X.fillna(0, inplace=True)
t0 = time.time()
print('Model Building')
model = ann_buildmodel(X,y)