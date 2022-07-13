#EUGENE FRANCISCO, NOV 8, 2021;
#Given some regression line where deviation from regression line is normal
#
#================================ Imports =============================================
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import torch
#=============================== Defining Functions ====================================
def densityCurve(x):#defines density curve. In this case, it is a normal distribution. May be anything (with some tweaking) !!
  y = ((math.e)**((-1*x**2)/2)/((2*math.pi)**1/2))
  return y
def regressionLine(x,b,m):#defines the regression line which we will be sampling from
  y = (m*x)+b
  return y
def randomFromGauss(mean, SD):#samples randomly from normal distribution given mean and standard deviation. Continuous
  testx = random.uniform(-5,5)
  testy = random.uniform(0,0.3989422804)
  y = densityCurve(testx)
  while testy > y:
    testx = random.uniform(-5,5)
    testy = random.uniform(0,0.3989422804)
    y = densityCurve(testx)
  return ((testx*SD)+mean)
def sampleFromReg(leftBound, rightBound, SD): #remember this is standard deviation of the residuals; simulates sampling from the regression line
  x = random.uniform(leftBound,rightBound)
  mean = regressionLine(x,10,2)
  sampledData = randomFromGauss(mean, SD) # simulating residual pattern which we assume to be normal at all places
  return x, sampledData
def plotLine(domain,b,m): #Plots the regression line. "b" is y intercept, "m" is slope, and "domain" is the defined domain
  x = np.arange(domain)
  plt.plot(x, (m*x)+b, "-")
#================================================ Main ===========================================================
trials = int(input("How many trials: "))#the amount of elements in the sample
trialArr = []
leftBound = 0#minimum domain place where data my be extrapolated
rightBound = 10#the maximum place where data may be extrapolated
domain = rightBound - leftBound
for x in range(trials):
  trialArr.append(sampleFromReg(leftBound,rightBound,2))#(leftBound, rightBound, SD)
trialMat = torch.tensor(trialArr) #Matrix where first column is x value and second column is sampled y value
print(trialMat)#should be able to find a way to sort the matrix by the 2nd column.
plt.scatter(trialMat[:,0],trialMat[:,1])#scatterplot of sampled data
plt.show
plotLine(domain,10,2)#overlay of original regression line
