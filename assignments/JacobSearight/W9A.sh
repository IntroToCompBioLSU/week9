#!/usr/bin/env python

######## Jacob Searight : Jacobssearight : Biol4800 : Week 9 Assignment : 10.23.18

######## The general idea is to employ a for loop to simulate the logarithmic growth in a population of a Staphylococcus species that's forming a biofilm inside a feeding tube.  
######## to import poisson values and graphing
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt
######## To setup  variables
r = nr.poisson(2)
p = input("Starting population size: ")
t = input("Number of generations: ")
k = input("Carrying capacity: ")
r = float(r)
p = int(p)
t = int(t)
k = int(k)
######## Establishes the starting population
num = [p]*(t+1)
######## As num increases, the last para. will start subtracting more, which will in turn make the poisson contribution decrease. This breaks as the population size or carrying capacity get large. 
for i in range(t):
	num[i+1] = num[i] + r*num[i] * (1 - num[i]/k)
####### To setup graph
plt.plot(range(t+1), num, color='black')
plt.xlabel("Generations")
plt.ylabel("Population Size")
plt.title("Change in Population Size Over Generations")
plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
plt.show()

