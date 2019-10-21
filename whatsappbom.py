//Header files
import pyautogui
import time

pyautogui.hotkey("alt","tab")
time.sleep(1)//this statement is used for wait 1 seconds
while True:
    pyautogui.typewrite("Hi bhaiya")
    pyautogui.press("enter")//button pressing event
