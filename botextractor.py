def botextraction(img):
    import cv2 as cv
    import numpy as np

    h,w,ch=img.shape
    f1=0
    f2=0
    bl=0
    bt=0
    for i in range(0,h):
        count1=0
        for j in range(0,w):        
            if img[i][j]==0:
                count1 +=1
        if count1>0:
            if f2==0:
                f2=1
                bt=i

        else:
            if f2==1:
                f2=0
                bt=0
    for j in range(0,w):
        count1=0
        for i in range(0,h):
            if img[i][j]==0:
                count1 +=1
        if count1>0:
            if f1==0:
                f1=1
                bl=j

        else:
            if f1==1:
                f1=0
                bl=0
                
                
    img1=np.zeros((h-bt,w-bl,1),np.uint8)
    for ii in range(0,h-bt):
        for jj in range(0,w-bl):
            img1[ii][jj]=img[bt+ii][bl+jj]

    #cv.imshow("dfs",img1)
    return img1
                
    
