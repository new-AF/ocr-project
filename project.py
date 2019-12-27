import os
import Tkinter as t
from PIL import ImageTk,Image

top = t.Tk()
top.title("ocr toolbox")

##U+2589

#detour = lambda i: visible(top)
#top.bind('<Visibility>',detour)

#top.tk_bisque()
image = ImageTk.PhotoImage(Image.open('test1.jpg'))

c = t.Canvas(top,) # cursor = 'hand2'
l = t.Label(top,image = image)
#c.create_image(0,0,image=image)

l.grid(row=0,column=1)
c.grid(row=0,column=2)

frame1 = t.Frame(top,relief='groove')       ; frame1.grid(row=0,column=0)
frame2 = t.Frame(frame1)                    ; frame2.pack(side = t.TOP)

#
# icon from Gemicon Icon Set (600+ free icons) (http://gemicon.net)
#
l1 = t.Label(frame2,text='Files in Current Directory')       ; l1.pack(side = 'top') ; png = ImageTk.PhotoImage(Image.open('folder3.png')) ;
ll1 = t.Listbox(frame2)     ;  ll1.pack(side = t.BOTTOM)
b1 = t.Button(frame2,image =  png, cursor = 'hand2',relief = 'groove')     ; b1.pack(side='top')

CurrentFiles = t.Listbox()
top.geometry('800x800+{}+{}'.format(1920/2,1080/2))
top.mainloop()