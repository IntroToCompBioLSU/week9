#!/usr/bin/python

import numpy
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
	num[organisms+1] = num[organisms]+Rate*num[organisms]*(1-num[organisms]/MaxPop)

plot.plot(range(Gens+1),num, "--")
plot.xlabel("Generation")
plot.ylabel("Number")
plot.title("Growth rate: %s, Carrying Capacity =%d" % (Rate, MaxPop))
plot.show()

#the growth rate rarely goes above 1 in the simulation. When I try to enter Numpy.random.poisson(2, 10) it gives me:
#"only length-1 arrays can be converted to Python scalars".
