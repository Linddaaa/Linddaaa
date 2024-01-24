# import turtle
# turtle.penup()
# turtle.backward(300)
# turtle.pendown()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.penup()
# turtle.forward(150)
# turtle.pendown()
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)

#SAISTĪTI FOR CIKLI
# import turtle
# turtle.penup()
# turtle.backward(300)
# turtle.pendown()
# for n in range (2):
#     turtle.penup()
#     turtle.forward(150)
#     turtle.pendown()
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)

#WHILE CIKLS 
# import turtle
# turtle.penup()
# turtle.backward(300)
# turtle.pendown()
# n = 0
# while n < 2:
#     turtle.penup()
#     turtle.forward(150)
#     turtle.pendown()
#     n += 1
#     i = 0
#     while i < 4:
#         turtle.forward(100)
#         turtle.right(90)
#         i += 1


# import turtle 
# turtle.showturtle()
# def my_function(x, y):
#     turtle.shape(x)
#     turtle.pencolor(y)
#     for x in range(10):
#         if x % 2==0:
#             turtle.forward(25)
#             turtle.right(45)
#         else:
#             turtle.forward(25)
#             turtle.right(45)

# my_function("triangle", "blue")


# import turtle 
# import random
# turtle.showturtle()
# def funkcija(figura, krasa):
#     turtle.shape(figura)
#     turtle.pencolor(krasa)
#     for x in range(100):
#         turtle.forward(10*x)
#         turtle.right(90)
# x = random.randint(-200, 200)
# y = random.randint(-200, 200)
# turtle.penup()
# turtle.goto(x,y)
# turtle.pendown()
# figura = ["circle", "turtle", "triangle", "classic", "arrow"]
# krasa = ["blue", "black", "red", "green"]
# funkcija(random.choice(figura),random.choice(krasa))



# import turtle 
# import random
# turtle.setpos(x,y)
# x = random.randint(-200;200)
# y = random.randint(-200;200)

# def square():
#     for x in range(4):
#         turtle.forward(50)
#         turtle.right(90) 

# def triangle():
#     for x in range(3):
#         turtle.forward(50)
#         turtle.right(120)


# import turtle 
# import random
# x = random.randrange(-200;200)
# y = random.randrange(-200;200)
# lielums = random.randrange(90)
# figura = random.randrange(1,4)




# import turtle 
# import random
# turtle.showturtle()
# def funkcija(figura, krasa):
#     turtle.shape(figura)
#     turtle.pencolor(krasa)
#     for x in range(4):
#        turtle.forward(100)
#        turtle.right(90)
# x = random.randint(-200, 200)
# y = random.randint(-200, 200)
# turtle.penup()
# turtle.goto(x,y)
# turtle.pendown()  
# figura = ["circle", "turtle", "triangle", "classic", "arrow"]
# krasa = ["blue", "black", "red", "green", "cyan", "pink"]
# funkcija(random.choice(figura),random.choice(krasa))


# import turtle
# k = turtle.Turtle()
# def square(x,y):
#    k.penup()
#    k.goto(x,y)
#    k.pendown()
#    for i in range(3):
#       k.color("red")
#       k.begin_fill()
#       k.forward(100)
#       k.left(120)
#       k.forward(100)
#       k.end_fill()
#    for i in range(4):
#       k.pencolor("black")
#       k.forward(100)
#       k.right(90)
#       k.forward(100)
#    for i in  range(4):
#       k.color("red", "blue")
#       k.begin_fill()
#       k.forward(50)
#       k.right(90)
#       k.forward(50)
#       k.end_fill()
   
# turtle.onscreenclick(square, 1)
# turtle.listen
# turtle.done()

# ZVAIGZNES
# import turtle
# import random
# k = turtle.Turtle()
# k.getscreen().bgcolor('black')
# def zvaigzne(x,y):
#    a = ["blue", "red", "green", "cyan", "pink", "purple", "yellow"]
#    k.penup()
#    k.goto(x,y)
#    k.pendown()
#    k.fillcolor(random.choice(a))
#    k.begin_fill()
#    for a in range(5):
#      k.forward(100) 
#      k.right(144)
#    k.end_fill()
# turtle.onscreenclick(zvaigzne, 1)
# turtle.listen
# turtle.done()


#18.01.24

# import turtle

# window = turtle.Screen()
# window.bgcolor('dark salmon')
# window.tracer(0)

# player = turtle.Turtle()
# player.shape('turtle')
# player.color('turquoise')
# player.penup()

# def turn_left():
#   player.color('light green')
#   player.left(10)
  
# def turn_right():
#   player.color('light blue')
#   player.right(10)
  
# window.onkeypress(turn_left, "Left")
# window.onkeypress(turn_right, "Right")
# window.listen() 

# while True:
#   player.forward(0.5)
#   window.update()




# import turtle
# import time 
# window = turtle.Screen()
# window.bgcolor('dark blue')
# window.title("Welcome to my game!")

# border = turtle.Turtle()
# border.color("Yellow")
# border.penup()
# border.setposition(-250,250)
# border.pendown()
# border.pensize(3)
# for i in range(4):
#   border.forward(500)
#   border.right(90)
# border.hideturtle()

# player = turtle.Turtle()
# player.shape('turtle')
# player.color('turquoise')
# player.penup()

# def turn_left():
#   player.color('pink')
#   player.left(10)

# def turn_right():
#   player.color('white')
#   player.right(10)

# window.onkeypress(turn_left, "Left")
# window.onkeypress(turn_right, "Right") 
# window.listen() 

# player2 = turtle.Turtle()
# player2.shape('arrow')
# player2.color('white')
# player2.penup()

# def turn_left():
#   player2.color('pink')
#   player2.left(10)

# def turn_right():
#   player2.color('green')
#   player2.right(10)

# window.onkeypress(turn_left,"z")
# window.onkeypress(turn_right,"c") 
# window.listen() 
  
# def moving_object(move):
#   move.fillcolor("red")
#   move.begin_fill()
#   move.circle(20)
#   move.end_fill()

# if __name__ == "__main__" : 
#   screen = turtle.Screen()
#   screen.setup(600,600)
#   screen.bgcolor("dark blue")
#   screen.tracer()
#   move = turtle.Turtle()
#   move.color("red")
#   move.speed(0)
#   move.width(2)
#   move.hideturtle()
#   move.penup()
#   move.goto(-250,0)
#   move.pendown()

# while True: 
#   move.clear()   
#   moving_object(move)    
#   screen.update()     
#   move.forward(5)
#   player.forward(1.5)
#   player2.forward(1.5)
#   window.update()






