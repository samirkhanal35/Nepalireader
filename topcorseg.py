def topcorsegmentation(iscounttop,iscountcore,headlow,headup,imgword,min_i,wordcount,m_c,m_b,m_t):
    import numpy as np
    import cv2 as cv
    import image
    import corebotsegmentor as cbs
    h,w,ch=imgword.shape
    flag1=0
    cb_h=h-headlow
    cleft=0
    cright=0
    charcount=0
    bot_mark=h-headlow
    bot_flag=0
    top_list=[0]*10
    bot_list=[0]*10
    
    for j in range(0,w):
        count1=0
        for i in range(0,h):
            if imgword[i,j]==0:
                count1 +=1
        
        if count1>0:
            if flag1==0:
                flag1 = 1
                cleft = j
            elif j==w-1 and flag1==1:
                cright=j
                flag1=0
                charcount+=1

        else:
            if flag1==1:
                flag1= 0
                cright = j
                charcount+=1

        if cright!=0:   
            cwidth=cright-cleft
            ff1=0
            ct_right=0
            ct_left=0
            for jtop in range(0,cwidth):
                cc1=0
                for itop in range(0,headup):
                    if imgword[itop][cleft+jtop]==0:
                        cc1 +=1
                if cc1>0:
                    if ff1==0:
                        ct_left=jtop
                        ff1=1
                    elif jtop==cwidth-1 and ff1==1:
                        ct_right=jtop
                        ff1=0
                else:
                    if ff1==1:
                        ct_right=jtop
                        ff1=0
            if ct_right!=0 and ct_right>ct_left:     #HAVING TOP MODIFIER
                imgtop=np.zeros((headup,ct_right-ct_left),np.uint8)
                for ii in range(0,headup):
                    for jj in range(0,ct_right-ct_left):
                        imgtop[ii][jj]=imgword[ii][cleft+ct_left+jj]
                top_list.insert(charcount,imgtop) #New
                
                ct_right=0
                ct_left=0
                img1=np.zeros((h-headlow-1,cwidth),np.uint8)
                for ii in range(0,h-headlow-1):
                    for jj in range(0,cwidth):
                        img1[ii][jj]=imgword[headlow+ii+1][cleft+jj]
                
            elif ct_right==0:   #POSSIBILITY OF HAVING BOTTOM MODIFIER
                if min_i<=0.75*cb_h and min_i>0.5*cb_h:
                    bot_mark=min_i
                    #print(bot_mark,headlow,h)
                if h>headlow:
                    if bot_mark!=h-headlow:
                        imgbot=np.zeros((h-bot_mark-headlow,cwidth),np.uint8)
                        for ii in range(0,h-bot_mark-headlow):
                            for jj in range(0,cwidth):
                                imgbot[ii][jj]=imgword[headlow+bot_mark+ii][cleft+jj]
                        bot_list.insert(charcount,imgbot)
                        bot_flag = 1    
                
            cleft=0
            cright=0
    #NEW***********************
    imgstrip = np.zeros((bot_mark,w),np.uint8)
    for i in range(0,bot_mark):
        for j in range(0,w):
            imgstrip[i,j]= imgword[headlow+i,j]
    a = cbs.corebotsegmentation(imgstrip,iscountcore,wordcount,min_i,top_list,bot_list,m_c,m_b,m_t)

    length = 0
    mergeMod = ""
    newMerge = ""
    aNew = ""
    flag_comb = 0
    for char in a:
        if char=="a" and flag_comb==0:
            flag_comb = 1
            mergeMod = mergeMod + char
        elif flag_comb==1:
            mergeMod = mergeMod + char
            if mergeMod=="aa":
                newMerge = "aa"
            elif mergeMod=="aii":
                newMerge = ""
            elif mergeMod=="aae":
                newMerge = "e"
            elif mergeMod=="aav":
                newMerge = "ai"
            elif mergeMod=="aaea":
                newMerge = "o"
            elif mergeMod=="aava":
                newMerge = "au"
            elif mergeMod=="aiia":
                newMerge = "ii"
            elif mergeMod=="ai":
                newMerge = "i"
            elif mergeMod=="au":
                newMerge = "u"
            elif mergeMod=="auu":
                newMerge = "uu"
            else:
                flag_comb=0
                if newMerge!="":
                    aNew = aNew + newMerge +char
                else:
                    aNew = aNew + mergeMod
                newMerge = ""
                mergeMod = ""
            if len(mergeMod)==4:
                aNew = aNew + newMerge
                flag_comb=0
                mergeMod = ""
                newMerge = ""
        else:
            aNew = aNew + char
        length +=1
        if length==len(a) and flag_comb==1:
            flag_comb = 0
            if newMerge!="":
                aNew = aNew + newMerge
            else:
                aNew = aNew + mergeMod
            
            newMerge = ""
            mergeMod = ""
    return aNew 

    
