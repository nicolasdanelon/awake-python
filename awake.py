import pyautogui
import time
import datetime

sleep = 20
pyautogui.FAILSAFE = False

try:
  while(True):
    now = datetime.datetime.now()

    currentX, currentY = pyautogui.position()
    pyautogui.moveTo(currentX+1, currentY)
    time.sleep(sleep)
    print(f"{now.hour}:{now.minute}:{now.second}\n")

    currentX, currentY = pyautogui.position()
    pyautogui.moveTo(currentX-1, currentY)
    time.sleep(sleep)
    print(f"{now.hour}:{now.minute}:{now.second}\n")

except:
  print("\nSomething just happened, maybe the program has stopped")
