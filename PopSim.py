#!/usr/bin/python
#this will rename and import all needed functions
import matplotlib as plt

import numpy.random as nr

#this will allow input of carrying cap
Popsize = int(input("Select the PopulationSize:   "))

Gensize = int(input("Select the generationSize:   "))

Carrycap = int(input("Select the carrying Capacuty:   "))


#This will produce an array with average offspring 5 for some gen size
for i in range (0, Gensize) 
pop = nr.poisson(lam=5.0, size=Popsize)
print(pop)

#To poisson for next generation
nextpop = 0
nextpop += nr.poisson(lam=5.0, size=pop)

#To prevent pop from exceeding Carrying cap
	if nextpop > lam=5.0
	nextpop = lam=5.0
