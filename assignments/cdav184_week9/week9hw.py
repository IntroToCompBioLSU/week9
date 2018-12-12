#!/usr/bin/env python
# week 9 homework assignment for population simulation
# Set a starting population
# Give a number for carrying capacity 
# Give a number for the amounts of generations you wish to test
# Figure out the number of offsprings per individual through the use of poisson
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# assigning the variables for population growth simulation
# set up user inputs
numberOff = nr.poisson(2.0) #Draw random number of offspring for each individual
initialPop = input("Enter starting population size: ")
numberGen = input("Enter number of generations: ")
carryingCap = input("Enter carrying capacity: ")

numberOff = float(numberOff)
initialPop = int(initialPop) #starting population
numberGen = int(numberGen) #number of generations
carryingCap = int(carryingCap) #carrying capacity

# Set number of individuals in starting population
num = [initialPop]*(numberGen+1)

# logistic growth formula
# use for loop with number of generations 
# add population change to starting population variable
for i in range(numberGen):
    num[i+1] = num[i] + numberOff*num[i] * (1 - num[i]/carryingCap)

# DB: I had been envisioning an individual-level simulation, where the number of offspring
#     was drawn independently from a Poisson for each individual. But using the analytical
#     equation should produce a similar result, albeit with less variation.

# simulation data plotted by using pyplot
plt.plot(range(numberGen+1), num, color='green')
# labeling the x and y axis & formatting the plot
plt.xlabel("Generations")
plt.ylabel("Population Size")
plt.title("Change in Population Size Over Generations")
txt=("Growth Rate: %s, Carrying Capacity: %d" % (numberOff,carryingCap))
plt.figtext(0.5, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=8, color='green')
plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
plt.show()

# DB: Overall, looks good! But did you include a short writeup describing the results of 
#     using different parameter values?