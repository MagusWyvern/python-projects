import pyautogui

pyautogui.FAILSAFE = True
pyautogui.click(x=1571, y=697, clicks=1, button='left')

def pressKey(key):
    pyautogui.keyDown(str(key))
    pyautogui.keyUp(str(key))


def main():
    pressKey('z')

    pressKey('down')

    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')

    pressKey('x')
    pressKey('down')

    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')
    pressKey('z')

    pressKey('up')

while True:
	main()

