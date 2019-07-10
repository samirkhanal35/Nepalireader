def recognize(img,model):
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
    if wt>=ht:
        r=wt/ht
        tw=32
        th=int(tw/r)
    else:
        r=ht/wt
        th=32
        tw=int(th/r)
    if th==0:
        th=1
    if tw==0:
        tw=1
    img = cv.resize(img,(tw,th),interpolation = cv.INTER_CUBIC)
    sph=int((32-th)/2)
    spw=int((32-tw)/2)
    for it in range(0,th):
        for jt in range(0,tw):
            img1[it+sph,jt+spw]=img[it,jt]
    b = np.zeros((1,1024),np.uint8)
    for i in range(0,32):
        for j in range(0,32):
            b[0,j+(i*32)]=(img1[i,j])
    b = b.reshape(-1,32,32,1)
    scale = np.max(b)
    b = b.astype(np.float32) /scale
    a = model.predict_classes(b)
    dict={0:'ae',1:'av',2:'ii',3:'i'}
    return dict[a[0]]
