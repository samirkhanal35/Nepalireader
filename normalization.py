def normalize(heighty,widthx,img1):
    import numpy as np
    import math
    import cv2

    img2 = np.zeros((heighty,widthx,1),np.uint8)
    Imax = 255
    Imin = 0

    rmin=0
    rmax=0
    #mxn = heighty*widthx
    
    rcount=np.zeros(256,np.uint)
    rcounts=[]
    for i in range(0,heighty):
        for j in range(0,widthx):
            rcount[int(img1[i][j])]+=1
            img2[i][j]=img1[i][j]

    countmin=min(rcount)
    countmax=max(rcount)
    flagmin=1
    flagmax=1
    for levels in range(0,256):
        if rcount[levels]>0 and flagmin==1:
            rmin=levels
            flagmin=0
        if rcount[255-levels]>0 and flagmax==1:
            rmax=255-levels
            flagmax=0
    print("rmin = "+str(rmin)+"  rmax = "+str(rmax))

    if rmax<Imax or rmin>Imin:
        for r in range(rmin,rmax+1):
            if rcount[r]>0:
                sub=(Imax-Imin)*((r-rmin)/(rmax-rmin))+Imin
                if sub>255:
                    sub=255
                if sub<0:
                    sub=0
                sub=int(round(sub,0))
                s=int(sub)
                #print("r="+str(r)+" s="+str(s))
                for i in range(0,heighty):
                    for j in range(0,widthx):
                        if img2[i][j]==r:
                            img1[i][j]=int(s)
