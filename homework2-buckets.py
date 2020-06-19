#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8 
#Homework 2


#Part 2


from turtle import *

# Create and set up your "turtle" and "screen" variables here.
ryan = Turtle()
ryan.speed(1000)
screen = ryan.getscreen()
# Pre-defined value for the code that draws buckets. Don't change it!
bucketSize = 90

# Below are pre-defined functions you can use to draw the buckets
# and marbles.

# This function tells Turtle t to draw a bucket at position (x,y).
def drawBucket(t, x, y):
    global bucketSize
    t.pu()
    pos = t.pos()
    heading = t.heading()
    pencolor = t.pencolor()
    thickness = t.width()

    t.pencolor("blue")
    t.width(2)
    t.goto(x, y)
    t.seth(270)
    t.pd()
    for i in range(3):
        t.fd(bucketSize)
        t.lt(90)

    t.pu()
    t.setpos(pos)
    t.seth(heading)
    t.width(thickness)
    t.pencolor(pencolor)

# This function tells Turtle t to draw a group of marbles at position (x,y).
# The value for "marbles" must be between 1 and 5, inclusive.
def drawMarbles(t, x, y, marbles):
    global bucketSize
    t.pu()
    pos = t.pos()
    heading = t.heading()
    pencolor = t.pencolor()
    thickness = t.width()

    marbleRad = 10
    t.color("blue", "cyan")

    if marbles >= 1:
        t.goto(x+2*marbleRad, y-bucketSize+10)
        t.pd()
        t.begin_fill()
        t.circle(marbleRad)
        t.end_fill()
        t.pu()
    if marbles >= 2:
        t.setx(t.xcor()+marbleRad+10)
        t.pd()
        t.begin_fill()
        t.circle(marbleRad)
        t.end_fill()
        t.pu()
    if marbles >= 3:
        t.setx(t.xcor()+marbleRad+10)
        t.pd()
        t.begin_fill()
        t.circle(marbleRad)
        t.end_fill()
        t.pu()

    if marbles >= 4:
        t.goto(x+3*marbleRad, y-bucketSize+2*marbleRad+10)
        t.pd()
        t.begin_fill()
        t.circle(marbleRad)
        t.end_fill()
        t.pu()

    if marbles == 5:
        t.setx(t.xcor()+marbleRad+10)
        t.pd()
        t.begin_fill()
        t.circle(marbleRad)
        t.end_fill()
        t.pu()

    t.pu()
    t.setpos(pos)
    t.seth(heading)
    t.width(thickness)
    t.pencolor(pencolor)

# This function tells Turtle t to erase the marbles located at position (x,y).
def eraseMarbles(t, x, y):
    global bucketSize
    t.pu()
    pos = t.pos()
    heading = t.heading()
    pencolor = t.pencolor()
    fillcolor = t.fillcolor()
    thickness = t.width()

    t.color("white", "white")
    t.goto(x+5, y-5)
    t.seth(270)
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.fd(bucketSize-10)
        t.lt(90)
    t.end_fill()

    t.pu()
    t.setpos(pos)
    t.seth(heading)
    t.width(thickness)
    t.fillcolor(fillcolor)
    t.pencolor(pencolor)

##### This is test code. Erase it once you understand it! #####

##### End of test code. #####


# Below you should declare (create) any variables you need for your program.
gameover = False
buckets = [1,1,1,1,1]


# Write code here to print the name of the game at the top of the screen.
ryan.write("Welcome to A Drop in the Bucket")
font=("Times New Roman",20,"normal")
ryan.penup()
ryan.goto(50,50)
# Draw the initial state of the game: 5 buckets with 1 marble in each.
drawBucket(ryan,-200,-100)
drawBucket(ryan,-100,-100)
drawBucket(ryan,0,-100)
drawBucket(ryan,100,-100)
drawBucket(ryan,200,-100)


drawMarbles(ryan,-200,-100,1)
drawMarbles(ryan,-100,-100,1)
drawMarbles(ryan,0,-100,1)
drawMarbles(ryan,100,-100,1)
drawMarbles(ryan,200,-100,1)

# Now write the main "game loop" which plays the game.
def invalid_move(s):
     s =int(s)
     if not s in range(1,5):
         return 1
     elif buckets[s-1]==0:
         return 2
     return 0
    
while not gameover:
    
    p1choice = screen.textinput("Player 1's Turn","Which bucket do you select?")
    while invalid_move (p1choice):
        if invalid_move (p1choice)==1:
              p1choice = screen.textinput("Player 1's Turn","That was an invalid bucket number! Please try again.\n Which bucket do you select?") 
        elif invalid_move (p1choice)==2:
              p1choice = screen.textinput("Player 1's Turn","That bucket has no marbles in it! Please try again.\n Which bucket do you select?")     
    buckets[int(p1choice)]=buckets[int(p1choice)]+buckets[int(p1choice)-1]
    buckets[int(p1choice)-1]=0


    eraseMarbles(ryan,(int(p1choice)-3)*100,-100)
    eraseMarbles(ryan,(int(p1choice)-2)*100,-100)
    drawMarbles(ryan,(int(p1choice)-3)*100,-100,buckets[int(p1choice)-1])
    drawMarbles(ryan,(int(p1choice)-2)*100,-100,buckets[int(p1choice)])
    if buckets[4]==5:
        ryan.goto(0,100)
        ryan.write("Player 1 wins!")
        gameover = True
        continue

    
    p2choice = screen.textinput("Player 2's Turn","Which bucket do you select?")
    while invalid_move (p2choice):
        if invalid_move (p2choice)==1:
              p2choice = screen.textinput("Player 2's Turn","That was an invalid bucket number! Please try again.\n Which bucket do you select?") 
        elif invalid_move (p2choice)==2:
              p2choice = screen.textinput("Player 2's Turn","That bucket has no marbles in it! Please try again.\n Which bucket do you select?")     
    buckets[int(p2choice)]=buckets[int(p2choice)]+buckets[int(p2choice)-1]
    buckets[int(p2choice)-1]=0


    eraseMarbles(ryan,(int(p2choice)-3)*100,-100)
    eraseMarbles(ryan,(int(p2choice)-2)*100,-100)
    drawMarbles(ryan,(int(p2choice)-3)*100,-100,buckets[int(p2choice)-1])
    drawMarbles(ryan,(int(p2choice)-2)*100,-100,buckets[int(p2choice)])
    if buckets[4]==5:
        ryan.goto(0,100)
        ryan.write("Player 2 wins!")
        gameover = True
        continue 
    

# The two players should take turns. After each turn, erase whichever
# bucket(s) should be erased and draw the new configuration of buckets
# with marbles inside of each.
# Keep playing until someone wins and then display the winner.


# Game over! Call done() to keep the window open.
done()























