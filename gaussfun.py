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
            
