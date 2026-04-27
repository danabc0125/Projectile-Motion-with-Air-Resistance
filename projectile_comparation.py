"""
This program compares two projectile motion simulations: one with air resistance and one without (ideal parabolic motion),
using user-defined parameters including mass, radius, initial velocity, and initial height.

The simulations are implemented using numerical methods (Euler method) to compute real-time motion.
Focusing on comparison, the program visualizes both trajectories to highlight the effects of air resistance.

Detailed velocity–time (v–t) and acceleration–time (a–t) graphs are not included in this version;
refer to projectile_simulation.py for a more comprehensive analysis.
"""

###python code

import turtle
import math

t = turtle.Turtle()
t1 = turtle.Turtle()
draw = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()

turtle.tracer(False) #if True ->too slow
turtle.setup(700, 1400)

turtle.hideturtle()
t.speed(0)
t1.speed(0)
draw.speed(0)
t2.speed(0)
s.bgcolor("black")
t.color("white")

t.setheading(0)
t.penup()
t.goto(-690, -290)
t.pendown()
t.goto(650, -290)
t.penup()
t.goto(-640, 260)
t.pendown()
t.goto(-640, -340)
t.penup()
t.goto(655, -305)
t.write("x(m)")
t.goto(-645, 265)
t.write("y(m)")
for i in range(6):
    t.goto(650-i, -290+i)
    t.dot(2, "white")
    t.goto(650-i, -290-i)
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
        t.forward(1280)
    t.penup()
for i in range(2, 130, 2):
    t.pensize(1)
    t.goto(-640+i*10, -290)
    t.setheading(90)
    t.color("white")
    t.pendown()
    t.backward(6)
    t.forward(12)
    if i % 10 == 0:  
        t.pencolor("gray")
        t.pensize(0.1)
        t.forward(524)
    t.penup()

t.color("white")
t.pensize(1)
for i in range(2, 52, 2):
    t.goto(-665, -294+i*10)
    t.write(i)
for i in range(2, 130, 2):
    t.goto(-644+i*10, -310)
    t.write(i)
t.hideturtle()

##############################calculate...

T = 0
Cd = 0.47
rho = 1.225
dt = 0.01
g = 9.81
d = 0.0
h = float(input("heigth of the ball : "))
p_d = 0
p_h = h
v0x = float(input("initial velocity (x direction) of the ball(m/s) : "))
v0y = float(input("initial velocity (y direction) of the ball(m/s) : "))
vx = v0x
vy = v0y
p_vx = v0x
p_vy = v0y
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
    
    

def update():
    global T, h, vy, vx, ax, p_vx, p_vy, d, p_d, p_h
    v = math.sqrt(vx*vx+vy*vy)

    ay = -g - k * v * vy
    ax = -k * v * vx

    d += vx * dt
    h += vy * dt

    p_d += p_vx * dt
    p_h += p_vy * dt

    vy += ay * dt
    vx += ax * dt

    p_vy -= g * dt

    if h >= 0 :
        t1.clear()
        draw.goto(-640 + d*10, -290 + h * 10)
        draw.dot(3, "red")
        t1.goto(-640 + d*10, -290 + h * 10)
        t1.pencolor("white")
        t1.write(f"(x, y) = ({d:.2f}, {h:.2f})")
    
    if p_h >= 0 :
        t2.clear()
        draw.goto(-640 + p_d * 10, -290 + p_h * 10)
        draw.dot(3, "white")
        t2.goto(-640 + p_d*10, -290 + p_h * 10)
        t2.pencolor("white")
        t2.write(f"(x, y) = ({p_d:.2f}, {p_h:.2f})")


    T += dt
    
    t1.hideturtle()
    draw.hideturtle()
    t2.hideturtle()
    turtle.update()

    if h>0 or p_h>0:
        turtle.ontimer(update, int(dt * 100))
    else : 
        print("completed!")

update()


##############################
t1.hideturtle()
turtle.update()
turtle.done()

