def conshasegmentation(img,count):
    import numpy as np
    import cv2 as cv
    import image
    import core_recognize as core

    h,w,ch=img.shape
    countdot1=0
    flag=0
    rbar=0
    lbar=0
    b="" #NEW
    for j in range(0,w):
        countdot1=0
        onetimeflag=0
        for i in range(0,h):
            if img[h-1-i][w-1-j]==0:
                countdot1 +=1
        if countdot1>=0.8*h:
            if flag==0:
                flag=1
                rbar=w-1-j

        else:
            if flag==1 and onetimeflag==0:
                onetimeflag=1
                lbar=w-1-j

        if rbar!=0 and lbar!=0:
            barwidth=rbar-lbar
            conwidth=int((w-barwidth)/2)
            if lbar-conwidth<0:
                diff=0
            else:
                diff=lbar-conwidth
            img1=np.zeros((h+3,diff,1),np.uint8)
            img2=np.zeros((h+3,w-diff,1),np.uint8)
            break
        else:
            if j==w-1:
                conwidth=int(w/2)
                if lbar-conwidth<0:
                    diff=0
                else:
                    diff=lbar-conwidth
                img1=np.zeros((h+3,diff,1),np.uint8)
                img2=np.zeros((h+3,w-diff,1),np.uint8)
                break
      
    for ii in range(0,h):
        for jj in range(0,w):
            if jj<diff:
                img1[ii+3][jj]=img[ii][jj]
            else:
                img2[ii+3][jj-diff]=img[ii][jj]
    
    
    
    if diff>0:
        #cv.imwrite("extracts/core/name"+str(count)+".jpg",img1)
        b = core.recognize(img1)
        count+=1
    #cv.imwrite("extracts/core/name"+str(count)+".jpg",img2)
    a = core.recognize(img2)
    b = b+a
    count+=1
    
    return (count,b)
    
    
            
            
    
