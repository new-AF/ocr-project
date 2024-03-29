import os
import Tkinter as t
import ttk
import tkFileDialog
from PIL import ImageTk,Image
import numpy as np
import cv2

top = t.Tk()
top.title("ocr toolbox")

def imread(x, mode=cv2.IMREAD_UNCHANGED):
    """
    Like cv2.imread(...) but returns RGB numpy.ndarray instead of BGR

    x: (str) path to image
    mode: (int) modes to be passed to cv2.imread(s,...) 'consts' from cv2.xxx

    returns: result of cv2.imread(x,mode)
    """
    i = cv2.imread(x,mode)

    try:
        i = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
    except Exception as e:
        print ('[Exception in imread({},{})] ({})'.format(x,mode,e))

    return i

class Checkbutton(t.Button):
    def __init__(self,parent,**kw):
        temp = kw.pop('state1',True)

        t.Button.__init__(self,parent,padx = 10,command = self.Released,**kw)

        self.set( temp)
        #self.bind('<ButtonRelease>',self.Released)

    def Released (self,e = None):
        self.toggle()

    def set(self,value):
        if value:
            self.on()
        else:
            self.off()

    def toggle(self,new_state = None):
        if new_state is not None:
            self.set(new_state)
        else:
            pass
            self.set(not self.Xstate)


    def on(self):
        self['text'] = 'Enabled'
        self['relief'] = 'sunken'
        self.Xstate = True

    def off(self):
        self['text'] = 'Press to enable'
        self['relief'] = 'raised'
        self.Xstate = False

class Control:

    Images = []
    Photos = []
    Counter = 0

    def __init__(self):
        self.all = [[]]

        self.counter = self.Counter
        self.updateCounter()

    @classmethod
    def updateCounter(cls):
        cls.Counter += 1

    @classmethod
    def updateImageS(class_,pos,I):
        cls = class_
        cls.Images[pos:pos+1] = [I]
        cls.Photos[pos:pos+1]= [ImageTk.PhotoImage(Image.fromarray(cls.Images[pos]))]
        print (len(cls.Images))
        setItext(cls.Photos[-1])

    def updateImage(self,I):
        self.updateImageS(self.counter,I)

    def ownImage(self):
        return self.Images[self.counter]


    def lastImage(self):
        #print self.Images
        return self.Images[self.counter-1]

    def add_to_group(self,index,item,**kw):

        bind = kw.pop('bind',None)
        bind2 = kw.pop('bind2',None) # bind already existing items

        self.all[index:index+1] = [item]

        for k in item:
            k.control_parent = self

        if item and bind:
            self.bind2(bind[0],bind[1],  xrange(len(self.all[index])) )

    def bind2(self,event_type,function,*i):

        for j in i:
            rtype = type(j)
            if  rtype == int:
                for i2 in self.all[j]:
                    i2.bind(event_type,function)
            elif rtype == str:
                vars(self)[j].bind(event_type,function)

    def __getitem__(self,y):

        if type(y) != tuple:
            y = (y,)

        if type(y[0]) == int:

            a = []

            if len(y) == 2:

                return self.all[y[0]][y[1]]

            else:
                for j in y:
                    if j is None:
                        continue

                    a += self.all[j]

            return a

        elif type(y[0]) == str:
            a = []
            v= vars(self)

            for j in y:
                a+= [v[j]]

            return a
##        if type(i[0]) == int:
##            target = map(lambda x: self.all[x], i)
##        else:
##            target = vars(self) ; target.remove('all')
##
##            target = filter(lambda x: x in i, target)
##
##            map( lambda x: getattr(self,x).bind(event_type,function))

    def __repr__(self):

        s=['Control']
        l = 0
        for j,i in vars(self).iteritems():

            L = '\t' + str(i).replace('[','[\n\t\t').replace(', [','\n\t\t, [').replace(']',']\n')

            s+= [j,L]
        s+=['end']

        return '\n'.join(s)

class FunctionPane(t.Frame):

    def __init__(self,parent,**kw):

        #self.Parent = kw.pop('parent')

        self.name = kw.pop('name','Generic Tab')

        self.tab= ttk.Notebook(parent,**kw)

        t.Frame.__init__(self,self.tab)

        #self['master'] = self.tab

        #self['text']= self.name

        #self.frame = t.Frame(self)

        self.disable = Checkbutton(self,text='Enabled')

        self.reload = ttk.Button(self,text= 'Reset')

        self.control = Control()

        self.put(0,(0,0,self.disable),(0,1,self.reload))

        self.position()

    def put(self,index,*item):

        Widgets = [ j[2] for j in item]
        #print Widgets
        self.control.add_to_group(index,Widgets, bind = None)

        for j in item:
            y,x,j = j
            j.grid(row = y, column = x,sticky = 'ws' )

        #print self.control
    def position(self):

        self.tab.pack(side='bottom',fill='both',expand = 1)

        self.tab.add(self,text = self.name)


        #self.f.bind('<Visibility>',globals()['_'+name])
        #self.reload.bind('<ButtonRelease>',globals()['_'+name])


