import turtle as t
pen = t.Turtle()
t.bgcolor('black')
t.delay(8)
pen.color('purple')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-170, 100)
    pen.color('cyan')
    pen.write('Kalbin İçine Yazılacak Metin.', font=("Comic Sans MS", 16))
txt()
pen.end_fill()
t.exitonclick()
"""
Aria
#A020F0
Comic Sans MS
#ffe4e1
"""

