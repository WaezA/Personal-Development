from tkinter import *

from tkinter import  messagebox

coord = 10, 50, 240, 210

#ARC
arc= canvas.create_arc(coord, start = 0, extent =150, fill = "blue")

#IMAGE
filename = PhotoImage(file = "image.jpg")
image = canvas.create_image( 50, 50, anchor = NE, image=filename)

#LINE
canvas.create_line (x0, y0, x1, y1, ..., xn, yn, options)

#OVAL
oval = canvas.create_oval(x3, y3, x4, y4, options)

#POLYGON
oval2 = canvas.create_polygon(x5, y5, x6, y6, ..., yn, options)

