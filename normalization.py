def normalize(heighty,widthx,img1):
    import numpy as np
    import math
    import cv2

    img2 = np.zeros((heighty,widthx,1),np.uint8)
    Imax = 285
    Imin = -30
    Idif = Imax-Imin
    rmin=0
    rmax=0
    rcount=np.zeros(256,np.uint8)
    news=np.zeros(256,np.uint8)
    for i in range(0,heighty):
        for j in range(0,widthx):
            rcount[img1[i][j]]+=1

    countmin=np.min(rcount)
    countmax=np.max(rcount)
    flagmin=1
    flagmax=1
    for levels in range(0,256):
        if rcount[levels]>0 and flagmin==1:
            rmin=levels
            flagmin=0
        if rcount[255-levels]>0 and flagmax==1:
            rmax=255-levels
            flagmax=0
        if flagmin==0 and flagmax==0:
            break
    if rmax<Imax or rmin>Imin:
        rdif=rmax-rmin
        for r in range(rmin,rmax+1):
            sub=Idif*(r-rmin)/rdif+Imin
            if sub>255:
                sub=255
            if sub<0:
                sub=0
            s=int(round(sub,0))
            news[r]=s
                
        for i in range(0,heighty):
            for j in range(0,widthx):
                img1[i][j]=news[img1[i][j]]
