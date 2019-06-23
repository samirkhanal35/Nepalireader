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

def gauss(heighty,widthx,img1):
    import math
    import numpy as np
    pi=3.1416
    sigma=1.2015
    u=2
    l=1
    a=0
    b=0
    print(heighty,widthx)
    
    for h in range(u,heighty+u):
        b=0
        for w in range(u,widthx+u):
            x=h-u
            y=w-u
            q=[]
            for i in range(a,h):
                for j in range(b,w):                    
                    d=((-1)*((i-x)**2+(j-y)**2))/(2*(sigma**2))
                    p=math.exp(d)
                    g=p/(2*pi*(sigma**2))
                    if i<heighty and j<widthx:
                        G=g*img1[i,j]/0.38
                    else:
                        G=g*255/0.38
                    q.append(G)           
            value=int(np.sum(q))
            img1[x,y]=value
            b=b+1
        a=a+1
            
import numpy as np
import math
import cv2

def normalize(heighty,widthx,img1):
    

    img2 = np.zeros((heighty,widthx,1),np.uint8)
    Imax = 285
    Imin = -30

    rmin=0
    rmax=0
    
    rcount=np.zeros(256,np.uint)
    rcounts=[]
    for i in range(0,heighty):
        for j in range(0,widthx):
            rcount[int(img1[i][j])]+=1
            img2[i][j]=img1[i][j]

    countmin=min(rcount)
    countmax=max(rcount)
    flagmin=1
    flagmax=1
    for levels in range(0,256):
        if rcount[levels]>0 and flagmin==1:
            rmin=levels
            flagmin=0
        if rcount[255-levels]>0 and flagmax==1:
            rmax=255-levels
            flagmax=0
    print("rmin = "+str(rmin)+"  rmax = "+str(rmax))

    if rmax<Imax or rmin>Imin:
        for r in range(rmin,rmax+1):
            if rcount[r]>0:
                sub=(Imax-Imin)*((r-rmin)/(rmax-rmin))+Imin
                if sub>255:
                    sub=255
                if sub<0:
                    sub=0
                sub=int(round(sub,0))
                s=int(sub)
                #print("r="+str(r)+" s="+str(s))
                for i in range(0,heighty):
                    for j in range(0,widthx):
                        if img2[i][j]==r:
                            img1[i][j]=int(s)

