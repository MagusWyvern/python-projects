import pyautogui
import time


time.sleep(5)
n=1000
while n!=0:
    pyautogui.press('w')     # press the F1 key
    time.sleep(1)
    n-=1
