import pyautogui
import time

# distance = 200
# while distance > 0:
#         pyautogui.drag(distance, 0, duration=0.5)   # move right
#         print("moving right!")
#         distance -= 5
#         pyautogui.drag(0, distance, duration=0.5)   # move down
#         print("moving down!")
#         pyautogui.drag(-distance, 0, duration=0.5)  # move left
#         print("moving left!")
#         distance -= 5
#         pyautogui.drag(0, -distance, duration=0.5)  # move up
#         print("moving up!")

time.sleep(5)

f = open("test", 'r')

for word in f:
    pyautogui.typewrite(word)

    pyautogui.press("enter")
