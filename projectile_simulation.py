"""
This program simulates projectile motion with air resistance using user-defined parameters,
including mass, radius, initial velocity, and initial height.

The simulation is implemented using numerical methods (Euler method) to compute real-time motion.
It visualizes the projectile trajectory, as well as velocity–time (v–t) and acceleration–time (a–t) graphs
in both x and y directions using the Python Turtle graphics module.
"""

###python code

import turtle
import math

t = turtle.Turtle()
t1 = turtle.Turtle()
draw = turtle.Turtle()
txy = turtle.Turtle()
s = turtle.Screen()

turtle.tracer(False) #if True ->too slow
turtle.setup(700, 1400)

turtle.hideturtle()
t.speed(0)
t1.speed(0)
draw.speed(0)
txy.speed(0)
s.bgcolor("black")
t.color("white")

t.setheading(0)
t.penup()
t.goto(-690, -290)
t.pendown()
t.goto(-90, -290)
t.penup()
t.goto(-640, 260)
t.pendown()
t.goto(-640, -340)
t.penup()
t.goto(-85, -295)
t.write("x(m)")
t.goto(-645, 265)
t.write("y(m)")
for i in range(6):
    t.goto(-90-i, -290+i)
    t.dot(2, "white")
    t.goto(-90-i, -290-i)
    t.dot(2, "white")
for i in range(6):
    t.goto(-640+i, 260-i)
    t.dot(2, "white")
    t.goto(-640-i, 260-i)
    t.dot(2, "white")
for i in range(0, 52, 2):
    t.pensize(1)
    t.goto(-640, -290+i*10)
    t.setheading(0)
    t.color("white")
    t.pendown()
    t.backward(6)
    t.forward(12)
    if i == 10 or i == 20 or i == 30 or i == 40 or i == 50:  
        t.pencolor("gray")
        t.pensize(0.1)
        t.forward(524)
    t.penup()
for i in range(0, 52, 2):
    t.pensize(1)
    t.goto(-640+i*10, -290)
    t.setheading(90)
    t.color("white")
    t.pendown()
    t.backward(6)
    t.forward(12)
    if i == 10 or i == 20 or i == 30 or i == 40 or i == 50:  
        t.pencolor("gray")
        t.pensize(0.1)
        t.forward(524)
    t.penup()

t.color("white")
t.pensize(1)
for i in range(2, 52, 2):
    t.goto(-665, -294+i*10)
    t.write(i)
for i in range(2, 52, 2):
    t.goto(-644+i*10, -310)
    t.write(i)
t.hideturtle()

