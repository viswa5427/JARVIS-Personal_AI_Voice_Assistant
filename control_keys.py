import pyautogui
import time

class TabOpt:
    def __init__(self):
        pass
    
    def switchTab(self):
        pyautogui.hotkey('ctrl','tab')

    def closeTab(self):
        pyautogui.hotkey('ctrl','w')

    def newTab(self):
        pyautogui.hotkey('ctrl','t')

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

 