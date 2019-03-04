import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import csv

def create_model():
	model = Sequential()
	model.add(Dense(512,activation='relu',input_shape=(1024,)))
	model.add(Dense(100,activation='relu'))
	model.add(Dense(2,activation='softmax'))
	model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model 


dataset = pd.read_csv("dataset_bottom.csv",sep=",",header=None)

labels = dataset[0]
features = dataset.loc[:,1:1024]
model = create_model()
model.fit(features,labels,batch_size=10,epochs=10)

model.save_weights('bottom_model_weights.h5')
