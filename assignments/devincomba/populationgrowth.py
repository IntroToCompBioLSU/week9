
#!/usr/bin/env python

#this script simulates population growth of a population

import numpy as np

#currentpop is number of individuals
currentpop = int(input("Initial Population Size:	"))

#carryingcap is maximum number carrying capacity/max number of individuals
carryingcap = int(input("Carrying Capacity of Population:	"))

#gencount is number of generations to be simulated
gencount = int(input("Number of Generations:	"))

#meanoffspring is average number of offspring for each individual, set by the program
meanoffspring = 2

#loop gencount times
for i in range (0,  gencount):
#{
	#show currentpop
	print (currentpop)

	#oldpopoffspring is determined by running Poisson (Mean: meanoffspring, size: currentpop)
	oldpopoffspring = np.random.poisson(meanoffspring, currentpop)

	#currentpop is sum of all oldpop
	currentpop = 0
	for j in oldpopoffspring:
		currentpop = currentpop + j

	#if currentpop > carryingcap, this allows for the population to plateau at carrying capacity
	if currentpop > carryingcap:
		currentpop = carryingcap


#}

