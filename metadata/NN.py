# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import tensorflow as tf
#print("TensorFlow version:", tf.__version__)

#from keras.datasets import cifar10

import pandas as pd 
import time
import joblib

from featureseng import get_features
from sklearn.model_selection import train_test_split
from cnn1dmodel import evaluate_model_cnn1d

import numpy as np

from keras.models import Model, Sequential
from keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Activation, Flatten
from keras.utils import np_utils

from sklearn import preprocessing

import numpy as np
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
batch_size = 32
num_epochs = 2
kernel_size = 3
pool_size = 2
conv_depth_1 = 32
conv_depth_2 = 64
drop_prob_1 = 0.25
drop_prob_2 = 0.5
hidden_size = 512

data = pd.read_csv(r'datasets/all/main.csv')


   #Block_No	Seq_num	pageno	toppage	top	left	height	width	fonts_type	fonts_size		Text
Y = data["LABEL"]
#del data["File"]
del data["LABEL"]

le = preprocessing.LabelEncoder()
le.fit(Y)
y = le.transform(Y)
 
print('Features Extraction for Model')
da = get_features(data)
del da["Text"]
X = da
X.fillna(0, inplace=True)
t0 = time.time()
print('Model Building')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#num_train, depth , height, width = X_train.shape
num_train = X_train.shape[0]
num_test = X_test.shape[1]
print(num_train)
print(num_test)
num_classes = np.unique(y_train).shape[0]
num_classes1 = np.unique(y_test).shape[0]
print(num_classes)
print(num_classes1)


Y_train = np_utils.to_categorical(y_train, num_classes)
Y_test = np_utils.to_categorical(y_test, num_classes)

acc = evaluate_model_cnn1d(X_train, Y_train, X_test, Y_test, num_train, num_test, num_classes)