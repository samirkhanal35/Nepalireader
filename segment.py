def segFun(heighty,widthx,img1,model_core,model_top,model_bot):
    import numpy as np
    import cv2 as cv
    import topcorseg as tcseg
    words = []

    i=0
    flag_line=0
    flag_word=0
    flagChar = 0
    flagAgain = 0
    f1=0
    f2=0
    randomFlag=0
    anoflag=0
    i_low=0
    i_high=0
    j_left=0
    j_right=0
    i_nhigh=0
    i_nlow=0
    charlow=0
    wordhigh=0
    wordlow=0
    iscounttop=[]
    iscountcore=[]
    coreTHheight=[]
    wordcount=0
    iscounttop.append(0)
    iscountcore.append(0)

    while (i<=heighty-1):
        count_dot1=0        
        for j in range(0,widthx-1):
            avalue=img1[i,j]
            if (avalue==0):
                count_dot1+=1
                
        if count_dot1>=3:
            if flag_line==0:
                flag_line=1
                i_high=i
        else:
            if flag_line==1:
                flag_line=0
                i_low=i     
            else:
                flag_line=0
        
        #******
        if ((i_low!=0) and (i_high!=0)):
            countbotdot=0
            #anoflag==0
            lineHeight = abs(i_low-i_high)
            i_li=i_low+1
            while(i_li<heighty):
                countbotdot=0
                for j_li in range(0,widthx-1):
                    if img1[i_li][j_li]==0:
                        countbotdot+=1
                        
                if countbotdot>2:
                    if anoflag==0:
                        anoflag=1
                        
                else:
                    if anoflag==1:
                        anoflag==0
                        i_low=i_li
                        break
                    
                if i_li>int(i_low+lineHeight*0.10) and anoflag==0:
                    break

                i_li +=1
                        
        #******
        if ((i_low!=0) and (i_high!=0)):    #A line is detected after Horizontal Projection.
            lineHeight = abs(i_low-i_high)
            i=i_low-1
            for j_line in range(0,widthx-1):
                count_dot2=0
                for i_line in range(i_high,i_low+1):
                    if img1[i_line][j_line]==0:
                        count_dot2+=1

                if count_dot2>=1:
                    if flag_word==0:
                        flag_word = 1
                        j_left = j_line-1

                else:
                    if flag_word==1:
                        flag_word = 0
                        j_right = j_line
                        wordcount+=1

                if (j_left!=0 and j_right!=0):      #A word is detected after Vertical Projection.
                    wordwidth = abs(j_right-j_left)
                    f1=0
                    f2=0
                    for i_w in range(i_high,i_low+1):
                        count_dot3=0
                        count_dot4=0
                        for j_w in range(j_left,j_right+1):
                            if img1[i_w][j_w]==0:
                                count_dot3+=1
                            if img1[i_low-i_w+i_high][j_w]==0:
                                count_dot4+=1
                            
                        if count_dot3>0:
                            if f1==0:
                                f1=1
                                wordhigh=i_w

                        if count_dot4>0:
                            if f2==0:
                                f2=1
                                wordlow=i_low-i_w+i_high

                    if wordlow!=0 and wordhigh!=0:
                        hedlist=[]
                        headup = 0
                        flagto=0
                        
                        for i_word in range(wordhigh,wordlow+1):
                            count_dot3=0
                            for j_word in range(j_left,j_right+1):
                                if img1[i_word][j_word]==0:
                                    count_dot3+=1
       
                            if count_dot3>=0.775*wordwidth:
                                flagto=1
                                hedlist.append(i_word)
                                for pixels in range(j_left,j_right+1):
                                    img1[i_word][pixels]=255
                            else:
                                if flagto==1:
                                    break
                                    

                        if len(hedlist)>0:
                            headlow=hedlist[len(hedlist)-1]-wordhigh
                            headup=hedlist[0]-wordhigh
                            imgword = np.zeros((wordlow-wordhigh,j_right-j_left,1),np.uint8)
                            min_histo=j_right-j_left
                            min_x=0
                            for x in range(0,wordlow-wordhigh):
                                histo_count=0                       #NEW
                                for y in range(0,j_right-j_left):
                                    imgword[x][y]=img1[wordhigh+x][j_left+y]
                                    if imgword[x][y]==0 and x>headlow:  #NEW
                                        #imghisto[x-headlow][histo_count]=0  #NEW
                                        histo_count+=1  #NEW
                                
                                if histo_count<=min_histo and x>headlow:  #NEW
                                    min_x=x-headlow             #NEW
                                    min_histo=histo_count
                            if headup!=0 or headlow!=0:
                                a = tcseg.topcorsegmentation(iscounttop,iscountcore,headlow,headup,imgword,min_x,wordcount,model_core,model_bot,model_top)  
                            words.append(a)
                        wordhigh=0
                        wordlow=0    

                    j_left=0
                    j_right=0    
            i_low=0
            i_high=0
        i+=1
    print("word="+str(wordcount))
    return words

    
                            
                        
            
