import time
import random
import pyautogui as pag

while True:
    x = random.randint(50, 1870)
    y = random.randint(50, 1030)
    pag.moveTo(x, y, 0.5)
    time.sleep(1.5)