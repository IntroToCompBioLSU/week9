#!/usr/bin/python		# DB: More robust to use /usr/bin/env python

# t(number of generations) and K(carrying capacity) must be whole numbers
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

#set input for population formula with starting population, generations and max capacity. 
r = nr.poisson(2.0)	# DB: I'd suggest using a poisson with a lambda higher than 1.
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

# DB: Overall, this looks pretty good. I had been envisioning an individual-level 
#     simulation, where the number of offspring was drawn independently from a Poisson for 
#     each individual. But using the analytical equation should produce a similar result, albeit 
#     with less variation from generation to generation and more variation across runs. The single 
#     value of r drawn above will have a large influence on the results.

# DB: Did you include a writeup of the results you observed?