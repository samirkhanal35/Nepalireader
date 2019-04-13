def bin_(num1,num2,img1):
    import cv2
    import numpy as np
    import math
    
    for i in range(1,num1-1):
        for j in range(1,num2-1):
            gray=img1[i,j]
            if gray<=127:
                img1[i,j]=0
            else:
                img1[i,j]=255
            
        
