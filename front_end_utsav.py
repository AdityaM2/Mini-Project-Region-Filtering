import tkinter as tk
from tkinter import *
from tkinter import filedialog,Text
from tkinter import *
from PIL import Image,ImageTk
import cv2

def webcam_btn_clicked():
    pass    

def exit_btn_clicked():
    cv2.destroyAllWindows()
    exit()


root= tk.Tk()

root.title("Welcome to Region Filtering Application")

canvas=tk.Canvas(root, height=550, width=500, bg="#101820")

frame=tk.Frame(canvas, bg="#101820")
frame.place(relx=0.01, rely=0.05, relwidth=0.9, relheight=0.8)

title=tk.Label(frame,text='Region Filtering', fg= '#FEE715', width=15, bg="#101820")
title.config(font=(100))
title.pack()
title.place(relx=0.35, rely=0.05)

descrption='Description of each filter:\n\n1. Pencil Sketch: This filter turns your webcam feed into beautiful hand-drawn pencil sketches.\n\n2. Sepia: Sepia effect gives your images a warm brownish tone. Sepia filter improves the general look and feel of your image.\n\n3. Paint: It creates an effect of brush strokes, which paint the image.\n\n4. Emboss: The emboss filter, also called a directional difference filter, will enhance edges in the direction of the selected convolution mask(s).\n\n5. Cartoon: It transforms the frame into a cartoon-like picture\n\n6. Green Overlay: Adds a green tint on the frame to produce a green virtual distortion'

desc=tk.Label(frame, text=descrption, bg="#101820", fg='#FEE715', justify=LEFT, wraplength=400)
desc.pack()
desc.place(relx=0.1, rely=0.25)

webcam_btn=tk.Button(frame,text='Webcam', bg='#101820', fg='#FEE715', padx=3, pady=2, command=webcam_btn_clicked, width=20)
webcam_btn.pack()
webcam_btn.place(relx=0.1, rely=0.9)

exit_btn=tk.Button(frame,text='Exit', bg='#101820', fg='#FEE715', padx=3, pady=2, command=exit_btn_clicked, width=20)
exit_btn.pack()
exit_btn.place(relx=0.65, rely=0.9)

canvas.pack()
root.mainloop()