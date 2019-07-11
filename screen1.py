
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
            m=k+j+'.jpg'
            #time.sleep(0.1)
            print(k,j)
            im2 = pyautogui.screenshot(m)
            i=i+1
    except KeyboardInterrupt:
        print("hyyyy") 

    
    img_array = []
    for filename in glob.glob('/home/adnan/Downloads/*.jpg'):
        img = cv2.imread(filename)
        #print(img)
        height, width, layers = img.shape
        if img is NONE:
            print(" no image ************")
        size = (width,height)
        img_array.append(img)
    
    
    out = cv2.VideoWriter(k+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 2, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    """
    #now after making video now im deleting screebshots
    dir_path = os.path.dirname(os.path.realpath('.jpg')) 
    for root,dirs, files in os.walk(dir_path): 
            print(root,"   ",dirs,files)
            for file in files: 
                if file.endswith('.jpg') : 
                    
                    os.system('rm *.jpg ')
    """
    os.system('rm *.jpg')
call()