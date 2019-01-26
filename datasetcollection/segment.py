from __future__ import print_function
import cv2 as cv
import gray
import numpy as np
from monochromize import monochrome
import math

from matplotlib import pyplot as plt
from binarize import binarize



def segFun(heighty,widthx,img):
    
    #import image as img1
    
    

    c=[]

    i=0
    flag_dot=0
    flag_dots=0
    i_low=0
    i_high=0
    j_left=0
    j_right=0
    i_nhigh=0
    i_nlow=0
    iscount=0

    while (i<=heighty-1):
        count_dot=0
        for j in range(0,widthx-1):
            avalue=np.mean(img[i,j])
            if (avalue==0):
                count_dot=count_dot+1
                
        if count_dot>=4:
            if flag_dot==0:
                flag_dot=1
                i_high=i-1
        else:
            if flag_dot==1:
                flag_dot=0
                i_low=i     
            else:
                flag_dot=0

        if ((i_low!=0) & (i_high!=0)):
            flag_dots=0
            for line_j in range(0,widthx-1):
                lj=line_j
                count_cr=0
                for line_i in range(i_high,i_low):
                    avalue1=np.mean(img[line_i,line_j])
                    if (avalue1==0):
                        count_cr=count_cr+1

                if count_cr>=1:
                    if flag_dots==0:
                        flag_dots=1
                        j_left=line_j-1
            
                else:
                    if flag_dots==1:
                        flag_dots=0
                        j_right=line_j
                    else:
                        flag_dots=0
                    

                if ((j_left!=0) & (j_right!=0)):
                    flag_dotd=0
                    for v_i in range(i_high,i_low+1):
                        count_cv=0
                        for h_j in range(j_left,j_right+1):
                            avalue2=np.mean(img[v_i,h_j])
                            if (avalue2==0):
                                count_cv=count_cv+1
                        if count_cv>=1:
                            if flag_dotd==0:
                                flag_dotd=1
                                i_nhigh=v_i
                                for drawn_j in range(j_left,j_right+1):
                                    img[v_i-1,drawn_j]=255
                                    

                            else:
                                img[v_i-1,j_left]=255
                                
                                img[v_i-1,j_right]=255
                                

                                
                        else:
                            if flag_dotd==1:
                                flag_dotd=0
                                i_nlow=v_i
                                for drawn_j in range(j_left,j_right+1):
                                    img[v_i,drawn_j]=255
                                    

                                img[v_i-1,j_left]=255
                                
                                img[v_i-1,j_right]=255
                                

                    #newly added

                    hs=abs(i_nlow-i_nhigh)
                    ws=abs(j_right-j_left)
                    img1 = np.zeros((hs,ws), np.uint8)
                    img1[:] = 255
                    for i_s in range(1,hs):
                        for j_s in range(1,ws):
                            img1[i_s,j_s]=img[i_nhigh + i_s , j_left + j_s]
                    img1=cv.resize(img1,(32,32),interpolation = cv.INTER_CUBIC)
                    cv.imwrite("%d.jpg"%iscount,img1)
                    iscount = iscount+1
                    #plt.imshow(img1, cmap = 'gray')
                    #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
                    #plt.show()
                    #cv.imshow("demos(%d)"%iscount,img1)

                    #c.append(rg.recognize(img1))




                    #********
                    j_right=0
                    j_left=0

            i_high=0
            i_low=0
        i=i+1

    






inp_img=cv.imread("017.jpg")
heighty,widthx,ch=inp_img.shape
grayed_image = gray.gray(heighty,widthx,inp_img)
img1 = monochrome(heighty,widthx,grayed_image)
img = binarize(heighty,widthx,img1)
segFun(heighty,widthx,img)

'''
plt.imshow(filtered_img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


binarized_img = binarize(heighty,widthx,filtered_img)
plt.imshow(binarized_img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


#cv2.destroyAllWindows()
#a=main(variables.img,variables.heighty,variables.widthx,variables.ch)'''
