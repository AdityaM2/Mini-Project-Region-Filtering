import numpy as np
import cv2
import random
import math
from math import ceil

frame = cv2.imread('images.jpg')

def apply_sepia():
    frame1 = frame.copy()
    intensity = 0.7
    blue = 0 
    green = 0 
    red = 0 

    try:
        frame1.shape[3] # looking for the alpha channel
    except IndexError:
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2BGRA)

    frame_h, frame_w, frame_c = frame1.shape
    sepia_bgra = (30, 76, 122, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame1, 1.0, 0, frame1)
    cv2.imshow('Sepia', frame1)

def apply_splatter():
    splatter = frame.copy()
    frame5 = frame.copy()
    d = 5 
    
    def IsOutside(r,c,shape):
        if (c<0 or c>= shape[1]):
            return True 
        if (r<0 or r>= shape[1]):
            return True 
        #return False    

    for r in range (frame5.shape[0]):
        for c in range (frame5.shape[1]):
            r1 = r + math.ceil(random.uniform(-0.5, 0.5) * d)
            c1 = c + math.ceil(random.uniform(-0.5, 0.5) * d)

            if (IsOutside(r1,c1,frame5.shape)):
                splatter.itemset((r,c,0),0)
                splatter.itemset((r,c,1),0)
                splatter.itemset((r,c,2),0)
            else :
                splatter.itemset((r,c,0),frame5.item((r1,c1,0)))
                splatter.itemset((r,c,1),frame5.item((r1,c1,1)))
                splatter.itemset((r,c,2),frame5.item((r1,c1,2)))
    
    cv2.imshow('splatter',splatter)

def paint():
    kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,4))
    frame7 = cv2.erode(frame.copy(), kern)
    cv2.imshow('paint',frame7)

def apply_color_overlay():
    frame3 = frame.copy()
    intensity=0.5
    blue=200
    green=0
    red=0

    try:
        frame3.shape[3] # looking for the alpha channel
    except IndexError:
        frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2BGRA)
    
    frame_h, frame_w, frame_c = frame3.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame3, 1.0, 0, frame3)
    cv2.imshow('Blue', frame3)

cv2.imshow('Frame', frame)
apply_sepia()
apply_splatter()
paint()
apply_color_overlay()

cv2.waitKey(0)