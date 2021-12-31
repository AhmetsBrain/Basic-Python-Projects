import pygame as py
import keyboard

py.init()

size = (500, 300)

screen = py.display.set_mode(size)
run = True

while run:
    for ev in py.event.get():
        
        if ev.type == py.MOUSEBUTTONUP:
            
            pos = py.mouse.get_pos()
            
            col= (0, 255, 255)
            
            py.draw.circle(
                screen, col, pos, 20, 5
            )
        if keyboard.is_pressed("k"):
            run = False
    py.display.update()