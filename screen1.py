
from tkinter import *
def call():
    import pyautogui
    import time
    import cv2
    import numpy as np
    import glob
    import os
    k=input(" enter name of video sequence ")
    im1 = pyautogui.screenshot()
    i=1
    j=''
    try:
        while i:
            
            j=str(i)
            m=k+j+'.png'
            print(k,j)
            im2 = pyautogui.screenshot(m)
    except KeyboardInterrupt:
        print("hyyyy") 

    
    img_array = []
    for filename in glob.glob('/home/adnan/Downloads/*.png'):
        img = cv2.imread(filename)
        print(img)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    
    out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    #now after making video now im deleting screebshots
    dir_path = os.path.dirname(os.path.realpath('.png')) 
    for root,dirs, files in os.walk(dir_path): 
            print(root,"   ",dirs,files)
            for file in files: 
                if file.endswith('.png') : 
                    
                    os.system('rm *.png ')

root=Tk()
root.title("Welcome to the screenrecorder")
root.geometry("700x450")
root.configure(background="powder blue")
label=Label(root,text='Screen Recorder',fg='chocolate',bg='powder blue',font=(100,100),height=0,width=30)
label.pack(side=TOP)
root1=Frame(root,bg='powder blue')

btn1=Button(root,text="Record Screen",command=call,fg="black", width=12,height=7,bg="green" ) #ok

btn1.pack()

btn2=Button(root,text="stop",command=exit,fg="black", width=12,height=7,bg="red" ) #ok
btn2.pack()

root.mainloop()
