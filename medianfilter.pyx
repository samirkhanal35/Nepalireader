from __future__ import print_function
from cython cimport view
import numpy as np



def filter(height,width,img):
    cdef int i,j,d,h,w
    cdef float avg 
    cdef int a = 0
    cdef int q[9]
    cdef int b = 0                   
    cdef img1 = view.array(shape=(height,width), itemsize=sizeof(int), format="i")
    img1 = img
    cdef img2 = view.array(shape=(height,width), itemsize=sizeof(int), format="i")
    img2 = img1    
    
    for d in range(5):

        for h in range(3,height,+3):
            for w in range(3,width,+3):
                q[i in range(9)]=0
                for i in range(a,h):
                    for j in range(b,w):
                        q=[img1[i,j],img1[i,j-1],img1[i,j+1],img1[i-1,j],img1[i-1,j-1],img1[i-1,j+1],img1[i+1,j],img1[i+1,j+1],img1[i+1,j-1]]
                        img2[i,j]=int(np.median(q))
                
                b=w
            a=h		
    return img2	



