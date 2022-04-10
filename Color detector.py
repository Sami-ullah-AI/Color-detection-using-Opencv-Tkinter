#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import numpy as np
import cv2
from PIL import Image, ImageTk
ash=tk.Tk()
#Run incase you have icon in png or ico format
#p1 = PhotoImage(file = 'icons8-color-detection-30.png')
#ash.iconphoto(False, p1)
ash.title("Color-Detection App")
ash.resizable(False,False)
ash.geometry('500x500+140+80')
ash.config(bg='#659DBD')
toptitle = Label(ash,text="Color Detection",bg = "dark gray",fg='white',font=('time new roman',24,'bold'),relief=GROOVE,bd=7).pack(fill=X,side=TOP)
#fun

def show_frame():
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1288)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,728)
    while True:
        _,frame=cap.read()
        hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        height,width, _=frame.shape
    
        cx=int(width/2)
        cy=int(height/2)
    
        pixel_center = hsv_frame[cy,cx]
        hue_value=pixel_center[0]
    
        color="undefined"
        if hue_value<5:
            color="RED"
        elif hue_value<22:
            color="ORANGE"
        elif hue_value<33:
            color="YELLOW"
        elif hue_value<78:
            color = "GREEN"
        elif hue_value<131:
            color="BLUE"
        elif hue_value<178:
            color="VOILET"
        
        else:
            color="RED"
        pixel_center_bgr = hsv_frame[cy,cx]
        b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
        cv2.putText(frame,color,(10,78),0,1.5,(b,g,r),2)
        cv2.circle(frame,(cx,cy),5,(25,25,25),3)
    
        cv2.imshow("Frame",frame)
        key=cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def exit():
    ash.destroy()
det_btn = Button(ash, text='Detect Colors', font=('Times New Roman', 20),command=show_frame, bg='cyan', fg='red',bd=9)
det_btn.place(relx=0.32,rely=0.35)

exit_btn = Button(ash, text='     Exit          ', font=('Times New Roman', 20),command=exit,bg='cyan', fg='red',bd=9)
exit_btn.place(relx=0.32,rely=0.54)
bottomtitle = Label(ash,text="-- Developed by Fazal and Noman--",bg = "dark gray",fg='white',font=('time new roman',16,'bold'),relief=GROOVE,bd=7).pack(fill=X,side=BOTTOM)

#color detection area

ash.mainloop()
    


# In[ ]:




