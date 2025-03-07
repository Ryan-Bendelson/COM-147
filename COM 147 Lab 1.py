#Ryan Bendelson, Liam Booth, and Joe Thatcher Code
#Install Scipy using pip command in Anaconda Prompt prior to running this file
import numpy as np #Import numpy as np
#from scipy import linalg #Import the linear algebra module of Scipy
import math #Import the math library
import random #Import the random module

#Create a function that will return a matrix of strings which say "clean" of a given size
def makeGrid(numRows, numCols):
    matrix = np.array(["clean"]) #Make a 1 by 1 numpy array stored as matrix

    #Put the right number of elements in matrix
    for i in range(1, (numRows * numCols)):
        matrix = np.append(matrix, ["clean"])

    matrix = matrix.reshape(numRows, numCols) #Reshape the matrix to have the right number of rows and columns
    return matrix

#Create a function that will take an entirely clean matrix and make a random selection of tiles dirty
def makeDirty(matrix):
    #Store the matrix's size
    numRows = len(matrix)
    numCols =(len(matrix[0]))

    #Traverse through all the rows and columns of the matrix
    for i in range(0, numRows):
        for j in range(0, numCols):

            #Choose random tiles in the matrix and make them dirty
            if(random.randint(1, 2) > 1):
                matrix[i][j] = "dirty"
                
    return matrix

#Create a function that will check and return if a tile is dirty or not
def checkDirty(matrix, i, j):
    return (matrix[i][j] == "dirty")

#Create a function that makes a vacuum which stores information for which tile it is on
def makeVacuum(i, j):
    vacuum = [i, j]
    return vacuum

#Create a function that will clean a specified tile if dirty and report if it cleaned it or not
def makeClean(matrix, i, j):
    dirty = checkDirty(matrix, i, j)
    matrix[i][j] = "clean"

    #Report if specified tile is was cleaned or already clean
    if(dirty):
        print("Tile in row", i, "and column", j, "was cleaned.")
    else:
        print("Tile in row", i, "and column", j, "was already clean.")
    
    return matrix

#Create a function that will move the vacuum up one space if possible
def moveVacuumUp(matrix, vacuum):
    if(vacuum[0] > 0):
        vacuum[0] = vacuum[0] - 1
    return vacuum

#Create a function that will move the vacuum down one space if possible
def moveVacuumDown(matrix, vacuum):
    if(vacuum[0] < len(matrix) - 1):
        vacuum[0] = vacuum[0] + 1
    return vacuum

#Create a function that will move the vacuum left one space if possible
def moveVacuumLeft(matrix, vacuum):
    if(vacuum[1] > 0):
        vacuum[1] = vacuum[1] - 1
    return vacuum

#Create a function that will move the vacuum right one space if possible
def moveVacuumRight(matrix, vacuum):
    if(vacuum[1] < len(matrix[0]) - 1):
        vacuum[1] = vacuum[1] + 1
    return vacuum

#Create a function to report a vacuum's name and position
def vacuumPos(vacuum, vacuumName):
    print(vacuumName, "is in row", vacuum[0], "and column", vacuum[1])

#Create a function that moves the vacuum as far right as possible and cleans each tile its on
def cleanRight(world, vacuum, vacuumName):
    while(vacuum[1] < len(world[0]) - 1):
        vacuumPos(vacuum, vacuumName)
        world = makeClean(world, vacuum[0], vacuum[1])
        print("\n")
        moveVacuumRight(world, vacuum)
    vacuumPos(vacuum, vacuumName)
    world = makeClean(world, vacuum[0], vacuum[1])
    return world

#Create a function that moves the vacuum as far left as possible and cleans each tile its on
def cleanLeft(world, vacuum, vacuumName):
    while(vacuum[1] > 0):
        vacuumPos(vacuum, vacuumName)
        world = makeClean(world, vacuum[0], vacuum[1])
        print("\n")
        moveVacuumLeft(world, vacuum)
    vacuumPos(vacuum, vacuumName)
    world = makeClean(world, vacuum[0], vacuum[1])
    return world

#Create a function to move a vacuum through a grid in a snake pattern
def vacuumSnake(world, vacuum, vacuumName):

    #Move the vacuum right, down, then left to clean each pair of rows
    while(vacuum[0] < len(world) - 1):
        world = cleanRight(world, vacuum, vacuumName)
        moveVacuumDown(world, vacuum)
        print("\n")
        world = cleanLeft(world, vacuum, vacuumName)
        moveVacuumDown(world, vacuum)
        print("\n")
        
    #Make the vacuum clean the last row if world has an odd number of rows
    if((len(world) % 2) == 1):
        world = cleanRight(world, vacuum, vacuumName)
    
    return world

