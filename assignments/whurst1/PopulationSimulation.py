#!/usr/bin/env python		# DB: More robust if you use this shebang. For me, using /usr/bin/python
							# calls v2, but /usr/bin/env python. In this case, it changes the results
import numpy				# because of the way the versions handle conversion of ints to floats.
import numpy.random as NumRan
import matplotlib.pyplot as plot

#choose random offspring rate
Rate= NumRan.poisson(2.0)

#set max pop size
MaxPop= input("Enter the Max Population: ")

#Number of generations to run
Gens= input("Enter the Number of Generations to run: ")
StartPop= input("Enter Starting Pop: ")

#setting
Gens=int(Gens)
MaxPop= int(MaxPop)
Rate= int(Rate)
StartPop= int(StartPop)

num = [StartPop+1]*(Gens+1)

for organisms in range(Gens):
	num[organisms+1] = num[organisms]+(Rate*num[organisms]*(1-(num[organisms]/MaxPop))) 

plot.plot(range(Gens+1),num, "--")
plot.xlabel("Generation")
plot.ylabel("Number")
plot.title("Growth rate: %s, Carrying Capacity =%d" % (Rate, MaxPop))
plot.show()

# the growth rate rarely goes above 1 in the simulation.
# DB: I'm not sure about this. Drawing from a Poisson with lambda=2 should often give
#     growth rates above 1.

# When I try to enter Numpy.random.poisson(2, 10) it gives me:
# "only length-1 arrays can be converted to Python scalars".
# DB: Did you try: sum(NumRan.poisson(2,10))?

# DB: Overall, this looks pretty good. I had been envisioning an individual-level 
#     simulation, where the number of offspring was drawn independently from a Poisson for 
#     each individual. But using the analytical equation should produce a similar result, albeit 
#     with less variation from generation to generation and more variation across runs. The single 
#     value of Rate drawn above will have a large influence on the results.

# DB: Did you include a writeup of the results you observed?