from functools import partial

import wx
import random

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        self.panel = wx.Panel(self)
        self.coloredpan = wx.Panel(self.panel)
        self.coloredpan.SetSize(1, 110, 300, 100)
        self.currentR = random.randint(0, 255)
        self.currentG = random.randint(0, 255)
        self.currentB = random.randint(0, 255)
        self.coloredpan.SetBackgroundColour(wx.Colour( self.currentR,  self.currentG, self.currentB))
        self.panelCtrl = wx.Panel(self.panel)
        self.panel1 = wx.Panel(self.panel)
        self.buttonValues={}
        self.buttonValues["DARK"] =   [0,0,0,0]
        self.buttonValues["PURPLE"] = [0,0,0,1]
        self.buttonValues["BLUE"] =   [0,0,1,0]
        self.buttonValues["GREEN"] =  [0,0,1,1]
        self.buttonValues["YELLOW"] = [0,1,0,0]
        self.buttonValues["ORANGE"] = [0,1,0,1]
        self.buttonValues["RED"] =    [0,1,1,0]
        self.buttonValues["WHITE"] =  [0,1,1,1]
        self.buttonValues["GREY"] =   [1,0,0,0]
        self.UI()
        self.Centre()
    def UI(self):
        boxPanels= wx.BoxSizer(wx.VERTICAL)
        new_button = wx.Button(self.panelCtrl,wx.ID_ANY,"NEW COLOR")
        new_button.Bind(wx.EVT_BUTTON, self.generateNewColor)
        dark_button = wx.Button(self.panel1, 3,"DARK" )
        dark_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="DARK"))
        purple_button = wx.Button(self.panel1, 3, "PURPLE")
        purple_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="PURPLE"))
        blue_button = wx.Button(self.panel1,3,"BLUE")
        blue_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="BLUE"))
        green_button = wx.Button(self.panel1, 3, "GREEN")
        green_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="GREEN"))
        yellow_button = wx.Button(self.panel1, 3, "YELLOW")
        yellow_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="YELLOW"))
        orange_button = wx.Button(self.panel1, 3, "ORANGE")
        orange_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="ORANGE"))
        red_button = wx.Button(self.panel1, wx.ID_ANY, "RED")
        red_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="RED"))
        white_button = wx.Button(self.panel1, 3, "WHITE")
        white_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="WHITE"))
        grey_button = wx.Button(self.panel1, 3, "GREY")
        grey_button.Bind(wx.EVT_BUTTON, partial(self.choiceColor, button_label="GREY"))
        boxcolors = wx.BoxSizer(wx.HORIZONTAL)
        boxcolors.Add(dark_button, 0)

        boxcolors.Add(purple_button, 0)
        boxcolors.Add(blue_button, 0)
        boxcolors.Add(green_button, 0)
        boxcolors.Add(yellow_button, 0)
        boxcolors.Add(orange_button, 0)
        boxcolors.Add(red_button, 0)
        boxcolors.Add(white_button, 0)
        boxcolors.Add(grey_button, 0)
        self.panel1.SetSizer(boxcolors);

        boxPanels.Add(self.panelCtrl)
        boxPanels.Add(self.panel1)
        self.panel.SetSizer(boxPanels)
    def generateNewColor(self,e):
        print("CLICKED")
        self.currentR = random.randint(0,255)
        self.currentG = random.randint(0, 255)
        self.currentB = random.randint(0, 255)
        self.coloredpan.SetBackgroundColour(wx.Colour( self.currentR,  self.currentG, self.currentB))
        self.coloredpan.Refresh()
    def choiceColor(self, Event, button_label):

        print ("In OnButton:", button_label)
        print (self.buttonValues[button_label])
        self.generateNewColor(Event)

def main():

    app = wx.App()
    mf = MyFrame(None,"TRAINER NN COLOR RECOGNITION")
    mf.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()