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

def populate_list(x = None):
    if x == None:
        x = list1.Xpath
    y = get_image_names(x)

    for j,i in enumerate(y):
        list1.insert(j+1,i)


def tk_image(fname,*rest ):
    p = Image.open(fname) # pillow_image

    if rest:
        p = p.resize(rest[0:2])

    i = ImageTk.PhotoImage(p)
    return i

def list_select(e):
    global image
    w = e.widget
    #print dir(e)
    i = w.curselection()[0]

    text = w.get(i) #; print (text)
    path = os.path.join(list1.Xpath,text)
    #print (path)
    image = tk_image(path)
    l.configure(image = image)
    #print ()

def list_hover(e):
    #print (dir(e))
    w=e.widget

    s= w.curselection()[0:1]
    i=w.nearest(e.y)

    if s!= i:
        try:
            w.itemconfig(w.Xhover_i,background = 'white')
        except:
            pass
        w.Xhover_i = i
    #print ('hover',i)
    w.itemconfig(i,background = 'gray80')

def list_leave(e):
    w=e.widget
    w.itemconfig(w.Xhover_i,background = 'white')
##U+2589

#detour = lambda i: visible(top)
#top.bind('<Visibility>',detour)

#top.tk_bisque()
image = tk_image('test1.jpg')

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
l1 = t.Label(frame2,text='Files in Current Directory')       ; l1.pack(side = t.LEFT) ; png = tk_image('folder3.png',20,20) ;
list1 = t.Listbox(frame1,exportselection=0, selectmode = t.SINGLE, relief = 'groove',activestyle='none',selectbackground = 'steelblue2',selectforeground='black', cursor = 'hand2' )     ;  list1.pack(side = t.BOTTOM, fill= t.X)
b1 = t.Button(frame2,image =  png, relief = 'groove', command = get_dir)     ; b1.pack(side=t.RIGHT) ; b1.config(padx = 11)

list1.focus()
list1.Xpath = os.getcwd()
populate_list()
list1.bind('<<ListboxSelect>>',list_select)
list1.bind('<Motion>',list_hover)
list1.bind('<Leave>',list_leave)
top.geometry('800x800+{}+{}'.format(1920/2,1080/2))
top.mainloop()