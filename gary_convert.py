def gray_con(num1,num2,img):
    import math
    import cv2

    for i in range(0,num1):
        for j in range(0,num2):
            red=img[i,j,2]
            green=img[i,j,1]
            blue=img[i,j,0]
            avg=int(0.72*green+0.21*red+0.07*blue)
            img[i,j]=avg

