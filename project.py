import os
import Tkinter as t
import tkFileDialog
from PIL import ImageTk,Image
import cv2 as cv

top = t.Tk()
top.title("ocr toolbox")
def move_(e):
    w = e.widget
    ImageFrame.place(x=e.x,y=e.y)

def make_frame(parent,label,font_size_increment = 0):
    fs = 10
    fs += font_size_increment
    l = t.Label(text = label, font = 'tahoma %d bold'%fs, cursor = 'fleur')
    f = t.LabelFrame(parent,bd=7, relief = 'groove',highlightthickness=7)
    f.XLabel = l
    f.XLabel.bind('<B1-Motion>',move_)
    f.config (labelwidget = l)
    return f
def get_dir():
    f = tkFileDialog.askdirectory(title = 'Choose the Path or Folder where Images reside')
    print (f)
    populate_list(f)

def get_image_names(x):
    x = os.listdir(x)
    x = filter(lambda l:l.rpartition('.')[2] in ['png','tif','tiff','jpg','jpeg','gif'],x)
    return x

def populate_list(x = False):
    if not x:
        x = os.getcwd()
    list1.Xpath = x
    y = get_image_names(x)

    list1.delete(0,t.END)

    for j,i in enumerate(y):
        list1.insert(j+1,i)


def tk_image(fname,*rest ):
    p = Image.open(fname) # pillow_image

    if rest:
        p = p.resize(rest[0:2])

    i = ImageTk.PhotoImage(p)
    return i

def list_select(e):
    global image,VirtualImage
    w = e.widget
    #print dir(e)
    i = w.curselection()[0]

    text = w.get(i) #; print (text)
    path = os.path.join(list1.Xpath,text)
    #print (path)
    image = tk_image(path)
    ImageText.delete(VirtualImage)
    VirtualImage = ImageText.image_create(t.END,image = image)
    #l.configure(image = image)
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
    w.itemconfig(i,background = 'yellow') #gray80

def list_leave(e):
    w=e.widget
    w.itemconfig(w.Xhover_i,background = 'white')

def Box(parent,*i):
    t.Frame(parent)

##U+2589

def Appear(x,manager,**kw):
    fun = getattr(x,manager)

    fun(x,**kw)


#detour = lambda i: visible(top)
#top.bind('<Visibility>',detour)

#top.tk_bisque()

## Variables
Container1 = t.Frame(top)
image = tk_image('test1.jpg')
ImageFrame = make_frame(Container1,'Image')
ImageText = t.Text(ImageFrame)
CurrentFrame = make_frame(top,'Images in Current Path',-2)
ScrollFrame = t.Frame(CurrentFrame,relief='groove')
VirtualImage = ImageText.image_create(t.END, image=image)
Canvas = t.Canvas(top,highlightthickness=7)
ImshowFrame = make_frame(Container1,'"imshow"')
ImshowText = t.Text(ImshowFrame)



ImageTextScroll1 = t.Scrollbar(ImageFrame)
ImageTextScroll2 = t.Scrollbar(ImageFrame,orient=t.HORIZONTAL)

class gridder:
    def __init__(self,dx,dy,offset = 50):
        self.inc = offset
        self.dx=dx
        self.dy=dy
    def getx(self,x):
        return self.dx*x+self.inc
    def gety(self,y):
        return self.dy*y

class im:
    def __init__(self,canvas,text, x=0,y=0):
        self.c = canvas
        self.x = self.c.Gridder.getx(x)
        self.y = self.c.Gridder.gety(y)
        self.button(text)
    def button(self,text):
        self.b = t.Button(font = 'tahoma 10',text=text)
        self.c.create_window(self.x,self.y,window = self.b)

Canvas.Gridder = gridder(dx = 100,dy=100)
im(Canvas,'imread',y=1)
im(Canvas,'im2bw',y=2)
im(Canvas,'channel extraction',x=1,y=2)

# Configs1
CurrentFrame.pack(side=t.LEFT,fill=t.X)
Container1.pack(side=t.LEFT,fill='both',expand=1)
ImageText.place(x=0,y=0, relwidth=.95,relheight=.95)

ImageText.config(yscrollcommand = ImageTextScroll1.set,xscrollcommand = ImageTextScroll2.set)
ImageText['bg']=top['bg']
ImageFrame.place(x=0,y=0,relheight=0.5,relwidth=1)

Canvas.pack(side=t.LEFT,fill='both',expand=1)
ImshowText.pack()
ImshowFrame.place(x=0,rely=0.5,relheight=0.5,relwidth=1)

## Configs2
ImageTextScroll1.config(command= ImageText.yview)
ImageTextScroll2.config(command= ImageText.xview)
ImageTextScroll1.place(relx=.95,y=0,relheight = .95)
ImageTextScroll2.place(x=0,rely=0.95,relwidth=.95)

## Old Variables
list_scroll1 = t.Scrollbar(ScrollFrame,orient=t.VERTICAL)
list_scroll2 = t.Scrollbar(ScrollFrame,orient=t.HORIZONTAL)
list_scroll1.pack(side= t.RIGHT, fill = t.Y)
list_scroll2.pack(side= t.BOTTOM, fill = t.X)


#
# icon from Gemicon Icon Set (600+ free icons) (http://gemicon.net)
#
#l1 = t.Label(frame2,text='Files in Current Directory')       ; l1.pack(side = t.LEFT)
png = tk_image('folder3.png',20,20) ;
list1 = t.Listbox(ScrollFrame, yscrollcommand = list_scroll1.set,xscrollcommand = list_scroll2.set, exportselection=0, selectmode = t.SINGLE, relief = 'groove',activestyle='none',selectbackground = 'steelblue2',selectforeground='black', cursor = 'hand2' )
list1.pack(side = t.LEFT, fill= t.BOTH)



b1 = t.Button(CurrentFrame,image =  png, relief = 'groove', command = get_dir)
b1.pack(side=t.TOP,anchor= t.E, pady = 5)
ScrollFrame.pack(side = t.BOTTOM)
list_scroll1.config(command = list1.yview)
list_scroll2.config(command = list1.xview)
Canvas.focus()
populate_list()
list1.bind('<<ListboxSelect>>',list_select)
list1.bind('<Motion>',list_hover)
list1.bind('<Leave>',list_leave)
#print top.place_slaves()
top.geometry('800x800+{}+{}'.format(1920/2,1080/2))
top.mainloop()