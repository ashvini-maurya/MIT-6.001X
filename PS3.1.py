# PS-3.1
# RADIATION EXPOSURE

def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
	start = int(start)
	stop = int(stop)
	step = float(step)
	exposure = 0
	
	i = start
	for i in range(start, (stop+1)):
		exposure = exposure + f(i) * step
		i += step
		

	return exposure

print radiationExposure(5, 11, 1)


