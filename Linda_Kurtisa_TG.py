
import turtle
#pārdēvēju turtle par a
a = turtle.Turtle()
#izveidoju definētu funkciju
def kvadrats(x,y):
   a.penup()
   a.goto(x,y)
   a.pendown()
#kvadrāta formula
for i in range(4):
      a.forward(50)
      a.right(90)
      a.forward(50)
#izveidoju otru definētu funkciju
def square(x,y):
    a.penup()
    a.pendown()
#otra kvadrāta formula
for n in range(4):
    a.forward(80)
    a.right(90)
    a.forward(80)
turtle.done()



import turtle
import random
#pārdēvēju turtle sev izvēlētā vārdā - b
b = turtle.Turtle()
#izveidoju definētu funkciju
def circle(x,y):
    #krāsas no kurām izvēlēties katru reizi veidojot jaunu apli
    a = ["blue", "red", "green", "cyan", "pink", "purple", "yellow"]
    #rādiuss ir 10
    r = 10
    b.penup()
    b.goto(x,y)
    b.pendown()
    b.fillcolor(random.choice(a))
    b.begin_fill()
    b.circle(r) 
    b.end_fill()
#funkcijas, lai aplis parādītos uz ekrāna ar kreiso klikšķi
turtle.onscreenclick(circle, 1)
turtle.listen
turtle.done()
