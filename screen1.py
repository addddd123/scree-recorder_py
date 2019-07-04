import pyautogui
import time
import cv2
import numpy as np
import glob
import os
k=input(" enter name of video sequence ")
im1 = pyautogui.screenshot()
i=0
j=''
while i<=10:
    
    j=str(i)
    m=k+j+'.png'
    print(k,j)
    im2 = pyautogui.screenshot(m)
    i=i+1

 
img_array = []
for filename in glob.glob('/home/adnan/Downloads/*.png'):
    img = cv2.imread(filename)
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