class Pane:
    def __init__(self,parent,name):
        self.tab = ttk.Notebook(parent)
        #self.code = t.Frame(self.tab)
        self.f = t.Frame(parent)
        self.disable = Checkbutton(self.f,text= 'Enabled')
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

'''
class Run:
    def __init__(self,*i):
        self.i = i
'''

# ---
Container3 = t.Frame(top)
Container3.pack(side=t.LEFT,fill='both',expand=0, padx = 20)

pane1 = FunctionPane(parent = Container3,name='imread /Read an Image')
def xread(e):
    x = e.widget.control_parent
    i = imread(Itext.Ipath)
    x.updateImage(i)
pane1.control[0][1].bind('<ButtonRelease>',xread)

pane2 = FunctionPane(parent = Container3,name='Noise Removal')

pane2.control.var1 = t.IntVar()
pane2.put(1,(1,0,t.Radiobutton(pane2,text='Mean Filter',variable=pane2.control.var1,value=0)),
(2,0,t.Radiobutton(pane2,text='Gaussian Filter',variable=pane2.control.var1,value=1)),
(3,0,t.Radiobutton(pane2,text='Median Filter',variable=pane2.control.var1,value=2))      )

pane2.control.var2 = [t.IntVar(),t.IntVar(),t.IntVar()]
pane2.put(2,(1,1,t.Scale(pane2,resolution=3,showvalue=1,orient=t.HORIZONTAL,from_=1,to=15,variable=pane2.control.var2[0])),
(2,1,t.Scale(pane2,showvalue=1,resolution=3,orient=t.HORIZONTAL,from_=1,to=15,variable=pane2.control.var2[1])),
(3,1,t.Scale(pane2,showvalue=1,resolution=3,orient=t.HORIZONTAL,from_=1,to=15,variable=pane2.control.var2[2]))
)


def xnoise0(w,v1,v2):

    s = v2
    if s == 0 :
        s = 1
    i = w.lastImage()
    i2 = cv2.blur(i,(s,s))
    w.updateImage(i2)

def xnoise1(w,v1,v2):

    s = v2
    if s == 0 :
        s = 1
    i = w.lastImage()
    i2 = cv2.GaussianBlur(i,(s,s),0)
    w.updateImage(i2)

def xnoise2(w,v1,v2):

    s = v2
    if s == 0 :
        s = 1
    i = w.lastImage()
    i2 = cv2.medianBlur(i,s)
    w.updateImage(i2)
##    l2 = lambda x,s : cv2.GaussianBlur(x,(s,s),0)
##    l3 = lambda x,s : cv2.medianBlur(x,s)

def xnoise_router(e,after=[0]):
    after[0] = not after[0]
    if (after[0]):
        top.after(10,xnoise_router,e)
        return
    w = e.widget.control_parent
    v1 = w.var1.get()
    v2 = map(lambda x: x.get(), w.var2)
    #print v1,v2
    globals()['xnoise%d'%(v1)](w,v1,v2[v1])

pane2.control.bind2('<ButtonRelease>',xnoise_router,1)
pane2.control.bind2('<B1-Motion>',xnoise_router,2)

###grayscaling

def xgray0(w,v):
    i = w.lastImage()

    v= int(v)
    i2 = i[:,:,v]

    w.updateImage(i2)

    w.var3.set(['Red','Green','Blue'][v])

def xgray1(w,v):

    i = w.lastImage()
    i2 = cv2.cvtColor(i, cv2.COLOR_RGB2GRAY)

    w.updateImage(i2)

def xgray_router(e,after=[0]):
    after[0] = not after[0]
    if (after[0]):
        top.after(10,xgray_router,e)
        return

    w = e.widget.control_parent
    v1 = w.var1.get()
    v2 = w.var2[v1].get()

    globals()['xgray%d'%(v1)](w,v2)


pane2_2 = FunctionPane(parent = Container3,name='Grayscaling')
pane2_2.control.var1 = t.IntVar()
pane2_2.control.var2 = [t.IntVar(),t.StringVar(value='None')]
pane2_2.control.var3 = t.StringVar(value='Red')
pane2_2.put(1,(1,0,t.Radiobutton(pane2_2,text = 'Extract the Channel',variable = pane2_2.control.var1, value= 0 )),
(3,0,t.Radiobutton(pane2_2,text = 'cv2.cvtColor',variable = pane2_2.control.var1, value = 1)))

pane2_2.put(2,(1,1,t.Label(pane2_2,textvariable = pane2_2.control.var3)),
(2,1,t.Scale(pane2_2,showvalue=0,resolution=1,orient=t.HORIZONTAL,from_=0,to=2,variable=pane2_2.control.var2[0] ))
)

pane2_2.control.bind2('<ButtonRelease>',xgray_router,1)
pane2_2.control.bind2('<B1-Motion>',xgray_router,2)

### thresholding

pane3 = FunctionPane(parent = Container3,name='Binary Threshold-ing')

pane3.control.var1 = t.IntVar()
pane3.control.var2 = [t.IntVar(),t.StringVar(value='None'),t.IntVar()]

