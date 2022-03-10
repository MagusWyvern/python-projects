#! python3

import pyautogui
import sys
import time
import random

print('Press Ctrl-C to quit.')

def getClicks():
    blueClickButton = pyautogui.locateOnScreen(
        'coins.png', confidence=0.5, region=(0, 0, 900, 900))

    if blueClickButton is not None:
        c = blueClickButton[0] 
        d = blueClickButton[1] 

        print('Game click button found')

        pyautogui.click(c, d)
        pyautogui.click(c, d)


try:
    while True:

        time.sleep(1)

        getClicks()

        pyautogui.hold('w')

        time.sleep(3)

        # Debugging
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=False)
except KeyboardInterrupt:
    print('\n')
