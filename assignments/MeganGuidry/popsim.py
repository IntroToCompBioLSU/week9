#!/usr/bin/env python
# week 9 homework- population simulation
import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

# assigning variables based on logistic growth formula
r = nr.poisson()
p = input("Starting population size: ")
t = input("Number of generations: ")
K = input("Carrying capacity: ")

r = float(r)
p = int(p) #starting population
t = int(t) #number of generations
K = int(K) #carrying capacity

# Set number of individuals in starting population
num = [p]*(t+1)

# logistic growth formula
# use for loop with number of generation 
# add population change to starting population variable
for i in range(t):
    num[i+1] = num[i] + r*num[i] * (1 - num[i]/K)

# plot results of population simulation using pyplot
plt.plot(range(t+1), num, color='purple')
# labeling axes & formatting
plt.xlabel("Generations")
plt.ylabel("Population Size")
plt.title("Change in Population Size Over Generations")
txt=("Growth Rate: %s, Carrying Capacity: %d" % (r,K))
plt.figtext(0.5, 0.005, txt, wrap=True, horizontalalignment='center', fontsize=8, color='purple')
plt.axvline(numpy.argmax(numpy.diff(num)), color = 'k' )
plt.show()




