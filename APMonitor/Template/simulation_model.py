import numpy as np
import random

def equations(x,t):
	dx1 = -0.2 * x[0] + 0.1 * x[2] + np.cos(t)
	dx2 = -0.2 * x[1] + 0.1 * x[0] + np.exp(-0.1*t)+ 0.01
	dx3 = -0.2 * x[2] + 0.2 * x[1] 
	
	return([dx1,dx2,dx3])

x0 = [1.,2.,4.]

time = np.linspace(0,100, num = 1e3)

head = 'time, y1obs, y2obs, last\n'


def observation(x):
	y1 = x[0]
	y2 = x[1] 
	# noisy
	y1noisy = y1 + 0.1 * y1 * random.random()
	y2noisy = y2 + 0.1 * y2 * random.random()

#	return([y1,y2])
	return([y1noisy,y2noisy])
