# -*- coding: utf-8 -*-
"""
Created on Tue May 14 07:50:48 2019

@author: behal
"""

def text_to_speech(a):
    from gtts import gTTS
    import os
    myobj = gTTS(text=a, lang='hi', slow=False)
    myobj.save("welcome1.mp3")
    os.system("mpg321 welcome.mp3")
    return