#! python3

import pyautogui
import sys
import time
import random

print('Press Ctrl-C to quit.')

def randomMouseMove():
    x = random.randint(0, 700)
    y = random.randint(0, 600)

    pyautogui.moveTo(x, y, 1, pyautogui.easeInOutQuad)

def rebirthCheck():
    rebirthNotif = pyautogui.locateOnScreen(
        'rebirth-notif.png', confidence=0.95)

    if rebirthNotif is not None:

        print("Rebirth notification found!")

        aa = rebirthNotif[0] + 10
        bb = rebirthNotif[1] + 10

        pyautogui.moveTo(aa, bb, 2, pyautogui.easeInOutQuad)

        pyautogui.click()

        randomMouseMove()

        time.sleep(2)

        randomMouseMove()

        rebirthButton = pyautogui.locateOnScreen(
            'rebirth-1.png', confidence=0.8, region=(0, 0, 700, 600))

        if rebirthButton is not None:
            a = rebirthButton[0] + 10
            b = rebirthButton[1] + 10
            pyautogui.moveTo(a, b, 2, pyautogui.easeInOutQuad)
            pyautogui.click()



def getClicks():
    blueClickButton = pyautogui.locateOnScreen(
        'click.png', confidence=0.8, region=(0, 0, 900, 900))

    if blueClickButton is not None:
        c = blueClickButton[0] + 30
        d = blueClickButton[1] - 30

        print('Game click button found')

        pyautogui.moveTo(c, d, 2, pyautogui.easeInOutQuad)

        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()


try:
    while True:
        randomMouseMove()

        rebirthCheck()

        randomMouseMove()

        time.sleep(1)

        randomMouseMove()

        getClicks()

        randomMouseMove()

        time.sleep(3)

        # Debugging
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=False)
except KeyboardInterrupt:
    print('\n')
