import random
import math
#A MAJOR limitation of this program at the moment is the inability for it to work with any function that has asymptopes.
#The algorithm inherently allows any function to become a density curve, but bounded regions must be defined so that area is finite.
#However, the algorithm works on relative proportions, so bounded are does not need to be equal to 1
#The program is, in a sense, a monte carlo simulation applied to a continuous function
#===========================================================================================================================================
#===========================================================================================================================================
#function defines density curve. (Must work in conjunction with findZeroes())
def densityCurve(x):
  y = float(-1*(math.log10(x**7))+12) #Although this is not an input that is run, that curve may be changed to any function one wants.
  return y
#function finds zero for logorithm. MUST INPUT SAME FUNCTION AS IN DENSITY CURVE, BUT ISOLATING X!
def findZeroes(y): # attemps to find zeroes for the function. If it cannot do so, it will prompt the user for som bounded range of random numbers.
  x = float(10**(-1*((y-12)/7)))#bounding the range ensures that inputted functions do not need bounded area = 1
  return x
maxRange = float(input("Max y value: "))#For the progrram to work even in the case of asymptopes, we must define a max y value which the program will test. This ensures that bounded area is finite. 
print(maxRange)
xList = []
#var zero = zeroes of the density curve, ie: range
leftBound = float(input("Left bound: "))
rightBound = float(input("Right bound: "))

for i in range(100):#creating 100 random numbers from 1 to the range (range defined as var zero)
  x = random.uniform(leftBound,rightBound)#creating 100 random numbers from 1 to the range (range defined as var zero)
  y = densityCurve(x)
  test = random.uniform(0,maxRange)#testing the y value to see if the x is a "success"
  #if test fails, we generate new random until it doesnt with this while loop
  while (test > y):
    x = random.uniform(leftBound,rightBound)
    y = densityCurve(x)
    test = random.uniform(0,maxRange)
  #Every succesful x value we recieve is appended to the list xList. 
  xList.append(x)#Generated random numbers are interpreted as the x values which were considered a success because a randomly chosen y value within the bound returned y values that corresponded to the x output
xList.sort()
print(xList)
lowList = []
highList = []

midPoint = (leftBound+rightBound)/2
#Tests how many values are in each range so we know the program is working.
for element in(xList):
  if (element < midPoint):
    lowList.append(element)
  else:
    highList.append(element)
print("<{}: ".format(midPoint) + str(len(lowList)))#if distribution has a mean the same as the midpoint, returned low and high lists should be roughly equal
print(">{}: ".format(midPoint) + str(len(highList)))
