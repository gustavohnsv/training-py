import pyautogui
import time
from time import sleep


time.sleep(5)
print("Executando")
var = 0
while var < 500:
    pyautogui.click(duration=.01)
    var = var + 1
    print(var)
