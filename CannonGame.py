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
bombs = []
powers = []
lives = 3
ballLine = []


def tap(x, y):
    global ballLine
    """Respond to screen tap."""  #If the ball isn't currently on the screen, it develops the coordinate of the ball on the screen where the user has clicked.
    if not inside(ball):
        ballLine.clear()
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25 
        #This makes inside(ball) == True untill it leaves the screen


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    global ballLine
    """Draw ball and targets."""
    clear()

    goto(-200,180)
    text = "Lives: " + str(lives)
    write(text)

    goto(-200,-200)
    pendown()
    for point in ballLine:
        goto(point[0], point[1])
    penup()

    for target in targets:
        goto(target.x, target.y) #Goes to every coordanite within the space and draws a large blue ball
        dot(20, 'blue')

    for bomb in bombs:
        goto(bomb.x, bomb.y)
        dot(20, 'black')

    if inside(ball): #When clicked, this draws a red circle on the coordinate. 
        goto(ball.x, ball.y)
        ballLine.append([ball.x, ball.y])
        dot(6, 'red')


    for power in powers: 
        goto(power.x, power.y)
        dot(20, 'green')

    update() #constantly refreshes the screen to provide smooth animations for objects. 

def move(): 
    global lives
    """Move ball and targets."""
    if randrange(40) == 0: #There is a 1/40 chance that a target will spawn 
        y = randrange(-150, 150) #This places the y coordinate of the target
        target = vector(200, y) #This makes the coordanates for which the target will appear
        targets.append(target) #This attaches the target to the list of targets so it will spawn on the map
    
    if randrange(120) == 0: 
        y = randrange(-150,150)
        x = randrange(-150,150)
        power = vector(x,y)
        powers.append(power)

    if randrange(60) == 0:
        y = randrange(-150, 150)
        bomb = vector(200, y)   # start from the right side, like targets
        bombs.append(bomb)

    for target in targets: 
        target.x -= 0.5 #This is the speed at which each of the targets move. 
    
    for bomb in bombs:
        bomb.x -= 0.5

    if inside(ball): #Only applies when the ball is launched
        speed.y -= 0.35 #This is the gravity of the ball
        ball.move(speed) #Sets the new speed of the ball each iteration

    dupe = targets.copy() #This is how the ball deletes a target without destroying the entire set
    targets.clear() 

    for target in dupe: #This adds it back to the set of targets of the ball hasn't touched it.
        if abs(target - ball) > 13:
            targets.append(target) #Lines 65-70 shows how the blue ball gets deleted when the red ball touches it.

    for power in powers: 
      if abs(power - ball) <13: 
            powers.remove(power)
            lives +=1

    for bomb in bombs.copy():
        if abs(bomb - ball) < 13:
            bombs.remove(bomb)
            lives -= 1

    draw()

    for target in targets: #If a target is not on screen, end the game.
        if not inside(target):
            targets.remove(target)
            lives -= 1

    for bomb in bombs.copy():
        if not inside(bomb):
         bombs.remove(bomb)

    if lives < 0:
        clear()
        return
    ontimer(move, 50) #everytimes 50 milliseconts passes, it goes through the move function again.
    #This is how it loops itself at the end. 


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
#clear()
done()