#Create a function to move a vacuum to the start position of a grid (i.e. top left corner)
def moveVacuumToStart(world, vacuum, vacuumName):

    #Make the vacuum go to the top row and report where it moves
    while(vacuum[0] > 0):
        vacuumPos(vacuum, vacuumName)
        moveVacuumUp(world, vacuum)

    #Make the vacuum go to the leftmost column and report where it moves
    while(vacuum[1] > 0):
        vacuumPos(vacuum, vacuumName)
        moveVacuumLeft(world, vacuum)

    #Report on vacuum status
    vacuumPos(vacuum, vacuumName)
    print("\n")
    print(vacuumName, "is at the start position.\n")
    
    return vacuum

#Create a function to clean the environment by moving a vacuum through the grid in a snake pattern
def cleanWorld1(world, vacuum, vacuumName):
    moveVacuumToStart(world, vacuum, vacuumName)
    vacuumSnake(world, vacuum, vacuumName)
    return world

#Create a function to clean the environment by moving the vacuum through the grid in a spiral pattern
def cleanWorld2(world, vacuum, vacuumName):
    moveVacuumToStart(world, vacuum, vacuumName)

    #Set the initial right, down, left, and up travel limits
    minRow = 1
    maxRow = len(world) - 1
    minCol = 0
    maxCol = len(world[0]) - 1

    #Traverse the grid in a spiral pattern and clean each tile traversed if dirty
    while((minRow <= maxRow + 1) & (minCol <= maxCol + 1)):
        #Make the vacuum travel right
        while(vacuum[1] < maxCol):
            vacuumPos(vacuum, vacuumName)
            world = makeClean(world, vacuum[0], vacuum[1])
            print("\n")
            moveVacuumRight(world, vacuum)
        maxCol = maxCol - 1
            
        #Make the vacuum travel down
        while(vacuum[0] < maxRow):
            vacuumPos(vacuum, vacuumName)
            world = makeClean(world, vacuum[0], vacuum[1])
            print("\n")
            moveVacuumDown(world, vacuum)
        maxRow = maxRow - 1
        
        #Make the vacuum travel left
        while(vacuum[1] > minCol):
            vacuumPos(vacuum, vacuumName)
            world = makeClean(world, vacuum[0], vacuum[1])
            print("\n")
            moveVacuumLeft(world, vacuum)
        minCol = minCol + 1
        
        #Make the vacuum travel up
        while(vacuum[0] > minRow):
            vacuumPos(vacuum, vacuumName)
            world = makeClean(world, vacuum[0], vacuum[1])
            print("\n")
            moveVacuumUp(world, vacuum)
        minRow = minRow + 1

    #Make sure the last tile is taken care of
    vacuumPos(vacuum, vacuumName)
    world = makeClean(world, vacuum[0], vacuum[1])
    return world

#Request all necessary user specififed information and store inputs
print("How tall should the environment be? (integer between 1 and 10):")
input1 = input()
print("How wide should the environment be? (integer between 1 and 10):")
input2 = input()
print("What name should the vacuum have?:")
input3 = input()
print("What row should the vacuum start in? (integer between 0 and (height - 1)):")
input4 = input()
print("What column should the vacuum start in? (integer between 0 and (width - 1)):")
input5 = input()
print("What cleaning method should the vacuum use? Type \"Spiral\" for spiral method. Type anything else for snake method:")
input6 = input()

#Store user specified numeric values as integers
height = int(input1)
width = int(input2)
startRow = int(input4)
startCol = int(input5)

#Check that numeric values fit parameters and use default values if they don't
if((height < 1) or (height > 10)):
    print("\nHeight value is invalid. A default value of 5 will be used.")
    height = 5
if((width < 1) or (width > 10)):
    print("\nWidth value is invalid. A default value of 5 will be used.")
    width = 5
if((startRow < 0) or (startRow > (height - 1))):
    print("\nStart row value is invalid. A default value of 0 will be used.")
    startRow = 0
if((startCol < 0) or (startCol > (width - 1))):
    print("\nStart column value is invalid. A default value of 0 will be used.")
    startCol = 0

#Generate the world and vacuum
print("\nGenerating World Now")
world = makeGrid(height, width)
world = makeDirty(world)
print("\nSetting Up Vacuum Now.", input3, "is ready.\n")
vacuum = makeVacuum(startRow, startCol)
print(world, "\n")

#Perform cleaning with user specified cleaning method
if(input6.lower() == "spiral"): #Check if the user typed "Spiral" without being case-sensitive
    print("Movement Method: Spiral\n")
    print(cleanWorld2(world, vacuum, input3))
else:
    print("Movement Method: Snake\n")
    print(cleanWorld1(world, vacuum, input3))
