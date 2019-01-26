import cv2
#from __future__ import print_function
import gray
import numpy as np
from monochromize import monochrome
from medianfilter import filter
from matplotlib import pyplot as plt
from binarize import binarize

inp_img=cv2.imread("111.jpg")
heighty,widthx,ch=inp_img.shape
grayed_image = gray.gray(heighty,widthx,inp_img)
#plt.imshow(grayed_image, cmap = 'gray')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()
img = monochrome(heighty,widthx,grayed_image)
print(img.shape)
filtered_img = filter(heighty,widthx,img)
print(img.shape)
plt.imshow(filtered_img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''

binarized_img = binarize(heighty,widthx,filtered_img)
plt.imshow(binarized_img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


#cv2.destroyAllWindows()
#a=main(variables.img,variables.heighty,variables.widthx,variables.ch)'''
