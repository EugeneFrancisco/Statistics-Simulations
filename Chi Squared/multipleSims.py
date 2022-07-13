import random
import numpy#redundant at the moment
import torch#redundant at the moment
def makeCumulative(arr): #returns cumulative list where first index is 0
  new_arr = []
  sum = 0
  for element in arr:
    sum = element+sum
    new_arr.append(sum)
  return new_arr
def sequentialList(end): #outputs every integer up to a number. if end = 4, returns 1,2,3,4
  keepEnd = end
  sequentialList = []
  dList = []
  for x in range(end):
    end = end - 1
    dList.append(end)
  end = keepEnd
  for x in range(end):
    num = end-dList[x]
    sequentialList.append(num)
  return sequentialList
def countSuccesses(array,searchnum): #counts number of successes in list
  count = 0
  for element in array:
    if element == searchnum:
      count = count+1
  return count
def countTimesRepeated(arr, groups): #repeats the countSucceses function over every proportion in group and outputs the succese for every category of distribution
  arr.sort()
  glist = sequentialList(groups)  #glist, when group = 4, = 1,2,3,4
  totalSuccesses = [] #final list which should contain the successe for each category
  for x in range(groups):
    individualSuccess = countSuccesses(arr,glist[x])
    totalSuccesses.append(individualSuccess)
  return totalSuccesses
def calculateProportions(array): #calculates proportion given counts
  sum = 0
  for element in array:
    sum = sum+element
  propList = []
  for element in array:
    p = element/sum
    propList.append(p)
  return propList
def experiment(proportionsList): #runs the simulation and appends index of number to list
  randList = []
  for x in range(n):
    rand = random.uniform(0,1)
    randList.append(rand)
  successList = []
  for rand in randList:
    count = 0
    for proportion in proportionsList:
      count = count+1
      if (rand <= proportion):
        successList.append(count)
        break
  return successList
def findExpected(proportionsList, sampleSize): #outputs expected values
  expectedList = []
  for x in range(len(proportionsList)):
    expected = proportionsList[x]*n
    expectedList.append(expected)
  return expectedList
def findChiSquared(observedTuple,expectedTuple): #outputs a chi squared statistic given a list of observed and expected counts
  elementsList = []
  for x in range(len(observedTuple)):
    element = ((observedTuple[x]-expectedTuple[x])**2)/expectedTuple[x]
    elementsList.append(element)
  chiSquared = 0
  for num in elementsList:
    chiSquared = chiSquared + num
  return chiSquared
n = int(input("What is your sample size? ")) #n = number in total sample. Example; taking 50 m&ms, n=50
groups = int(input("How many categories in distribution? ")) #groups is the number of categories in the distribution; if selected m&ms have 5 different colors, groups = 5
#======================
#the following for loop will define the distribution. Each group will be assigned an expected probability. All group's probability's should sum to 1
#======================
proportionsList = [] #array where each index represents one group and the associated float represents the expectred probability of the group

for x in range(groups):
  proportion = float(input("Category: " + str(x+1) + " expected frequency? "))
  proportionsList.append(proportion)
originalProportions = proportionsList #originalProportions will contain a list of frequency distribution NOT CUMULATIVE
proportionsList = makeCumulative(proportionsList)
expectedList = findExpected(originalProportions,n)
print(expectedList)
#print(proportionsList) #for debugging
#================================
#Creating random numbers from 0,1 to simulate. n numbers will be created
#================================

numOfSimulations = int(input("How many simulations are you running? "))
allCounts = []
allProps = []
#simulating many many experiments
print("Output in form [trial num, simulated observed counts, chi-squared]")
for i in range(numOfSimulations):
  data = []
  successList = experiment(proportionsList)
  successList.sort
  totalSuccesses = countTimesRepeated(successList, groups)#the sampled counts for each trial. Let n=100 uniformly distributed into 5 catefories. totalSuccesses might be [19,21,20,16,24]
  data.append(totalSuccesses)
  data.append(findChiSquared(totalSuccesses,expectedList))
  print(i+1, data)
  totalProportions = calculateProportions(totalSuccesses)
  allCounts.append(totalSuccesses)
  allProps.append(totalProportions)

print(allCounts)
