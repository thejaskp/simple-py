import pyautogui as pag
import time

message = input("What is the message")
msg_count = int(input("how many times you need to send the message"))
time.sleep(4)
count = 0

while count < msg_count:
    pag.typewrite(message)
    pag.press("enter")
    count = count + 1