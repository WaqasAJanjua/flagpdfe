# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:57:35 2022

@author: rwjan
"""
from keras.layers import Dense , Input
from keras.layers import Flatten
from keras.layers import Dropout
from keras.models import Model, Sequential
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.utils import np_utils
from keras.layers import concatenate
from keras.utils.vis_utils import plot_model

def evaluate_model_cnn1d(trainX, trainy, testX, testy, num_train, num_test, num_classes):
    n_timesteps, n_features, n_outputs = trainX.shape[0], trainX.shape[1], trainy.shape[0]
	#verbose, epochs, batch_size = 0, 10, 32
	#n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
 	# head 
    inputs1 = Input(shape=(None, num_train,num_test))
    conv1 = Conv1D(filters=16, kernel_size=3, activation='relu')(inputs1)
    drop1 = Dropout(0.5)(conv1)
    #pool1 = MaxPooling1D(pool_size=2)(drop1)
    flat1 = Flatten()(drop1)
	# head 2
   # inputs2 = Input(shape=(num_train,num_test))
    conv2 = Conv1D(filters=16, kernel_size=5, activation='relu')(inputs1)
    drop2 = Dropout(0.5)(conv2)
    #pool2 = MaxPooling1D(pool_size=2)(drop2)
    flat2 = Flatten()(drop2)
	# head 3
   # inputs3 = Input(shape=(num_train,num_test))
    conv3 = Conv1D(filters=16, kernel_size=11, activation='relu')(inputs1)
    drop3 = Dropout(0.5)(conv3)
   # pool3 = MaxPooling1D(pool_size=2)(drop3)
    flat3 = Flatten()(drop3)
	# merge
    merged = concatenate([flat1, flat2, flat3])
	# interpretation
    dense1 = Dense(100, activation='relu')(merged)
    outputs = Dense(n_outputs, activation='softmax')(dense1)
    model = Model(inputs=[inputs1, inputs2, inputs3], outputs=outputs)
	# save a plot of the model
    plot_model(model, show_shapes=True, to_file='multichannel.png')
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit([trainX,trainX,trainX], trainy, epochs=1, batch_size=5, verbose=0)
	# evaluate model
    #_, accuracy = model.evaluate([testX,testX,testX], testy, batch_size=10, verbose=0)
    #return accuracy

