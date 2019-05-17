import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout,Activation,Conv2D,MaxPooling2D,Flatten
from keras.optimizers import Adam

train = pd.read_csv('dataset_core2.csv',sep=",",header=None)

train_labels = train[0]
train_features = train.loc[:,1:]


train_labels = train_labels[1:]
train_features = train_features[1:]

train_features = train_features.astype(int) #astype(int) is used to convert all the values to integer.

train_features = train_features.values.reshape(-1,32,32,1)

scale = np.max(train_features)

train_features = train_features.astype(np.float32) /scale

def create_model():
    model = Sequential() 
    
    model.add(Conv2D(32,(3,3),padding='same',activation='relu',input_shape=(32,32,1)))
    
    model.add(MaxPooling2D(pool_size=(3,3)))
    
    model.add(Conv2D(64,(3,3),padding='same',activation='relu'))
    
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(300,activation='relu'))
    
    model.add(Dense(200,activation='relu'))
    
    model.add(Dense(71,activation='softmax'))
    
    model.compile(loss='sparse_categorical_crossentropy',optimizer=Adam(lr=0.01),metrics=['accuracy'])
    
    return model

model = create_model()
model.fit(train_features,train_labels,epochs=100,batch_size=32,validation_split=0.4,verbose=1)

model.save_weights('core_model_weights.h5')

