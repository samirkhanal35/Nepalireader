
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
		model.add(Dense(71,activation='softmax'))
		model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
		return model 

	
	model = create_model()
	model.load_weights('core_model_weights.h5')
	img1 = cv.resize(img,(32,32),interpolation = cv.INTER_CUBIC)
	b = np.zeros((1,1024),np.uint8)
	for i in range(0,32):
		for j in range(0,32):
			b[0,j+(i*32)]=(img1[i,j])
	
	a = model.predict_classes(b)
	
	dict={0:'ddha',1:'a',2:'i',3:'u',4:'uu',5:'RRI',6:'e',7:'ka',8:'kha',9:'ga',
      10:'gha',11:'nga',12:'cha',13:'Cha',14:'ja',15:'jha',16:'~na',17:'Ta',
      18:'Tha',19:'Da',20:'Dha',21:'nda',22:'ta',23:'tha',24:'da',25:'dha',
      26:'na',27:'pa',28:'pha',29:'ba',30:'bha',31:'ma',32:'ya',33:'ra',34:'la',
      35:'wa',36:'sha',37:'Sha',38:'sa',39:'ha',40:'ksa',41:'tra',42:'Gya',
      43:'k',44:'kh',45:'g',46:'Gh',47:'ch',48:'J',49:'~n',50:'nd',51:'t',
      52:'th',53:'dh',54:'n',55:'p',56:'b',57:'bh',58:'m',59:'l',60:'w',
      61:'sh',62:'Sh',63:'s',64:'ks',65:'ddhya',66:'shra',67:'tta',68:'Tra',
      69:'dadh',70:'a'}
	
	return dict[a[0]]







