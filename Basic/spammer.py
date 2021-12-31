import pyautogui as auto
from time import sleep
import keyboard
while True:
    auto.write("Metin Girin")
    auto.press("enter")
    sleep(0.5)
    if keyboard.is_pressed("l"): #Burası eğer "l" tuşuna basılırsa Programı Kapatır
        run = False
        
