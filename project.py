import os
import Tkinter as t
import ttk
import tkFileDialog
from PIL import ImageTk,Image
import numpy as np
import cv2

top = t.Tk()
top.title("ocr toolbox")



def _imread(e):
    x = Itext.I = cv2.imread(Itext.Ipath,cv2.IMREAD_UNCHANGED)
    mod(0,x)
    display(0)

def _Channel_Extraction(e):
    pass

def _Noise_Removal(e):
    pass

def _Canny_Edge_Detection(e):
    x = get(2)
    y = cv2.Canny(x,50,100)
    #y = cv2.Laplacian(x,cv2.CV_8U)
    #ret, y2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    mod(3, y )
    display(3)
def _X1(e):
    x = get(3)
    se = np.ones((2,2),np.uint8)
    seflood = np.zeroes((0,0),np.uint8)
    se = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]], dtype=np.uint8)
    y = cv2.morphologyEx(x, cv2.MORPH_CLOSE, se)
    #y = cv2.floodFill(x,seflood,(0,0),255)
    mod(4, y)
    display(4)
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
    global image,VirtualImage,Ipath
    w = e.widget
    #print dir(e)
    i = w.curselection()[0]

    text = w.get(i) #; print (text)
    path = os.path.join(list1.Xpath,text)

    Itext.Ipath = path
    Itext.a[0] = cv2.imread(path)
    display(0)

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

def switch_page(e):
    pass
    # to be implemented later

#detour = lambda i: visible(top)
#top.bind('<Visibility>',detour)

#top.tk_bisque()

## Variables
Container1 = t.Frame(top)
Container2 = t.Frame(top)
image = tk_image('test1.jpg')
ImageFrame = make_frame(Container1,'Image')
ImageText = t.Text(ImageFrame)
CurrentFrame = make_frame(top,'Images in Current Path',-2)
ScrollFrame = t.Frame(CurrentFrame,relief='groove')
VirtualImage = ImageText.image_create(t.END, image=image)

Canvas = t.Canvas(top,highlightthickness=7)
ImshowFrame = make_frame(Container1,'Pipeline')
ImshowFrame.tab = ttk.Notebook(ImshowFrame)
ImshowText = t.Text(ImshowFrame.tab)



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

class Reel:
    def __init__(self,parent,image,length = 1):
        self.image = image
        self.f = t.Frame(parent)
        self.buttons = []
        for i in xrange(length):
            b = t.Label(self.f,relief='groove',image =self.image )
            b.XPageIndex = i
            self.buttons += [b]
            b.grid(row=0,column=i,sticky='WE')
            b.bind('<Motion>',switch_page)

image2 = tk_image('3.png',11,11)
Container2.XIndex = []
class Pane:
    def __init__(self,parent,name):
        self.tab = ttk.Notebook(parent)
        #self.code = t.Frame(self.tab)
        self.f = t.Frame(parent)
        self.disable = ttk.Button(self.f,text= 'Disable')
        self.reload = ttk.Button(self.f,text= 'Reload')
        #self.l = t.Label(self.f,text = name, font = 'tahoma 11')
        #self.l.grid(row = 0,column =0 , sticky='W')
        parent.XIndex += [self.f]
        self.tab.pack(side='top',fill='both',expand = 1)
        self.reload.grid(row = 0,column=0,sticky = 'E')
        self.disable.grid(row = 0,column=1,sticky = 'E')
        self.tab.add(self.f,text=name)
        self.f.bind('<Visibility>',globals()['_'+name])
        self.reload.bind('<ButtonRelease>',globals()['_'+name])
        #self.tab.add(self.code,text='Code')

Dict = ['imread','Noise_Removal','Channel_Extraction','Canny_Edge_Detection','X1']
DictValues=[]



Itext = t.Text(ImshowFrame.tab)
ImshowFrame.tab.add(Itext,text='Processed Image')
Itext.a = []
Itext.b = []

Itext.Ipath = os.getcwd()+os.sep+'test1.jpg'
Itext.I = cv2.imread(Itext.Ipath)
Itext.M = Itext.I
#print '->>>',Itext.I

for i in Dict:
    j=Pane(Container2,i)
    DictValues += [j]
    Itext.a += [Itext.I]
    Itext.b += [Itext.I]

def get(pos):
    return Itext.a[pos]

def getb(pos):
    return Itext.b[pos]

