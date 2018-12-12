#!/usr/bin/env python

#import numpy and matplot libraries
import numpy.random as nr
import matplotlib.pyplot as plt

#set variable for total population , value shown is initial population
Totalpop=[10]

#set the number of generations
generations=100

#set variable to track number of generations simulated
generationnumber=0

#for loop to simulate population change in the generations
for gen in range(generations):

		#use numpy random to select number of offsprings per individual from the previous generation
        birthrate=nr.poisson(1.1,Totalpop[-1])	# DB: Creative syntax, I like this.
        # DB: Using a lambda just above 1 might be most interesting. When 1, pop'n likely to crash.

		#total all offspring to make up the next generation population
        newpop=sum(birthrate.tolist())	# DB: Is .tolist() even necessary here?
        generationnumber += 1

		#output carrying capacity(500) as the new pop when population reaches carrying capacity.
        if int(newpop)>=500:
                newpop=500
		
		#send the new population to variable Totalpop for the next generation simulation
        Totalpop.append(newpop)

#output total population in all generations and the number of generations simulated
print('Total population in each generation:',Totalpop)
print('Number of generations:',generationnumber)
plt.plot(Totalpop)
plt.show()

# DB: Overall, this looks really good. Did you include a writeup of the results?