def recognize(img,model):
    #from keras.models import Sequential
    #from keras.utils import np_utils
    #from keras.layers import Dense, Dropout,Activation,Conv2D,MaxPooling2D,Flatten
    #from keras.optimizers import Adam
    import pandas as pd
    import numpy as np
    import csv
    import cv2 as cv
    img1 = np.full((32,32),0,np.uint8)

    ht = img.shape[0]
    wt = img.shape[1]
    for ii in range(0,ht):
        for jj in range(0,wt):
            if img[ii,jj]>127:
                img[ii,jj]=0
            else:
                img[ii,jj]=255
    '''def create_model():
        model = Sequential()
        model.add(Conv2D(32,(3,3),padding='same',activation='relu',input_shape=(32,32,1)))
        model.add(MaxPooling2D(pool_size=(3,3)))
        model.add(Conv2D(64,(3,3),padding='same',activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Dropout(0.1))
        model.add(Flatten())
        model.add(Dense(300,activation='relu'))
        model.add(Dense(200,activation='relu'))
        model.add(Dense(2,activation='softmax'))
        model.compile(loss='sparse_categorical_crossentropy',optimizer=Adam(lr=0.01),metrics=['accuracy'])
        return model
    
    model = create_model()'''
    #model.load_weights('bottom_model_weights.h5')
    if wt>=ht:
        r=wt/ht
        tw=32
        th=int(tw/r)
    else:
        r=ht/wt
        th=32
        tw=int(th/r)
    img = cv.resize(img,(tw,th),interpolation = cv.INTER_CUBIC)
    sph=int((32-th)/2)
    spw=int((32-tw)/2)
    for it in range(0,th):
        for jt in range(0,tw):
            img1[it+sph,jt+spw]=img[it,jt]

    b = np.zeros((1,1024),np.uint8)
    for i in range(0,32):
        for j in range(0,32):
            ad = j+(i*32)
            b[0,ad]=(img1[i,j])
    
    b = b.reshape(-1,32,32,1)
    scale = np.max(b)
    b = b.astype(np.float32) /scale
    a = model.predict_classes(b)
    a = model.predict_classes(b)
    dict={0:'uu',1:'u'}
    return dict[a[0]]