def drawxy(s, x, y):
    t.pencolor("white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y+300)
    t.setheading(225)
    t.forward(4)
    t.penup()
    t.goto(x, y+300)
    t.setheading(315)
    t.pendown()
    t.forward(4)
    t.penup()

    for i in range(0, 29, 1):
        t.setheading(0)
        t.pencolor("white")
        t.goto(x, y+i*10)
        t.pendown()
        t.forward(5)
        if i == 0 or i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
            t.pencolor("gray")
            t.forward(295)
            t.penup()
            if s == "Vx" and i == 0: 
                t.goto(x, y+i*10)
                t.pencolor("white")
                t.pendown()
                t.forward(300)
                t.setheading(135)
                t.forward(5)
                t.backward(5)
                t.setheading(225)
                t.forward(5)
            if s == "Vy" and i == 15:
                t.goto(x, y+i*10)
                t.pencolor("white")
                t.pendown()
                t.forward(300)
                t.setheading(135)
                t.forward(5)
                t.backward(5)
                t.setheading(225)
                t.forward(5)
            if s == "ax" and i == 25:
                t.goto(x, y+i*10)
                t.pencolor("white")
                t.pendown()
                t.forward(300)
                t.setheading(135)
                t.forward(5)
                t.backward(5)
                t.setheading(225)
                t.forward(5)
            if s == "ay" and i == 25:
                t.goto(x, y+i*10)
                t.pencolor("white")
                t.pendown()
                t.forward(300)
                t.setheading(135)
                t.forward(5)
                t.backward(5)
                t.setheading(225)
                t.forward(5)
        t.penup()

    for i in range(0, 29, 1):
        t.goto(x-20, y-5+i*10)
        if i == 0 or i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
            if s == "Vx": 
                t.write(i)
            if s == "Vy":
                t.write(i-15)
            if s == "ax":
                t.write(i-25)
            if s == "ay":
                t.write(i-25)
    
    for i in range(1, 6, 1):
        if s == "Vx": 
            t.goto(x+i*50, y-15)
            t.write(i)
        if s == "Vy":
            t.goto(x+i*50, y+135)
            t.write(i)
        if s == "ax":
            t.goto(x+i*50, y+235)
            t.write(i)
        if s == "ay":
            t.goto(x+i*50, y+235)
            t.write(i)

        
    for i in range(1, 29, 1):
        t.setheading(90)
        t.pencolor("gray")
        t.goto(x+i*10, y)
        t.pendown()
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
            t.pencolor("gray")
            t.forward(300)

        t.penup()
    
    for i in range(1, 29, 1):
        t.setheading(90)
        if s == "Vx" and i == 0: 
            t.goto(x+i*10, y-3)
        if s == "Vy" and i == 15:
            t.goto(x+i*10, y+147)
        if s == "ax" and i == 25:
            t.goto(x+i*10, y+247)
        if s == "ay" and i == 25:
            t.goto(x+i*10, y+247)
        t.forward(6)
    

    
    if s == "Vx": 
        t.goto(x+305, y-5)
    if s == "Vy":
        t.goto(x+305, y+145)
    if s == "ax":
        t.goto(x+305, y+245)
    if s == "ay":
        t.goto(x+305, y+245)
    t.write("t")
    t.goto(x-10, y+305)
    t.write(s)

    
drawxy("Vx", 25, 25)
drawxy("Vy", 25, -325)
drawxy("ax", 360, 25)
drawxy("ay", 360, -325)


##############################caculate...

T = 0
Cd = 0.47
rho = 1.225
dt = 0.01
g = 9.81
d = 0.0
h = float(input("heigth of the ball : "))
v0x = float(input("initial velocity (x direction) of the ball(m/s) : "))
v0y = float(input("initial velocity (y direction) of the ball(m/s) : "))
vx = v0x
vy = v0y
v = math.sqrt(vx*vx+vy*vy)
r = float(input("radius or the ball (m) : "))
m = float(input("mass of the ball (kg) : "))
Area = r * r * math.pi
k = (Cd * rho * Area)/(2 * m)

t.goto(-600, 340)
t.pencolor("white")
t.write(f"h0 = {h:.2f}m, V0x = {v0x:.2f}m/s, V0y = {v0y:.2f}m/s, r = {r:.4f}m, m = {m:.4f}kg")

t1.color("white")
t1.penup()
draw.penup()

def draw_four_graph(graph, time, value):
    if graph == "Vx":
        text = "Vx"
        x_2 = 25
        y_2 = 25
        pencolor = "white"
    if graph == "Vy":
        text = "Vy"
        x_2 = 25
        y_2 = -175
        pencolor = "red"
    if graph == "ax":
        text = "ax"
        x_2 = 360
        y_2 = 275
        pencolor = "yellow"
    if graph == "ay":
        text = "ay"
        x_2 = 360
        y_2 = -75
        pencolor = "green"
    t.goto(x_2+time*50, y_2+value*10)
    t.dot(4, pencolor)
    t1.goto(x_2+5+time*50, y_2+5+value*10)
    t1.write(text + f" = {value:.2f}")
    
    

def update():
    global T, h, vy, vx, ax, d
    v = math.sqrt(vx*vx+vy*vy)

    ay = -g - k * v * vy
    ax = -k * v * vx

    d += vx * dt
    h += vy * dt

    vy += ay * dt
    vx += ax * dt

    t1.clear()
    t1.goto(-630, -340)
    
    t1.pencolor("yellow")
    t1.write(f"Vx: {vx:.2f}   Vy: {vy:.2f} (m/s)   ax: {ax:.2f} (m/s^2)   ay: {ay:.2f} (m/s^2)   t: {T:.2f} (s)")
    t1.goto(-640 + d*10, -290 + h * 10)
    draw.goto(-640 + d*10, -290 + h * 10)
    t1.pencolor("white")
    t1.write(f"(x, y) = ({d:.2f}, {h:.2f})")
    draw.dot(5, "red")

    draw_four_graph("Vx", T, vx)
    draw_four_graph("Vy", T, vy)
    draw_four_graph("ax", T, ax)
    draw_four_graph("ay", T, ay)

    T += dt

    t1.hideturtle()
    draw.hideturtle()
    turtle.update()

    if h>0:
        turtle.ontimer(update, int(dt * 100))
    else : 
        print("completed!")

update()


##############################
t1.hideturtle()
turtle.update()
turtle.done()


