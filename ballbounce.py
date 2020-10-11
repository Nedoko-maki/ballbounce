import math


class ball:
    def __init__(self, xpos, ypos, xspeed, yspeed, xforce, yforce, accel, mass, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.xforce = xforce
        self.yforce = yforce
        self.accel = accel
        self.mass = mass
        self.radius = radius
        
    def drag(self):
        area = pi * self.radius**2
        velocitysq = self.xspeed**2 + self.yspeed**2
        drag = (Cd * density * velocitysq * area)/2
        return drag

    
# WEIGHT
# DRAG / TERMINAL VELOCITY
# AIR BUOYANCY
# USER INTERACTION
# WIND (LAST)

#CONSTANTS#

g = -9.81 #N/kg or m/s^2
dt = float(0.01) #seconds
Cd = 0.47
pi = float(math.pi)
density = 1.225

xborder = 100 #+-50
yborder = 100 #+-50
        
ball1 = ball(0, 0, 0, 0, 0, 0, 0, 0.2, 0.2)
time = 100

settings = input("Say 1 for default settings. Say 2 for custom settings:")

if settings == "1":
    pass
elif settings == "2":
    dt = float(input("dt (time period): "))
    ball1.xspeed = float(input("initial x speed: "))
    ball1.yspeed = float(input("initial y speed: "))
    ball1.mass = float(input("mass: "))
    ball1.radius = float(input("radius: "))
    time = int(input("times (integer) (time = times*dt): "))

ball1.xpos = xborder/2
ball1.ypos = yborder/2



#acceleration = (sum of all forces) / mass
#velocity += acceleration * dt
#position += velocity * dt


#ball1.xforce?

##for x in range(1, 100):
##    
##    if ball1.yforce >= 0:
##        ball1.accel = ( (((ball1.yforce**2 + ball1.xforce**2)**0.5) - ball1.drag()) / ball1.mass)
##    else:
##        ball1.accel = ( (((ball1.yforce**2 + ball1.xforce**2)**0.5) + ball1.drag()) / ball1.mass)
##
##
##    velocity = velocity + ball1.accel * dt
##
##    if ball1.xforce == 0:
##        if ball1.yforce > 0:
##            ball1.yspeed = velocity
##        elif ball1.yforce <= 0:
##            ball1.yspeed = -1*velocity
##    else:
##        ball1.xspeed = velocity*math.cos(math.tan(math.atan(ball1.yforce/ball1.xforce)))
##        ball1.yspeed = velocity*math.sin(math.tan(math.atan(ball1.yforce/ball1.xforce)))
##
##    ball1.xpos = ball1.xpos + ball1.xspeed * dt
##    ball1.ypos = ball1.ypos + ball1.yspeed * dt
##    print(str(x) + ": xpos:" + str(ball1.xpos))
##    print(str(x) + ": ypos:" + str(ball1.ypos))

for x in range(1, time):

    if abs(ball1.drag()) < abs(ball1.mass*g):
        ball1.yspeed += g*dt

    ball1.xforce = (0.5*ball1.mass*ball1.xspeed)/dt
    ball1.yforce = (0.5*ball1.mass*ball1.yspeed)/dt

    totalforce = ((ball1.yforce**2 + ball1.xforce**2)**0.5)
    
    print(str(x) + ": ttlfrc:" + str(totalforce))

    ball1.xforce = ball1.xforce / totalforce
    ball1.yforce = ball1.yforce / totalforce
    totalforce -= ball1.drag()
    ball1.xforce = ball1.xforce * totalforce
    ball1.yforce = ball1.yforce * totalforce

    ball1.xspeed = (2*ball1.xforce*dt)/ball1.mass
    ball1.yspeed = (2*ball1.yforce*dt)/ball1.mass

    print(str(x) + ": xsp:" + str(ball1.xspeed))
    print(str(x) + ": ysp:" + str(ball1.yspeed))
    
    ball1.xpos += ball1.xspeed*dt
    ball1.ypos += ball1.yspeed*dt

    if abs(ball1.xpos)+ball1.radius >= xborder or abs(ball1.xpos)+ball1.radius <= 0: #bounce code
        ball1.xspeed = ball1.xspeed * -1
    elif abs(ball1.ypos)+ball1.radius >= yborder or abs(ball1.ypos)+ball1.radius <= 0:
        ball1.yspeed = ball1.yspeed * -1

    print(str(x) + ": xpos:" + str(ball1.xpos))
    print(str(x) + ": ypos:" + str(ball1.ypos))
    print(str(x) + ": drag:" + str(ball1.drag()))
