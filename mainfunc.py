def main(img,model_core,model_top,model_bot):
    import cv2
    import numpy as np
    import gary_convert as gc
    
    import binarize as br
    import segment as sg
    import gaussfun as gau
    import normalization as norm
    heighty,widthx,ch=img.shape
    #cv2.imshow("input",img)
    img1=np.zeros((heighty,widthx),np.uint8)
    print(ch)
    #*********************************************
    gc.gray_con(heighty,widthx,img)
    for i in range(0,heighty):
        for j in range(0,widthx):
            img1[i][j]=img[i,j,0]
    print("Grayed")
    #cv2.imshow("Gray conversion",img1)
    #*********************************************
    '''nr.noisered(heighty,widthx,img1)
    print("filtered")'''
    #*********************************************
    gau.gauss(heighty,widthx,img1)
    #cv2.imshow("Gaussian Blurring",img1)
    #*********************************************
    norm.normalize(heighty,widthx,img1)
    print("Normalized")
    #cv2.imshow("contrast stretching",img1)
    #*********************************************
    br.bin_(heighty,widthx,img1)
    print("Binarized")
    #cv2.imshow("binarization",img1)
    #*********************************************
    a = sg.segFun(heighty,widthx,img1,model_core,model_top,model_bot)
    
    print("Segmented")
    return a
