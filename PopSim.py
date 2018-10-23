#!/usr/bin/python
#this will rename and import all needed functions
	import matplotlib as plt
	import numpy.random as nr
#this will allow input of carrying cap
	Popsize = int(input("Select the Carrying Cap:   "))
#This will produce an array with average offspring 5 pop size 100
	pop = nr.poisson(lam=5,Popsize)
	print pop
