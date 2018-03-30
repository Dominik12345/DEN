import numpy as np

def equations(x,t):
   dx1 = -0.1 * x[0] + 0.2 * x[3] + 1/(1+(t-5)**2)
   dx2 = -0.1 * x[1] + 0.2 * x[0] 
   dx3 = -0.1 * x[2] + 0.2 * x[1] + np.arctan(t)
   dx4 = -0.1 * x[3] + 0.2 * x[2]
	
   return([dx1,dx2,dx3,dx4])

x0 = [1.,0.01,0.01,0.01]

time = np.linspace(0,10)

head = 'time, y1obs, y2obs, y3obs, last\n'

def observation(x):
   y1 = x[0] + x[1] + 2 * x[2]
   y2 = x[1] + 2 * x[2]
   y3 = x[2]
   return([y1,y2,y3])
