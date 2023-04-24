import random
import pyautogui

screenWidth, screenHeight = pyautogui.size()

for i in range(10):
    x = random.random() * screenWidth
    y = random.random() * screenHeight
    pyautogui.moveTo(x, y, duration=0.25)
