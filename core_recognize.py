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
    if tw == 0:
        tw = 1
    if th == 0:
        th = 1
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
    dict={0:'a',1:'i',2:'u',3:'uu',4:'RRI',5:'e',6:'ka',7:'kha',8:'ga',
          9:'gha',10:'cha',11:'chha',12:'ja',13:'jha',14:'~na',15:'Ta',
          16:'Tha',17:'Da',18:'Dha',19:'n.a',20:'ta',21:'tha',22:'da',
          23:'dha',24:'na',25:'pa',26:'pha',27:'ba',28:'bha',29:'ma',
          30:'ya',31:'ra',32:'la',33:'va',34:'sha',35:'Sha',36:'sa',
          37:'ha',38:'kchya',39:'tra',40:'gya',41:'k',42:'kh',43:'g',
          44:'ch',45:'j',46:'~n',47:'n.',48:'t',49:'th',50:'dh',51:'n',
          52:'p',53:'b',54:'bh',55:'m',56:'l',57:'v',58:'sh',59:'Sh',
          60:'s',61:'kch',62:'ddya',63:'shra',64:'tta',65:'kra',66:'dhda',
          67:'dda',68:'.na',69:'gh',70:'a'}
    
    return dict[a[0]]
