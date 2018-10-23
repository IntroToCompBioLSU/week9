#!/usr/bin/env python
import numpy as np  
###

# currentPopulation <- number of individuals
currentPopulation = int(input("Initial Population Size: "))

# carryingCapacity <- maximum number of individuals
carryingCapacity = int(input("Population Carying Capacity: "))

# generationCount <- number of generations to be simulated
generationCount = int(input("Number of generations: "))

# meanOffspring <- avg number of offspring for each individual
meanOffspring = 2

# loop generationCount times
for i in range (0, generationCount): 
#{
# showcurrentPopulation
	print (currentPopulation)
 #oldPopulationOffspring <- Poisson(mean:meanOffspring, size: currentPopulation)
	oldPopulationOffspring = np.random.poisson(meanOffspring, currentPopulation)
# currentPopulation <- sum of all oldPopulationOffspring
	currentPopulation = 0
	for j in oldPopulationOffspring:
		currentPopulation = currentPopulation + j
#if currentPopulation > carryingCapacity
	if currentPopulation > carryingCapacity:
		currentPopulation=carryingCapacity 
#{
# nextPopulation <- carryingCapacity
	#}
#}
#currentPopulation <- nextPopulation
#}
#}
