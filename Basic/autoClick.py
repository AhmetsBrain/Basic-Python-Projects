import pyautogui as auto
import keyboard 
print("başladı")
while True:
    auto.click()
    if keyboard.is_pressed("space"):
        break
    print("bitti")