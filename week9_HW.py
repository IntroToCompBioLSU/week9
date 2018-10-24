#!/usr/bin/env python

# Set starting population size.
# Figure out number of offspring per individual with poisson.
# Set a number for carrying capacity.
# Set number of generations to test.
# Create loop that runs through each of the above specifications till number of generations is over.
# Create a plot of population size over time.

# week9 homework assignment, population growth simulation.
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# Variables being used for population growth simulation and setting up user inputs.
numOff = nr.poisson(2.0) #Draw random number of offspring per individual.
startPop = input("Enter the starting population size: ")
numGen = input("Enter the number of generations to test: ")
carCap = input("Enter the carrying capacity for the population: ")

numOff = float(numOff)
startPop = int(startPop) # Starting population.
numGen = int(numGen) # Number of generations.
carCap = int(carCap) # Carrying capacity.

# Set number of individuals in starting population.
num = [startPop]*(numGen+1)

# Logistic growth formula.
# Use for loop with Number of generations.
# Add population change to starting population variable.
for i in range(numGen):
    num[i+1] = num[i] + numOff*num[i] * (1 - num[i]/carCap)

# All simulation data plotted using pyplot.
plt.plot(range(numGen+1), num, color='red')
# Labeling x and y axis and formatting plot.
plt.xlabel("Generations")
plt.ylabel("Population Size")
plt.title("Change in Population Size Over Generations")
txt=("Growth Rate: %s, Carrying Capacity: %d" % (numOff,carCap))
plt.figtext(0.5, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=8, color='red')
plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
plt.show()