def mod(pos,x=None,disabled = 0):
    if disabled:
        Itext.a[pos] = Itext.b[pos]
    if x is not None:
        Itext.a[pos] = x
    #for i in range(pos):
    #    display(i)

def display(pos = -1):
    try:
        Itext.Im = ImageTk.PhotoImage(Image.fromarray(Itext.a[pos]))
        Itext.delete(Itext.Itag)
    except:
        pass
    #print Itext.I
    Itext.Itag = Itext.image_create(t.END,image = Itext.Im)

def scale1_fun(v):
    v = int(v)
    L ={0:'Blue',1:'Green',2:'Red'}
    label1['text']= L[v]
    prev = get(1)
    mod(2,prev[:,:,v])
    display(2)


def spin_fun(v = False, v3=1,v2 = [1]):
    if v is False:
        v = int(radio1_var.get())

    if v3%2==0:
        v3+=1

    v2[0] = v3
    #print '->>>',v,v2

    l1 = lambda x,s : cv2.blur(x,(s,s))
    l2 = lambda x,s : cv2.GaussianBlur(x,(s,s),0)
    l3 = lambda x,s : cv2.medianBlur(x,s)
    x = [l1,l2,l3][v]
    x = x(get(0),v2[0])
    #print x
    mod(1,x)
    display(1)

def spin_fun2(v):
    spin_fun(radio1_var.get(),int(v))

label1 = t.Label(DictValues[2].f,text=0)
scale1 = t.Scale(DictValues[2].f, from_ = 0, to=2,command=scale1_fun, orient=t.HORIZONTAL,showvalue=0)
label1.grid(row=1,column=0,columnspan = 2)
scale1.grid(row=2,column=0,columnspan = 2)

radio1_var = t.IntVar()
radio11 = t.Radiobutton(DictValues[1].f,text = 'Average',variable=radio1_var,value=0,command = spin_fun)
radio12 = t.Radiobutton(DictValues[1].f,text = 'Gaussian',variable=radio1_var,value=1,command = spin_fun)
radio13 = t.Radiobutton(DictValues[1].f,text = 'Median',variable=radio1_var,value=2,command = spin_fun)
spin11 = t.Scale(DictValues[1].f,from_=1,to = 10,font = 'tahoma 9',orient=t.HORIZONTAL,command = spin_fun2)
spin12 = t.Scale(DictValues[1].f,from_=1,to = 10,font = 'tahoma 9',orient=t.HORIZONTAL,command = spin_fun2)
spin13 = t.Scale(DictValues[1].f,from_=1,to = 10,font = 'tahoma 9',orient=t.HORIZONTAL,command = spin_fun2)
radio11.grid(row=1,column=0,columnspan = 1,sticky=t.W)
radio12.grid(row=2,column=0,columnspan = 1,sticky=t.W)
radio13.grid(row=3,column=0,columnspan = 1,sticky=t.W)
spin11.grid(row=1,column=1,columnspan = 1,sticky=t.W)
spin12.grid(row=2,column=1,columnspan = 1,sticky=t.W)
spin13.grid(row=3,column=1,columnspan = 1,sticky=t.W)
#print Container2.XIndex

#Canvas.Gridder = gridder(dx = 100,dy=100)
#im(Canvas,'imread',y=1)
#im(Canvas,'im2bw',y=2)
#im(Canvas,'channel extraction',x=1,y=2)

# Configs1

Container2.pack(side=t.LEFT,fill='both',expand=1)
Container1.pack(side=t.LEFT,fill='both',expand=1)
ImageText.place(x=0,y=0, relwidth=.90,relheight=.95)
CurrentFrame.pack(side=t.LEFT,fill=t.X)
ImageText.config(yscrollcommand = ImageTextScroll1.set,xscrollcommand = ImageTextScroll2.set)
ImageText['bg']=top['bg']
ImageFrame.place(x=0,y=0,relheight=0.5,relwidth=1)

#Canvas.pack(side=t.LEFT,fill='both',expand=1)
ImshowFrame.tab.place(x=0,y=0, relwidth=.95,relheight=.95)
ImshowFrame.place(x=0,rely=0.5,relheight=0.5,relwidth=1)

## Configs2
ImageTextScroll1.config(command= ImageText.yview)
ImageTextScroll2.config(command= ImageText.xview)
ImageTextScroll1.place(relx=.91,y=0,relheight = .95)
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