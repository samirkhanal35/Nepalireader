def topcorsegmentation(ctop,ccore,hlow,hup,img,cword,m_c,m_b,m_t):
    import numpy as np
    import cv2 as cv
    import image
    import topsegmentor as Ts
    import corebotsegmentor as CBs
    h,w,ch=img.shape
    a=""
    if hup>2:
        #cv.imshow("asdf"+str(cword),img)
        imgtopstrip = np.zeros((hup,w,1),np.uint8)
        for i in range(0,hup):
            for j in range(0,w):
                imgtopstrip[i][j]=img[i][j]
        a = Ts.topsegmentation(imgtopstrip,ctop,m_t)

    imgcorebotstrip = np.zeros((h-hlow,w,1),np.uint8)
    for i in range(0,h-hlow):
        for j in range(0,w):
            imgcorebotstrip[i][j]=img[hlow+i][j]
    b = CBs.corebotsegmentation(imgcorebotstrip,ccore,m_c,m_b)
    return (a+b)    

    
