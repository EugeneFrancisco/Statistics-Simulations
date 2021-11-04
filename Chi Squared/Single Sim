0.2#PROGRAM FUNCTIONALITY
# This program simulates sampling from a population with frequencies that apply to any number of categorical variables within the population
# When prompted for sample size, it is the equivelent of sampling n number of individuals from a population that has some frequency distribution
# The number of categories represenents the categorical variables which should have some population relative frequency.
# The program will ask for individidual expected frequencies for each category
# Program output is a simulated trial of picking n number of individuals from the inputted population distribution
# Example: Picking 100 m&ms from a large bag of m&ms, where the distribution of 5 colors is uniform: sample size = 100, categories = 5, expected frequencies all = 0.2
# To run the program, click the small play button on the top left of the cell. 
#============================================
import random
def makeCumulative(arr): #returns cumulative list where first index is 0.
  new_arr = [] 
  sum = 0
  for element in arr:
    sum = element+sum
    new_arr.append(sum)
  return new_arr
def sequentialList(end): #returns array of all integers up to end. For example, if end =5 5, sequentialList = 1,2,3,4,5
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
def countTimesRepeated(arr, groups): #Count times some numer is repeated in an array and returns that number
  arr.sort()
  glist = sequentialList(groups)  #glist, when group = 4, = 1,2,3,4
  totalSuccesses = [] #final list which should contain the successe for each category
  for x in range(groups):
    individualSuccess = countSuccesses(arr,glist[x])
    totalSuccesses.append(individualSuccess)
  return totalSuccesses
def calculateProportions(array): #some array of counts are ocnverted into an array of proportions of count/total counts
  sum = 0
  for element in array:
    sum = sum+element
  propList = []
  for element in array:
    p = element/sum
    propList.append(p)
  return propList
n = int(input("What is your sample size? ")) #n = number in total sample. Example; taking 50 m&ms, n=50
groups = int(input("How many categories in distribution? ")) #groups is the number of categories in the distribution; if selected m&ms have 5 different colors, groups = 5
#======================
#the following for loop will define the distribution. Each group will be assigned an expected probability. All group's probability's should sum to 1
#======================
proportionsList = [] #array where each index represents one group and the associated float represents the expected probability of the group

for x in range(groups):
  proportion = float(input("Category: " + str(x+1) + " expected frequency? "))
  proportionsList.append(proportion)
proportionsList = makeCumulative(proportionsList)
#print(proportionsList) #for debugging
#================================
#Creating random numbers from 0,1 to simulate. n numbers will be created
#================================
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
successList.sort()
#print(successList) #the amont of times a certain number is repeated represents the count of successes that number had.
#print(len(successList))
totalSuccesses = countTimesRepeated(successList, groups)
print("Total Successes, indexed by associated group", totalSuccesses)#returned list is indexed where each index is the assocaited category. The first index corresponds to the first category.
print("Proportions of succeses, indexed by associated group", calculateProportions(totalSuccesses))
