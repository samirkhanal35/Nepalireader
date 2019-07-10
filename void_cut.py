def edition(img,wcount,ccount,str1,str2,rec_model):
    import numpy as np
    import cv2 as cv
    import core_recognize as core
    import bottom_recognize as btm
    import top_recognize as tr
    h,w = img.shape
    a = ""
    flag1=0
    cleft=0
    cright=0
    cbot=h    
    
    for j in range(0,w):
        dotcount1=0
        for i in range(0,h):
            if img[i,j]==0:
                dotcount1+=1

        if dotcount1>0:
            if flag1==0:
                cleft=j
                flag1=1
            elif flag1==1 and j==w-1:
                cright=j
                flag1=0

        else:
            if flag1==1:
                cright=j
                flag1=0

        if cright!=0:
            #flag2=0
            for il in range(h-1,0,-1):
                dotcount2=0
                for jl in range(0,w-cleft):
                    if img[il,cleft+jl]==0:
                        dotcount2 +=1
                if dotcount2>0:
                    cbot=il
                    break
                    
            #cv.imshow("char"+str(wcount)+"fd"+str1+str(ccount),img1)
            if str1=="":
                img1 = np.zeros((cbot+3,cright-cleft),np.uint8)
                for ii in range(0,cbot):
                    for jj in range(0,cright-cleft):
                        img1[ii+3,jj]=img[ii,cleft+jj]
                #cv.imshow("wd"+str(wcount)+"ch"+str(ccount),img1)
                a = core.recognize(img1,rec_model)            
            elif str1=="top":
                img1 = np.zeros((cbot,cright-cleft),np.uint8)
                for ii in range(0,cbot):
                    for jj in range(0,cright-cleft):
                        img1[ii,jj]=img[ii,cleft+jj]
                #cv.imshow("wd"+str(wcount)+"ch"+str(ccount)+"top",img1)
                a = tr.recognize(img1,rec_model)
            elif str1=="bot":
                img1 = np.zeros((cbot,cright-cleft),np.uint8)
                for ii in range(0,cbot):
                    for jj in range(0,cright-cleft):
                        img1[ii,jj]=img[ii,cleft+jj]
                #cv.imshow("wd"+str(wcount)+"ch"+str(ccount)+"bot",img1)
                a = btm.recognize(img1,rec_model)
            #cv.imwrite("extracts/fornow/w"+str(wcount)+"ch"+str(ccount)+".jpg",img1)
            #ccount+=1
            cright=0
            cleft=0
    return a
    
