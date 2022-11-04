!pip install pynverse

from pynverse import inversefunc
from scipy.integrate import quad
from sympy import *
import math
import numpy as np
import random

def randomGaussian():#One weighted random value
  def f(x): #pdf
    return math.e**(-1*((x-2)**2)/2)/(math.sqrt(2*math.pi))
  x = symbols("x")
  def cdfTuple(x):
    return quad(f, -np.inf, x )
  def cdf(x):
    return cdfTuple(x)[0]
  r = random.uniform(0,1)
  #print("Random: ", r)
  x = float(inversefunc(cdf, y_values = r))
  return x

def randomPower():#Returns one weighted random value according to Power series distribution
  def f(x): #pdf
    return 2*(x**(-3))
  x = symbols("x")
  def cdfTuple(x): #cdf as integral. Integration heuristic has error here I think...
    return quad(f, 1, x )
  def cdf(x):
    return cdfTuple(x)[0]
  def inverseCdf(x):# manually defining inverse through manual computations
    return 1/(math.sqrt(-x+1))
  r = random.uniform(0,1)
  #print("Random: ", r)
  x = inverseCdf(r)

  return x

def sampleN(n):
  randomValues = []
  for x in range(n):
    r = randomGaussian()
    randomValues.append(r)
  return randomValues

def regressionComparison():
  gaussianValueList = []
  gaussianMeanList = []
  gaussianResidualList = []
  for x in range(2000):
    value = randomGaussian()
    gaussianValueList.append(value)
    if x%2 == 0:
      mean = stats.mean(gaussianValueList)
      gaussianMeanList.append(mean)
      gaussianResidualList.append(mean-2)

  powerValueList = []
  powerMeanList = []
  powerResidualList = []
  for x in range(2000):
    value = randomPower()
    powerValueList.append(value)
    if x%2 == 0:
      mean = stats.mean(powerValueList)
      powerMeanList.append(mean)
      powerResidualList.append(mean-2)  
      

x = [x for x in range(0, 2000, 2)]
print(len(x))
print(len(gaussianResidualList))
plt.ylim(-0.3, 0.3)
plt.scatter(x, gaussianResidualList)
plt.scatter(x, powerResidualList)
  
