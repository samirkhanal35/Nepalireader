#from __future__ import print_function
#from cython cimport view

def monochrome(num1,num2,img):
                      
    img1 = np.zeroes((num1,num2),np.unint8)
        
    
    for i in range(0,num1):
        for j in range(0,num2):
            img1[i][j]=img[i][j][0]              
            
    return img1	

