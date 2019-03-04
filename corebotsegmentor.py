def corebotsegmentation(imgstrip,iscount):
    import numpy as np
    import cv2 as cv
    import image
    import conshasegmentor as conseg
    import botextractor as bex
    import core_recognize as core
    import bottom_recognize as btm
    a=""
    
    h,w,ch=imgstrip.shape
    maxcharht=h
    maxcharwd=0
    flag1=0
    flag2=0
    flag3=0
    randomflag=0
    charleft=0
    charright=0
    ccount=iscount[0]
    avght=0
    avgwd=0
    hilow=[]
    hiup=[]
    wileft=[]
    wiright=[]
    hibin1=[]
    hibin2=[]
    hibin3=[]
    wibin1=[]
    wibin2=[]
    wibin3=[]
    wibin4=[]
    for j in range(0,w):
        countdot1=0
        for i in range(0,h):
            if imgstrip[i][j]==0:
                countdot1+=1

        if countdot1>=2:
            if flag1==0:
                flag1=1
                randomflag=0
                charleft=j
            if j==w-1 and flag1==1:
                flag1=0
                charright=j
                randomflag=1

        else:
            if flag1==1:
                flag1=0
                randomflag=1
                charright=j

        if randomflag==1:
            charhigh=0
            charlow=0
            flag2=0
            flag3=0
            for charh in range(0,h):
                countdot2=0
                countdot3=0
                for charw in range(charleft,charright):
                    if imgstrip[charh][charw]==0:
                        countdot2 +=1
                    if imgstrip[h-1-charh][charw]==0:
                        countdot3 +=1

                if countdot2>0:
                    if flag2==0:
                        flag2=1
                        charhigh=charh

                if countdot3>0:
                    if flag3==0:
                        flag3=1
                        charlow=h-1-charh
                        
            if charlow!=0:
                charht=charlow-charhigh
                if maxcharwd<charright-charleft:
                    maxcharwd=charright-charleft

                hilow.append(charlow)
                hiup.append(charhigh)
                wileft.append(charleft)
                wiright.append(charright)
                
                if charht>=0.8*maxcharht:
                    hibin1.append(charht)
                if charht<0.8*maxcharht and charht>0.64*maxcharht:
                    hibin2.append(charht)
                if charht<=0.64*maxcharht:
                    hibin3.append(charht)

            randomflag=0

    maxcount=max(len(hibin1),len(hibin2),len(hibin3))
    if len(hibin1)==maxcount and len(hibin1)>=1:
        avght=int(np.mean(hibin1)) 
    if len(hibin2)==maxcount and len(hibin2)>=1:
        avght=int(np.mean(hibin2))
    if len(hibin3)==maxcount and len(hibin3)>=1:
        avght=int(np.mean(hibin3))
    
    for y in range(0,len(wiright)):
        wid=wiright[y]-wileft[y]
        hiie=hilow[y]-hiup[y]
        if wid>=0.8*maxcharwd:
            wibin1.append(wid)
        if wid<0.8*maxcharwd and wid>0.64*maxcharwd:
            wibin2.append(wid)
        if wid<=0.64*maxcharwd:
            if wid/hiie<0.4:
                wibin3.append(wid*3)
            else:
                wibin3.append(wid)
            
    maxcountw=max(len(wibin1),len(wibin2),len(wibin3))
    if len(wibin1)==maxcountw and len(wibin1)>=1:
        avgwd=int(np.mean(wibin1))
    if len(wibin2)==maxcountw and len(wibin2)>=1:
        avgwd=int(np.mean(wibin2))
    if len(wibin3)==maxcountw and len(wibin3)>=1:
        avgwd=int(np.mean(wibin3))

    for x in range(0,len(hilow)):
        rat=(wiright[x]-wileft[x])/(hilow[x]-hiup[x])
        if hilow[x]-hiup[x]<=avght and avght!=0:
            imgchar = np.zeros((hilow[x]-hiup[x],wiright[x]-wileft[x],1),np.uint8)
            for ver in range(0,hilow[x]-hiup[x]):
                for hor in range(0,wiright[x]-wileft[x]):
                    imgchar[ver][hor] = imgstrip[hiup[x]+ver][wileft[x]+hor]
            if avgwd!=0:
                if wiright[x]-wileft[x]>avgwd and rat>1.2:
                    (ccount,b)=conseg.conshasegmentation(imgchar,ccount)
                    a = a+b
                else:
                    #cv.imwrite("extracts/core/name"+str(ccount)+".jpg",imgchar)
                    b = core.recognize(imgchar)
                    a = a+b
                    ccount=ccount+1
            
        if hilow[x]-hiup[x]>avght and avght!=0:
            imgchar = np.zeros((avght,wiright[x]-wileft[x],1),np.uint8)
            if hilow[x]-avght>=0.2*avght:
                imgbot = np.zeros((hilow[x]-avght,wiright[x]-wileft[x],1),np.uint8)
                for veri in range(0,hilow[x]-avght):
                    for hori in range(0,wiright[x]-wileft[x]):
                        imgbot[veri][hori] = imgstrip[avght+veri][wileft[x]+hori]
                imgbot1=bex.botextraction(imgbot)
                #cv.imwrite("extracts/bottom/name"+str(ccount)+".jpg",imgbot1)
                b = btm.recognize(imgbot1)
                a = a+b
                
            for ver in range(0,avght):
                 for hor in range(0,wiright[x]-wileft[x]):
                    imgchar[ver][hor] = imgstrip[hiup[x]+ver][wileft[x]+hor]
            if avgwd!=0:
                if wiright[x]-wileft[x]>avgwd and rat>1.2:                    
                    (ccount,b)=conseg.conshasegmentation(imgchar,ccount)
                    a = a+b
                else:
                    #cv.imwrite("extracts/core/name"+str(ccount)+".jpg",imgchar)
                    b = core.recognize(imgchar)
                    a = a+b
                    ccount=ccount+1
                        
    iscount[0]=ccount 
    return a
