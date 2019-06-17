from __future__ import print_function
from cython cimport view


cdef int min(a,b,c):
    if a<b<c:
        return a
    elif a<c<b:
        return a
    elif b<a<c:
        return b
    elif b<c<a:
        return b
    else :
        return c
     
	
cdef int max(a,b,c):
    if a>b>c:
        return a
    elif a>c>b:
        return a
    elif b>a>c:
        return b
    elif b>c>a:
        return b
    else :
        return c
	

def gray(num1,num2,img):
    cdef int i,j,red,green,blue
    cdef int a = int(num1)
    cdef int b = int(num2)                   
    cdef img1 = view.array(shape=(a, b), itemsize=sizeof(int), format="i")
    img1 = img    
    
    for i in range(0,num1):
        for j in range(0,num2):
            red=img1[i][j][2]              
            green=img1[i][j][1]            
            blue=img1[i][j][0]             
            avg=int(min(red,green,blue)//2+max(red,green,blue)//2)
            img1[i][j]=avg 
    return img1	
	
	
	
