import pyautogui
import time

sleep = 20
pyautogui.FAILSAFE = False

while(True):
    currentX, currentY = pyautogui.position()
    pyautogui.moveTo(currentX+15, currentY)
    time.sleep(sleep)
    currentX, currentY = pyautogui.position()
    pyautogui.moveTo(currentX-15, currentY)
    time.sleep(sleep)


