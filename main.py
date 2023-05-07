import turtle
from random import randint

FONT = ('Courier', 30, 'normal')
turtle_screen=turtle.Screen()
turtle_screen.bgpic("Slider-CL01-Background.png")
turtle_screen.setup(800,600)
turtle_screen.title("Tospa'yı Yakala")

turtle.tracer(0)
turtle_image=turtle.Turtle()
turtle_image.penup()
turtle_image.shape('turtle')
turtle_image.shapesize(4)

score1=10
points = turtle.Turtle()
points.color("yellow")
style = ('Courier', 30, 'normal')
points.hideturtle()
points.penup()
points.goto(-200, 250)
points.write("Points: "+ str(score1), font=style)
def play_game(x,y):
        global score1
        score1 += 2
        points.clear()
        points.write("Points: " + str(score1), font=style)

turtle_image.onclick(fun=play_game,btn=1,add=True)


turtle_screen.listen()
def countdown(time):
    turtle_screen.onclick(None)  # disable click until countdown completes
    turtle.clear()

    if time > 0:
        turtle.write(time, align='center', font=FONT)
        turtle_screen.ontimer(lambda: countdown(time - 1), 1000)
        turtle_image.setpos(randint(-250, 250), randint(-250, 250))
        turtle_image.speed("fast")
        turtle_image.clear()

    else:
        turtle.write("Click Screen", align='center', font=FONT)
        turtle_screen.onclick(lambda x, y: countdown(30))

turtle_screen.onclick(lambda x, y: countdown(30))

turtle.tracer(1)

turtle.mainloop()