import pandas as pd 
import time
import joblib

from featureseng import get_features
from modelbuild import buildmodel
from buildmetadata import buildmetadata

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
model = buildmodel(X,y)
filename = 'finalized_model.sav'
joblib.dump(model, filename)
print ("training time:", round(time.time()-t0, 3), "s")
h = model.fit(X,y,None)

print('Starting FLAG-PDFx ... ')
for i in range(len(fdr)):
    
    test = pd.read_csv(r'datasets/all/'+fdr[i]+'alL.csv')
    test_file = test['filename']
    
    '''
    Step 2 - Features Extraction
    '''
    print('Features Extraction')

    da1 = get_features(test)

    text = da1["Text"]
    del da1["Text"]
    
    print('Section Extraction')
    
    #predicted = model.predict(X_test)
    da1.fillna(0, inplace=True)
    
    predicts = model.predict(da1)
    #print(predicts)
    da1['LABEL'] = predicts
    da1['Text'] = text
    da1['filename'] = test_file
    
    print('Metadata Extraction')
    buildmetadata(da1,fdr[i])