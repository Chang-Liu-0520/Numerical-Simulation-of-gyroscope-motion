import wx
from visual import window
from math import pi

class Control: # a class that control the object
    def __init__(self,obj):
        self.object = obj
        L = 400.
        w = window(width=2*window.dwidth+L, height=L+window.dheight+window.menuheight,
                   menus=True, title='Control') # create the window
        p = w.panel
        self.s1 = wx.Slider(p,pos=(0.25*L,0.25*L),size = (200,60))
        # create the slider that control the nutation angle
        self.s1.SetMin(1)
        self.s1.SetMax(50*pi)
        self.s1.SetValue(30*pi)
        wx.StaticText(p,pos=(0.25*L,0.15*L),label = 'set nutation angle',size = (200,25),
                      style = wx.ALIGN_CENTER)
        self.s1.Bind(wx.EVT_SCROLL, self.SetNutation)
        
        self.s2 = wx.Slider(p,pos=(0.25*L,0.55*L),size= (200,60))
        # create the slider that contro the velocity of rotation
        self.s2.SetMin(0)
        self.s2.SetMax(100)
        self.s2.SetValue(30)
        wx.StaticText(p,pos=(0.25*L,0.45*L),label = 'set rotation velocity',size = (200,25),
                      style = wx.ALIGN_CENTER)
        self.s2.Bind(wx.EVT_SCROLL, self.SetRotationVel)
        
        text1 = wx.StaticText(p,pos=(0.25*L,0.75*L),label = 'the total energy is:',size = (200,25),
                             style = wx.ALIGN_CENTER)
        self.text2 = wx.TextCtrl(p,pos = (0.25*L,0.8*L),size = (200,25))   
        self.text2.SetValue('0') # create the text to show the total energy
    
    def SetNutation(self,evt): 
        # a method to use the method SetNutation of the object to set the nutation angle
        nutation = self.s1.GetValue()/100.
        self.object.SetNutation(nutation)
    
    def SetRotationVel(self,evt):
        # a method to use the method SetRotationVel of the object to set the rotation velocity
        rotation = self.s2.GetValue()
        self.object.SetRotationVel(rotation)
    
    def ShowEnergy(self):
        # show the total energy in text2
        energy = round(self.object.GetPower())
        energy_str = str(energy)
        self.text2.SetValue(energy_str) 