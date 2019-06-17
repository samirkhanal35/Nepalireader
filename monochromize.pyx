from __future__ import print_function
from cython cimport view

def monochrome(num1,num2,img):
    cdef int a = int(num1)
    cdef int b = int(num2)                   
    cdef img1 = view.array(shape=(a, b), itemsize=sizeof(int), format="i")
        
    
    for i in range(0,num1):
        for j in range(0,num2):
            img1[i][j]=img[i][j][0]              
            
    return img1	
