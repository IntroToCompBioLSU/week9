#!/usr/bin/python
#This script expects t and K as whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
#Input and Formatting
r = nr.poisson()
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
#Plotting results
plt.plot(range(t+1),num, 'b')
plt.xlabel('Generation')
plt.ylabel('Number')
plt.title('Growth rate: %s, Carrying Capacity = %d' % (r, K))
plt.axvline(np.argmax(np.diff(num)),  color = 'k' )
plt.show()