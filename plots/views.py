from django.shortcuts import render
import numpy as np
from math import *
import matplotlib.pyplot as plt

# Create your views here.

def A(n):
	if n == 0:
		return 1/2
	else:
		return 0

def B(n):
	if n%2:
		return 2/pi/n
	else:
		return 0

def plotsPage(request):
	#Settings
	nbPoints = 2000
	tMax = 2
	n_max = 20

	#Calculation
	T = np.linspace(-tMax,tMax,nbPoints)
	Y = []
	for t in T:
		Y.append(0)
		for n in range(n_max+1):
			Y[-1] += A(n)*np.cos(2*pi*n*t) + B(n)*np.sin(2*pi*n*t)

	#Plots
	plt.plot(T,Y,c='green')
	plt.title("nMax = {}".format(n_max))
	plt.savefig('plots/static/plots/img/plotting')
	return render(request, 'plots/plotsPage.html', {'n_max': n_max})