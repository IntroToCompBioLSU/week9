#!/usr/bin/env python

#import numpy
import numpy as np
#import numpy random to draw from poisson
import numpy.random
#import matplotlib
import matplotlib.pyplot as plt
#import random
import random

#define the value for the starting number of individuals
StartPop = input("Enter the start number of individuals:")

#list to hold population size
popsizes = []
popsizes.append(StartPop)
r = numpy.random.poisson(1.0)
#Define the carrying capacity
carry = input("Enter the carrying capacity:" )

#define the number of generations
generations = input("Enter the max number of generations:")

#random values for equation
attempt = numpy.random.poisson()
n = [int(StartPop)]*(int(generations)+1)
#define the rate of reproduction using a growth rate equation
#Use a for loop to repeat growth for the population
for offspring in range(int(generations)):
	while attempt < int(generations):
#adding new offspring and counting the generations(attempt)
		n[attempt + 1] = n[attempt] + r*n[attempt]*(1-n[attempt]/int(carry))
		attempt = attempt + 1
#print the generation to screen
		print("Generation:")
		print(attempt)
#print the population size to screen
		print("offspring population:")
		print(n)
#when max generation is reached
	else:
		print("Max generations reached")
		break
#plot the results using matplotlib
plt.xlabel('Generations')
plt.ylabel('number of individuals')
plt.plot(range(int(attempt)+1),n)
plt.show()
