from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  1186 Y: 1016 RGB: ( 80,  82, 115)
#Tile 2 Position: X:  1042 Y: 1017 RGB: ( 77,  80, 115)
#Tile 3 Position: X:  877 Y: 1030 RGB: ( 77,  80, 115)
#Tile 4 Position: X:  750 Y: 1029 RGB: ( 79,  81, 115)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(1186, 400)[0] == 0:
        click(1186, 400)
    elif pyautogui.pixel(1042, 400)[0] == 0:
        click(1042, 400)
    elif pyautogui.pixel(877, 400)[0] == 0:
        click(877, 400)
    elif pyautogui.pixel(750, 400)[0] == 0:
        click(750, 400)
    
