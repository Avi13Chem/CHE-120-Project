"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange #randrange selects a random item from a range.
from turtle import *

from freegames import vector

ball = vector(-200, -200) #Initial ball placement is at the bottom left corner of the map
speed = vector(0, 0)
targets = [] 


def tap(x, y):
    """Respond to screen tap."""  #If the ball isn't currently on the screen, it develops the coordinate of the ball on the screen where the user has clicked.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25 
        #This makes inside(ball) == True untill it leaves the screen


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y) #Goes to every coordanite within the space and draws a large blue ball
        dot(20, 'blue')

    if inside(ball): #When clicked, this draws a red circle on the coordinate. 
        goto(ball.x, ball.y)
        dot(6, 'red')

    update() #constantly refreshes the screen to provide smooth animations for objects. 


def move(): 
    """Move ball and targets."""
    if randrange(40) == 0: #There is a 1/40 chance that a target will spawn 
        y = randrange(-150, 150) #This places the y coordinate of the target
        target = vector(200, y) #This makes the coordanates for which the target will appear
        targets.append(target) #This attaches the target to the list of targets so it will spawn on the map

    for target in targets: 
        target.x -= 0.5 #This is the speed at which each of the targets move. 

    if inside(ball): #Only applies when the ball is launched
        speed.y -= 0.35 #This is the gravity of the ball
        ball.move(speed) #Sets the new speed of the ball each iteration

    dupe = targets.copy() #This is how the ball deletes a target without destroying the entire set
    targets.clear() 

    for target in dupe: #This adds it back to the set of targets of the ball hasn't touched it.
        if abs(target - ball) > 13:
            targets.append(target) #Lines 65-70 shows how the blue ball gets deleted when the red ball touches it.

    draw()

    for target in targets: #
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()