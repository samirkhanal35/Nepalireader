def topsegmentation(imgstrip,iscount,m_t):
    import numpy as np
    import cv2 as cv
    import image
    from top_recognize import recognize
    h,w,ch=imgstrip.shape
    countdot1=0
    flag1=0
    flag2=0
    randomflag=0
    charleft=0
    charright=0
    ccount=iscount[0]
    b=""
    
    
    for j in range(0,w):
        countdot1=0
        for i in range(0,h):
            if imgstrip[i][j]==0:
                countdot1+=1

        if countdot1>=2:
            if flag1==0:
                flag1=1
                randomflag=0
                charleft=j

        else:
            if flag1==1:
                flag1=0
                randomflag=1
                charright=j

        if randomflag==1:
            charhigh=0
            charlow=0
            for charh in range(0,h):
                countdot2=0
                for charw in range(charleft,charright):
                    if imgstrip[charh][charw]==0:
                        countdot2 +=1

                if countdot2>0:
                    if flag2==0:
                        flag2=1
                        charhigh=charh

                else:
                    if flag2==1:
                        flag2=0
                        charlow=charh
            imgchar = np.zeros((h,charright-charleft,1),np.uint8)
            for ver in range(0,h):
                for hor in range(0,charright-charleft):
                    imgchar[ver][hor] = imgstrip[ver][charleft+hor]
                    
            #cv.imwrite("extracts/topmod/name"+str(ccount)+".jpg",imgchar)
            a = recognize(imgchar,m_t)
            b = b+a
            ccount=ccount+1
            randomflag=0
    iscount[0]=ccount
    return b
