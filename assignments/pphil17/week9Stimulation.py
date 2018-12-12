#!/usr/bin/python	# DB: More robust to use /usr/bin/env python. 

import numpy
import numpy.random as nr
import matplotlib.pyplot as plt

#set important variables such as the total number of generations, and carrying capacity.
r = nr.poisson(1)
k = input("Carrying Capacity: ")
t = input("Set number of generations: ")
p = input("Starting population size: ")

t = int(t)
p = int(p)
k = int(k)
r = float(r)

#We need to set starting number
num = [p]*(t+1)

#change to starting population variable
for i in range(t):
    num[i+1] = num[i]+r*num[i]*(1-num[i]/k)


#Using pyplot (Madplotlib), plot the results of the stimulation (Set up the graph)
plt.plot(range(t+1),num, color='orange')
plt.xlabel("Generation")
plt.ylabel("Population Size")
plt.title("Growth rate: %s, Carrying Capacity = %d" % (r, k))
plt.axvline(numpy.argmax(numpy.diff(num)),  color = "k" )
plt.show()

# DB: Overall, this looks pretty good. I had been envisioning an individual-level 
#     simulation, where the number of offspring was drawn independently from a Poisson for 
#     each individual. But using the analytical equation should produce a similar result, albeit 
#     with less variation from generation to generation and more variation across runs. The single 
#     value of r drawn above will have a large influence on the results.
