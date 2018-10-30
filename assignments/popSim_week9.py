#!/usr/bin/env python
import numpy as np

# currentPop --  number of individuals to start simulation with
currentPopulation = int(input("Input population size: " ))

# set carrying capacity
carryingCapacity = int(input("Input carrying capacity: "))

#generationCount -- number of generations to run in the simulation
generationCount = int(input("Number of generations to run: "))

# meanOffspring -- avg number of offpsing per each individual
meanOffspring = 2

# for loop that runs through generations
for i in range (0, generationCount):

# show current population
	print(currentPopulation)

#oldPopulationOffspring -- Poisson (mean: meanOffspring, size: current
# population)
	oldPopulationOffspring = np.random.poisson(meanOffspring, currentPopulation)

# currentPopulation -- sum of all (will loop back around and add each new poisson)
	currentPopulation = 0
	for x in oldPopulationOffspring:
		currentPopulation = currentPopulation + x

# if statement for if --> currentPopulation > carryingCapacity
	if currentPopulation > carryingCapacity:
	# spits out carrying capacity rather than a greater integer
		currentPopulation = carryingCapacity
