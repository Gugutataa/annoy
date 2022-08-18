import pyautogui
import time
countdown = input("Enter countdown timer(seconds):")
countdown = float(countdown)
countdown = round(countdown)
countdown = int(countdown)
delay = input("Enter delay between WIN+D(seconds):")
delay = float(delay)
delay = round(delay)
delay = int(delay)
time1 = input("Enter prank time(seconds):")
time1 = float(time1)
time1 = round(time1)
time1= int(time1)
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1
mod = time1 % delay
time1 = time1 - mod
while time1 > 0:
    time.sleep(delay)
    time1 = time1 - delay
    pyautogui.hotkey("win", "d")
