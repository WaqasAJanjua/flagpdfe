from sklearn.model_selection import train_test_split , KFold , cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def buildmodel(X, y):
    num_folds = 10
    seed = 7
    kfold = KFold(n_splits=num_folds)#, randoml_state=seed)
    
    

    
    #results = cross_val_score(model1, X_train,y_train, cv=kfold)
    
    #h = model.fit(X_train,y_train,None)
    #predicted = model.predict(X_test)
    #print (classification_report( y_test,predicted ))
    #cm = confusion_matrix(y_test, predicted)
    #print (cm)
    #model1 = SVC()
    #model = RandomForestClassifier(n_estimators=100, max_features=5)
    model = DecisionTreeClassifier()
  #  model = SVC(C=1, kernel='rbf', degree=3, gamma='auto')
    results = cross_val_score(model, X, y, cv=kfold)
    return model