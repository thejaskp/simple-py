import pyautogui as pag
import time

time.sleep(4)
count = 0

while count < 200:
    pag.typewrite("hi")
    pag.press("enter")
    count = count + 1