#!/usr/bin/python

# t(number of generations) and K(carrying capacity) must be whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
#set imput for population formula with starting population, generations and max capacity. 
r = nr.poisson()
K = input('Set Carrying Capacity:')
t = input('Set Number of Generations:')
p = input('Set Starting Population:')
t = int(t)
K = int(K)
r = float(r)
p = int(p)
#set starting number and popultion
num = [p]*(t+1)
#log. growth population equation model 
for i in range(t): 
    num[i+1] = num[i]+r*num[i]*(1-num[i]/K)
# graphing results with plot
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (r, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show() 
