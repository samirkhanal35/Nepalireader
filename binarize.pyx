from __future__ import print_function
from cython cimport view

def binarize(num1,num2,img):
    cdef int i,j
    cdef img1 = view.array(shape=(num1,num2), itemsize=sizeof(int), format="i")
    img1 = img    
    
    for i in range(1,num1-1):
        for j in range(1,num2-1):
            if img1[i,j]<=128:
                img[i,j]=0
            else:
                img[i,j]=255
    return img1	


