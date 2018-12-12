#!/usr/bin/python

#This script expects t and K as whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#Input and Formatting
r = nr.poisson(3.0)		# DB: Might pick a higher rate for the Poisson. By default, it's 1, which often results in 0.
K = input('Enter the Carrying Capacity:')
t = input('Enter the Number of Generations:')
p = input('Enter the Starting Population:')
t = int(t)
K = int(K)
r = float(r)
p = int(p)

#setting start
num = [p]*(t+1)

#logistic growth model equation
for i in range(t): 
    num[i+1] = num[i]+r*num[i]*(1-num[i]/K)

# DB: I had been envisioning an individual-level simulation, where the number of offspring
#     was drawn independently from a Poisson for each individual. But using the analytical
#     equation should produce a similar result, albeit with less variation.

#Plotting results
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (r, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show()

# DB: Overall, looks good! But did you include a short writeup describing the results of 
#     using different parameter values?