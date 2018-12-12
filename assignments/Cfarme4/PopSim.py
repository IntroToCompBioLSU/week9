#!/usr/bin/python

#this will rename and import all needed functions
import matplotlib as plt
import numpy.random as nr

#this will allow input of carrying cap
pop = int(input("Select the PopulationSize:   "))

Gensize = int(input("Select the generationSize:   "))

Carrycap = int(input("Select the carrying Capacuty:   "))

#This will produce an array with average offspring 5 for some gen size
for i in range (0, Gensize):	# DB: Missing colon
		
	print(pop)	# DB: These lines need to be indented inside the for loop

	#To poisson for next generation
	pop = sum(nr.poisson(lam=5.0, size=pop))	# DB: This is all you need here.

	#To prevent pop from exceeding Carrying cap
	if pop > Carrycap:	# DB: Missing colon; Also, comparison should be with Carrycap
		pop = Carrycap	# DB: Needs to be indented inside the if statement; Need to reset to Carrycap

# DB: General framework getting there, but lots of syntax and logic problems. How did you 
#     get this to run in order to get the results included in your writeup?