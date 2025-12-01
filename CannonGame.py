"""Cannon, hitting targets with projectiles.

Our changes:
Power ups
Lives
Parabola
Bombs
"""

"""
Names:
Avalon Martin-McTavish: AMM
Christopher Gunawan: CG
Retal Hashmi: RH
"""

from random import randrange #randrange selects a random item from a range.
from turtle import *

from freegames import vector

targetImage = "target.gif"

ball = vector(-200, -200) #Initial ball placement is at the bottom left corner of the map
speed = vector(0, 0)

#AMM Created variables to hold main information.
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

    #AMM Displayed the lives variables on screen.
    goto(-200,180)
    text = "Lives: " + str(lives)
    write(text)

    #AMM Drew the parabola of the ball.
    goto(-200,-200)
    pendown()
    for point in ballLine:
        goto(point[0], point[1])
    penup()

    for target in targets:
        goto(target.x, target.y) #Goes to every coordanite within the space and draws a large blue ball
        dot(20, 'blue')

    for bomb in bombs: #RH Loop through every bomb object in the bombs list
        goto(bomb.x, bomb.y) # RH each bomb has x and y attributes)
        dot(20, 'black') #RH Draw a black dot at that position to visually represent the bomb

    if inside(ball): #When clicked, this draws a red circle on the coordinate. 
        goto(ball.x, ball.y)
        ballLine.append([ball.x, ball.y])
        dot(6, 'red')


    for power in powers: #CG This draws a green dot at the coordinates of our powers. 
        goto(power.x, power.y)
        dot(20, 'green')

    update() #constantly refreshes the screen to provide smooth animations for objects. 

def move(): 
    global lives
    """Move ball and targets."""
    if randrange(40) == 0: #CG There is a 1/40 chance that a target will spawn 
        y = randrange(-150, 150) #CG This places the y coordinate of the target
        target = vector(200, y) #CG This makes the coordanates for which the target will appear
        targets.append(target) #CG This attaches the target to the list of targets so it will spawn on the map
    
    if randrange(120) == 0: #CG This spawns the powers when the iteration equals 0. To make it appear less often than targets, I've set the range to be longer
        y = randrange(-150,150) #CG The next two codes spawns the coordinates within a random place in the game screen
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
        bomb.x -= 0.5 #RH Move the bomb to the left by decreasing its x-coordinate

    if inside(ball): #Only applies when the ball is launched
        speed.y -= 0.35 #This is the gravity of the ball
        ball.move(speed) #Sets the new speed of the ball each iteration

    dupe = targets.copy() #This is how the ball deletes a target without destroying the entire set
    targets.clear() 

    for target in dupe: #This adds it back to the set of targets of the ball hasn't touched it.
        if abs(target - ball) > 13:
            targets.append(target) #Lines 65-70 shows how the blue ball gets deleted when the red ball touches it.

    for power in powers: 
      if abs(power - ball) <13: #Cg If the ball gets anywhere near the power ball, it removes it from the list and adds a life
            powers.remove(power)
            lives +=1

    for bomb in bombs.copy(): 
        if abs(bomb - ball) < 13: #RH Check if the distance between the bomb and the ball is less than 13 
            bombs.remove(bomb) #RH Remove the bomb that hit the ball
            lives -= 1 #RH Decrease the player's lives by 1

    draw()

    for target in targets: #If a target is not on screen, end the game.
        if not inside(target):
            targets.remove(target)
            lives -= 1

    for bomb in bombs.copy(): #RH # copy of the bombs list to avoid removing while looping
        if not inside(bomb):
         bombs.remove(bomb) #RH Remove the bomb from the list

    #AMM If all there are no more lives left, end the game.
    if lives < 0:
        clear()
        return
    ontimer(move, 50) #everytimes 50 milliseconds passes, it goes through the move function again.
    #This is how it loops itself at the end. 


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
#clear()
done()