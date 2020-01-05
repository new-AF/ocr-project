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

class S:
    def __init__(self,target):
        self.target = target
        self.scroll1 = t.Scrollbar(target)
        self.scroll2 = t.Scrollbar(target)

        self.config_self()
        self.config_target()

    def _position(self,_fun,**kw):
        _fun(self.scroll1,**kw)

    def pack(self,**kw):
        self._position(self.target.pack,**kw)
        if kw.pop('scroll2',False):
            return self.scroll2

    def place(self,**kw):
        self._position(self.target.place,**kw)
        if kw.pop('scroll2',False):
            return self.scroll2

    def grid(self,**kw):
        self._position(self.target.grid,**kw)
        if kw.pop('scroll2',False):
            return self.scroll2

    def config_self(self):
        self.scroll1.config(command= self.target.yview)
        self.scroll2.config(command= self.target.xview)

    def config_target(self):
        self.target['xscrollcommand']=self.scroll1.set
        self.target['yscrollcommand']=self.scroll2.set



def _imread(e):
    x = Itext.I = imread(Itext.Ipath)
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
    #print ('before thresh',x,type(x),x.shape)
    #ret, y = cv2.threshold(x,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    #
    #print 'Canny>>>',y
    mod(3, y )
    display(3)

def _X1(e):
    x = get(3)
    h,w = x.shape[:2]
    se1 = np.ones((2,2),np.uint8)
    seflood = np.zeros((h+2,w+2),np.uint8)

    se = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]], dtype=np.uint8)
    y = cv2.morphologyEx(x, cv2.MORPH_DILATE, se1)
    #y = cv2.floodFill(x,seflood,(0,0),255)
    #print '++++++++',type(y),y
    #yinv = cv2.bitwise_not(y[1])
    #yinv = ~y[1]
    #yy = x | yinv
    #print '++++++++',type(yinv),yinv,type(yinv)

    # ----
    # ----

    mod(4, y)
    #mod(4,y)
    display(4)
def move_(e):
    w = e.widget
    ImageFrame.place(x=e.x,y=e.y)

def make_frame(parent,label,font_size_increment = 0):
    fs = 10
    fs += font_size_increment
    l = t.Label(text = label, font = 'tahoma %d bold'%fs, cursor = 'fleur')
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

    def __init__(self,*i):
        self.all = [list(i)]

    def add_to_group(self,index,*item,**kw):

        bind = kw.pop('bind',None)
        bind2 = kw.pop('bind2',None) # bind already existing items

        self.all[index:index+1] = item

        if item and bind:
            self.bind(bind[0],bind[1],  xrange(len(self.all[index])) )

    def bind(self,event_type,function,*i):

        for j in i:
            rtype = type(j)
            if  rtype == int:
                self.all[j].bind(event_type,function)
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

        self.control = Control(self.disable,self.reload)

        self.position()

    def put(self,index,*item):

        Widgets = [ j[2] for j in item]

        self.control.add_to_group(index,Widgets, bind = None)

        for j in item:
            y,x,j = j
            j.grid(row = y, column = x,sticky = t.W+t.S )

        print self.control
    def position(self):

        self.tab.pack(side='left',fill='both',expand = 1)

        self.tab.add(self,text = self.name)

        self.reload.grid(row = 0,column=0,sticky = t.E)

        self.disable.grid(row = 0,column=1,sticky = t.E)


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
Dict = ['imread','Noise_Removal','Channel_Extraction','Canny_Edge_Detection','X1']
DictValues=[]



Itext = t.Text(ImshowFrame.tab)
ImshowFrame.tab.add(Itext,text='Processed Image')
Itext.a = []
Itext.b = []

Itext.Ipath = os.getcwd()+os.sep+'test1.jpg'
Itext.I = imread(Itext.Ipath)
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
    L ={0:'Red',1:'Green',2:'Blue'}
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

## --

te = FunctionPane(parent = top,name='( imread ) Read an Image')

te.put(1, (1,0,t.Button(te,text = 'Hi')),(1,1,t.Button(te,text = 'Hi2')) )
#tes2 = FunctionPane(parent = top)
#tes = t.Frame()


## --
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
#S(ImshowText).grid(row=0,column=1,second=1).grid(row=1,column=1)

top.geometry('800x800+{}+{}'.format(1920/2,1080/2))
top.mainloop()
