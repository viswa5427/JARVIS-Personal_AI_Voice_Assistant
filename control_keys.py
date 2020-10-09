#MIT License

#Copyright (c) 2020 Viswanadh Kothakota

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import pyautogui
import time

class General_keys:
    def __init__(self):
        pass

    def SelectAll(self):
        pyautogui.hotkey('ctrl','a')

    def Cut(self):
        pyautogui.hotkey('ctrl','x')
        time.sleep(1)

    def Copy(self):
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)

    def Paste(self):
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        
    def History(self):
        pyautogui.hotkey('ctrl','h')

    def Download(self):
        pyautogui.hotkey('ctrl','j')

    def Undo(self):
        pyautogui.hotkey('ctrl','z')
    
    def Redo(self):
        pyautogui.hotkey('ctrl','y')
    
    def Save(self):
        pyautogui.hotkey('ctrl','s')
    
    def Enter(self):
        pyautogui.hotkey('enter')

    def Find(self):
        pyautogui.hotkey('ctrl','f')

class WindowOpt:
    def __init__(self):
        pass

    def openWindow(self):
        self.maximizeWindow()

    def closeWindow(self):
        pyautogui.hotkey('alt','F4')

    def minimizeWindow(self):
        pyautogui.hotkey('win','down')
        time.sleep(1)
        pyautogui.hotkey('win','down')

    def maximizeWindow(self):
        pyautogui.hotkey('win','up')

    def moveWindow(self, data):
        if "left" in data:
            pyautogui.hotkey('win','left')
        elif "right" in data:
            pyautogui.hotkey('win','right')
        elif "down" in data:
            pyautogui.hotkey('win','down')
        elif "up" in data:
            pyautogui.hotkey('win','up')
            
    def switchWindow(self):
        pyautogui.hotkey('alt','tab')

class TabOpt:
    def __init__(self):
        pass
    
    def switchTab(self):
        pyautogui.hotkey('ctrl','tab')

    def closeTab(self):
        pyautogui.hotkey('ctrl','w')

    def newTab(self):
        pyautogui.hotkey('ctrl','t')


    

def Ctrl_Keys(data):
    keys = General_keys()
    if "select all" in data:
        keys.SelectAll()
    if "cut" in data:
        keys.Cut()
    if "copy" in data:
        keys.Copy()
    if "paste" in data or "test" in data:
        keys.Paste()
    if "save" in data:
         keys.Save()
    if "enter" in data or 'search' in data:
        keys.Enter()
    elif "history" in data:
        keys.History()
    elif "download" in data:
        keys.Download()
    elif "undo" in data:
        keys.Undo()
    elif "Redo" in data:
        keys.Redo()
    elif "find" in data:
        keys.Find()
    return

def Win_Opt(data):
    w=WindowOpt()
    if "open" in data:
        w.openWindow()
    elif "close" in data:
        w.closeWindow()                 
    elif "mini" in data:
        w.minimizeWindow()
    elif "max" in data:
        w.maximizeWindow()
    elif "move" in data:
        w.moveWindow(data)
    elif "switch" in data:
        w.switchWindow()
    return

def Tab_Opt(data):
    t = TabOpt()
    if "new" in data:
        t.newTab()
    elif "switch" in data or "move" in data:
        t.switchTab()
    elif "close" in data or "delete" in data:
        t.closeTab()
    return