pane3.put(1,(1,0,t.Label(pane3,text='Global')),
(7,0,t.Label(pane3,text='Local',)))

pane3.put(2,(2,0,t.Radiobutton(pane3,text='Set Value Manually',variable = pane3.control.var1 , value = 0)),
(3,0,t.Radiobutton(pane3,text="Apply Otsu's algorithm",variable = pane3.control.var1 , value=1)),
(8,0,t.Radiobutton(pane3,text='Adaptive threshloding',variable = pane3.control.var1 , value=2)) )

pane3.put(3,(2,1,t.Scale(pane3,variable=pane3.control.var2[0],showvalue=1,orient=t.HORIZONTAL,from_=0,to=255)),
(8,1,t.Scale(pane3,variable = pane3.control.var2[2],showvalue=1,orient=t.HORIZONTAL,resolution=3,from_=0,to=255)))

def xthresh0(w,v):
    i = w.lastImage()

    ret, i2 = cv2.threshold(i,v,255,cv2.THRESH_BINARY)
    w.updateImage(i2)

def xthresh1(w,v):
    i = w.lastImage()

    ret,i2 = cv2.threshold(i,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #print ("--->",i2)
    w.updateImage(i2)

def xthresh2(w,v):
    i = w.lastImage()

    print ('adaptive v',v)

    # ot avoid error: (-215:Assertion failed) blockSize % 2 == 1 && blockSize > 1 in function 'cv::adaptiveThreshold'
    if v > 1 and v%2 == 1:
        i2 = cv2.adaptiveThreshold(i,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,v,0)
        w.updateImage(i2)

def xthresh_router(e,after = [0]):
    after[0] = not after[0]
    if (after[0]):
        top.after(10,xthresh_router,e)
        return

    w = e.widget.control_parent
    v = w.var1.get()
    v2 = w.var2[v].get()
    if type(v2) == int:
        v2 = int(v2)
    globals()['xthresh%d'%v](w,v2)



pane3.control.bind2('<ButtonRelease>',xthresh_router,2)
pane3.control.bind2('<B1-Motion>',xthresh_router,3)


### end-thresholding

#pane3.control[2]
# ---


def move_(e):
    w = e.widget
    ImageFrame.place(x=e.x,y=e.y)

def make_frame(parent,label,font_size_increment = 0,font_name = 'tahoma'):
    fs = 10
    fs += font_size_increment
    l = t.Label(text = label, font = '{} {} bold'.format(font_name,fs))#, cursor = 'fleur')
    f = t.LabelFrame(parent,borderwidth=7, relief = 'groove',highlightthickness=7)
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

    dirs = filter(os.path.isdir,x)
    f = filter(os.path.isfile, x)

    x = filter(lambda l:l.rpartition('.')[2] in ['png','tif','tiff','jpg','jpeg','jpe','jp2','bmp','dib'],x)
    return x,dirs

def populate_list(x = False):
    if not x:
        x = os.getcwd()
    list1.Xpath = x

    y,dirs = get_image_names(x)

    list1.delete(0,t.END)


    c = len(dirs)
    for j,i in enumerate(dirs):
        pass

    for j,i in enumerate(y):
        list1.insert(j,i)

    #for j,i in enumerate(y):

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
    Itext.a[0] = imread(path)
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

##U+2589

def switch_page(e):
    pass
    # to be implemented later

#top.tk_bisque()

## Variables
Container1 = t.Frame(top)

image = tk_image('test1.jpg')
ImageFrame = make_frame(Container1,'Image')
ImageText = t.Text(ImageFrame)

CurrentFrame = make_frame(top,'Images in Current Path',-2)

ScrollFrame = t.Frame(CurrentFrame,relief='groove')
VirtualImage = ImageText.image_create(t.END, image=image)

ImshowFrame = make_frame(Container1,'Pipeline')
ImshowFrame.tab = ttk.Notebook(ImshowFrame)
ImshowText = t.Text(ImshowFrame.tab)

ImageTextScroll1 = t.Scrollbar(ImageFrame)
ImageTextScroll2 = t.Scrollbar(ImageFrame,orient=t.HORIZONTAL)


Itext = t.Text(ImshowFrame.tab)
ImshowFrame.tab.add(Itext,text='Processed Image')
Itext.a = []
Itext.b = []

Itext.Ipath = os.getcwd()+os.sep+'test1.jpg'
Itext.I = imread(Itext.Ipath)
Itext.M = Itext.I


def setItext(x):
    j = x
    try:
        Itext.delete(Itext.Itag)
    except:
        pass
    Itext.Itag=Itext.image_create(t.END,image = j)

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


populate_list()
list1.bind('<<ListboxSelect>>',list_select)
list1.bind('<Motion>',list_hover)
list1.bind('<Leave>',list_leave)
#print top.place_slaves()
#S(ImshowText).grid(row=0,column=1,second=1).grid(row=1,column=1)

top.geometry('800x800+{}+{}'.format(1920/2,1080/2))

topmenu = t.Menu(top)
smenu = t.Menu(topmenu)
smenu.add_checkbutton()
topmenu.add_cascade(label = 'Setting',menu = smenu)

top.mainloop()
