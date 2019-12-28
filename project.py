import os
import Tkinter as t
import tkFileDialog
from PIL import ImageTk,Image

top = t.Tk()
top.title("ocr toolbox")

def get_dir():
    f = tkFileDialog.askdirectory(title = 'Choose the Path or Folder where Images Reside')
    print (f)

def get_image_names(x):
    x = os.listdir(x)
    x = filter(lambda l:l.rpartition('.')[2] in ['png','tif','tiff','jpg','jpeg','gif'],x)
    return x

def populate_list(x):
    y = get_image_names(x)
    for j,i in enumerate(y):
        list1.insert(j+1,i)

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
l1 = t.Label(frame2,text='Files in Current Directory')       ; l1.pack(side = t.LEFT) ; png = ImageTk.PhotoImage(Image.open('folder3.png')) ;
list1 = t.Listbox(frame1, selectmode = t.SINGLE, relief = 'groove',activestyle='none',selectbackground = 'yellow',selectforeground='black')     ;  list1.pack(side = t.BOTTOM, fill= t.X)
b1 = t.Button(frame2,image =  png, cursor = 'hand2',relief = 'groove', command = get_dir)     ; b1.pack(side=t.RIGHT) ; b1.config(padx = 11)

populate_list(os.getcwd())
top.geometry('800x800+{}+{}'.format(1920/2,1080/2))
top.mainloop()