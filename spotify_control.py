import pyautogui
import time
import os
import sys
import psutil
import time

for proc in psutil.process_iter():
    if proc.name() == "Spotify.exe":
        pyautogui.press('playpause')
        time.sleep(1)
        sys.exit(1)
    
pyautogui.press('win') 
time.sleep(1)
pyautogui.write('Spotify') 
time.sleep(1)
pyautogui.press('enter') 

time.sleep(5) 
pyautogui.press('space')  