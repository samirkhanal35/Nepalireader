def conshasegmentation(img,ccount,wcount,top_list,m_c,m_t):
    import numpy as np
    import cv2 as cv
    import image
    import void_cut as vc
    h,w=img.shape
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
            if lbar-conwidth<int(2*conwidth/3):
                diff=0
            else:
                diff=w-barwidth-conwidth
            img1=np.zeros((h+3,diff),np.uint8)
            img2=np.zeros((h+3,w-diff),np.uint8)
            break
        else:
            if j==w-1:
                conwidth=int(w/2)
                diff=int(w-conwidth*1.2)
                img1=np.zeros((h+3,diff),np.uint8)
                img2=np.zeros((h+3,w-diff),np.uint8)
                break
      
    for ii in range(0,h):
        for jj in range(0,w):
            if jj<diff:
                img1[ii+3][jj]=img[ii][jj]
            else:
                img2[ii+3][jj-diff]=img[ii][jj]
    
    
    
    if diff>0:
        b = vc.edition(img1,wcount,ccount,"","two",m_c)
        ccount+=1
    a = vc.edition(img2,wcount,ccount,"","two",m_c)
    b = b+a
    if type(top_list[ccount])!=int:
        c = vc.edition(top_list[ccount],wcount,ccount,"top","two",m_t)
        b = b+c
    ccount+=1
    
    return (ccount,b)
