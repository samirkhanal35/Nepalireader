
def recognize(img):
	import keras
	from keras.models import Sequential
	from keras.layers import Dense
	import pandas as pd
	import numpy as np
	import csv
	import cv2 as cv
	
	def create_model():
		model = Sequential()
		model.add(Dense(512,activation='relu',input_shape=(1024,)))
		model.add(Dense(100,activation='relu'))
		model.add(Dense(4,activation='softmax'))
		model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
		return model
	
	model = create_model()
	model.load_weights('top_model_weights.h5')
	img1 = cv.resize(img,(32,32),interpolation = cv.INTER_CUBIC)
	b = np.zeros((1,1024),np.uint8)
	for i in range(0,32):
		for j in range(0,32):
			b[0,j+(i*32)]=(img1[i,j])
	a = model.predict_classes(b)
	dict={0:'ae',1:'av',2:'i',3:'ii'}
	return dict[a[0]]







