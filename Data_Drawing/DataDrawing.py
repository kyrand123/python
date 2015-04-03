from graphics import *                  #imports the graphics
from random import randint              #imports the random number
import time                             #imports the time


                                                        # Do some simple drawing
window = GraphWin("Visualisation", 200, 650)            #creates a simple graphic window

                                                        # Read in and print out the data in the data file
datafile = open("data.txt",'r')                         #opens the file with the data
myarray = datafile.readlines()                          #read lines into my array
for line in datafile:                                   #prints the data on the shell
    print(line)

while True:                                             #the forever looping 

    RightTop = 10                                       #sets the variables
    Rcorner = 20

    r = randint(0,255)                                  #creats a random RGB colour code
    g = randint(0,255)
    b = randint(0,255)

    #leftTop = 670

    number = 0  

    textCorner = 20
    for i in myarray:                                                            #loops through my array assisnging the values to i
                for x in range(-50,100):                                         # counters from -50 to 100, looping a lot
                    box1 = Rectangle(Point(x-10.00,RightTop),Point(i,Rcorner))      #creates a new rectangle from the variables and the length is i
                    box1.setOutline(color_rgb(0,0,0))                            # sets the outline to the colour black
                    box1.setFill(color_rgb(255,255,255))                         #uses the random RGB codes to fill the rectangle
                    box1.draw(window)                                            # draws the rectangle onto the created window
                text = Text(Point(120,textCorner),i)                             # creates a text image using the value assigned to i
                textCorner = RightTop + 30                                       # positions the text at the end of the rectangle
                text.draw(window)                                                # draws the text onto the created window
                time.sleep(0.05)                                                 # creates a delay so rectangles are filled at a slower pace

                RightTop = RightTop + 20                                         # changes the variables so that the rectangles are evenly spaced
                Rcorner = RightTop + 10


                            
window.getMouse()                                                                # Waits until the mouse is clicked before closing the window
