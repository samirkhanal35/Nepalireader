def model_creation(outNum):
    from keras.models import Sequential
    from keras.utils import np_utils
    from keras.layers import Dense, Dropout,Activation,Conv2D,MaxPooling2D,Flatten
    from keras.optimizers import Adam
    model = Sequential()
    model.add(Conv2D(32,(3,3),padding='same',activation='relu',input_shape=(32,32,1)))
    model.add(MaxPooling2D(pool_size=(3,3)))
    model.add(Conv2D(64,(3,3),padding='same',activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(300,activation='relu'))
    model.add(Dense(200,activation='relu'))
    model.add(Dense(outNum,activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy',optimizer=Adam(lr=0.01),metrics=['accuracy'])
    return model
