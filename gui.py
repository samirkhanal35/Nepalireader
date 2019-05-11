import os
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image,ImageTk
import image
import numpy as np
from mainfunc import main
top = tk.Tk()
top.title("Nepali Reader")
top.geometry("600x700")
imgicon = ImageTk.PhotoImage(file=os.path.join(r'D:\study materials\IV-I\MAJOR\codings\partOCR\imgs','nepread.ico'))
top.tk.call('wm', 'iconphoto', top._w, imgicon)
top.resizable(0,0)

#***********************************************************
class variables:
    fileName=""
    heighty=int
    widthx=int
    ch=int
    img=image
    size_of=[]
    
    img_ch=Image.open("imgs\chooseimg1.ico")
    imgch = ImageTk.PhotoImage(img_ch)

    img_strt=Image.open("imgs\startimg.ico")
    imgstrt=ImageTk.PhotoImage(img_strt)

    img_ex=Image.open("imgs\exitimg.ico")
    imgex=ImageTk.PhotoImage(img_ex)
    
    frame2 = tk.Frame(top,highlightbackground="green",
                      highlightcolor="green", highlightthickness=3,bg="white",
                      width="600", height="400", colormap="new",bd="0")
    frame2.grid(row=2,column=0)
    frame2.pack_propagate(0)

    output_txt = tk.Text(top,highlightbackground="green",
                      highlightcolor="green", highlightthickness=3,width="60", height="3",bd="0")
    output_txt.grid(row=5,column=0)
    
    L=tk.Label(frame2,bg="white",fg="green",text="(Your image appears here)")
    L.pack()
      
#***********************************************************
def design_fun():
    choose_but = tk.Button(top,text ="Choose image",font='Ariel 9',image=variables.imgch,compound="right",command=choose)
    choose_but.image=variables.imgch
    choose_but.grid(row=0,column=0)

    input_lab=tk.Label(top,text="INPUT IMAGE",font='Helvetica 11 bold')
    input_lab.grid(row=1,column=0)

    
    start_but=tk.Button(top,text="Start",font='Ariel 9',image=variables.imgstrt,compound="right",command=call_main)
    start_but.image=variables.imgstrt
    start_but.grid(row=3,column=0)

    output_lab=tk.Label(top,text="OUTPUT TEXT",font='Helvetica 11 bold')
    output_lab.grid(row=4,column=0)
    
    exit_but = tk.Button(top,text ="Exit",font='Ariel 9',image=variables.imgex,compound="right",command=call_exit)
    exit_but.grid(row=6,column=0)
#***********************************************************
def call_exit():
    exit(0)
#***********************************************************
def choose():
    variables.fileName=""
    variables.fileName=filedialog.askopenfilename(filetypes=(("JPEG","*.jpg"),
                                                   ("PNG","*.png"),
                                                   ("All Files","*.*")))  

    variables.heighty=0
    variables.widthx=0
    variables.ch=0
    if (variables.fileName!=""):
        variables.img=cv2.imread(variables.fileName)
        variables.heighty,variables.widthx,variables.ch=variables.img.shape
        img1=Image.open(variables.fileName)
        ph1=resize_img(img1,variables.widthx,variables.heighty)
        ph = ImageTk.PhotoImage(ph1)
        
        variables.L.pack_forget()
        variables.frame2.update()
        
        if ((variables.heighty>400) or (variables.widthx>600)):
            variables.heighty=int(1*variables.size_of[1])
            variables.widthx=int(1*variables.size_of[0])
            variables.img=cv2.resize(variables.img,(variables.widthx,variables.heighty),interpolation = cv2.INTER_CUBIC)
            variables.size_of=[]
        
        variables.L=tk.Label(variables.frame2,image=ph)
        variables.L.image=ph
        variables.L.pack()

#***********************************************************    
def call_main():
    if (variables.fileName!=""):
        main(variables.img)
#*********************************************************** 
def resize_img(img,widthx,heighty):
    th=heighty
    tw=widthx
    if ((heighty>400) or (widthx>600)):
        if widthx/heighty>=600/400:
            r=widthx/heighty
            w=600
            h=int(w/r)
        else:
            r=heighty/widthx
            h=400
            w=int(h/r)
        img = img.resize((w, h), Image.ANTIALIAS)
        variables.size_of.append(w)
        variables.size_of.append(h)        
    return img
#***********************************************************
design_fun()


top.mainloop()

