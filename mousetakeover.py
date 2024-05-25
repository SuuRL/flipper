import os
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
import random
import time
while True:
    time.sleep(0.1)
    pyautogui.moveRel(random.randint(-250, 250), random.randint(-250, 250), duration=0.25)
