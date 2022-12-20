# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 00:48:24 2022

@author: rwjan
"""

from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn import preprocessing


# load pima indians dataset
#dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
def ann_buildmodel(X, y):
    print(X.shape)
    print(y.shape)
    
    le = preprocessing.LabelEncoder()
    le.fit(y)
    Y = le.transform(y)
    
    model = Sequential()
#Adding 3 dense layers
    model.add(Dense(15, input_dim = 13, activation = 'relu')) # Rectified Linear Unit Activation Function
    model.add(Dense(15, activation = 'relu'))
    model.add(Dense(1, activation = 'softmax')) # Softmax for multi-class classification
# Compile model
    model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam',
              metrics= ['accuracy']
       )
# Fit the model
    model.fit(X, Y, epochs= 5, batch_size=10,  verbose=2)
# evaluate the model

    model.evaluate(X_test, Y_test, verbose=1)
    model.summary()
   #scores = model.evaluate(X, y)
   #print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))