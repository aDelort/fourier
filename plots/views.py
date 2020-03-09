from django.shortcuts import render
import numpy as np
from math import *
import matplotlib.pyplot as plt

# Create your views here.

def A(n):
	return 0

def B(n):
	if n%2:
		return 2/pi/n
	else:
		return 0

def formateXTicks(tMax):
	Tint = list(range(round(-tMax),round(tMax)+1))
	Tstr = []
	for t in Tint:
		if t == 0:
			Tstr.append('0')
		elif t == -1:
			Tstr.append('-T')
		elif t == 1:
			Tstr.append('T')
		else:
			Tstr.append(str(t)+'T')
	return Tint,Tstr

def plotsPage(request):
	#Settings
	nbPoints = 2000
	tMax = 2.2
	nMax = 20
	eachCurvePlot = True
	nMaxPlotted = 10

	#Calculation
	T = np.linspace(-tMax,tMax,nbPoints)
	Y = np.zeros(nbPoints)
	Ycurves = np.zeros((nbPoints,nMax))
	for i in range(nbPoints):
		for n in range(1,nMax+1):
			Ycurves[i,n-1] = A(n)*np.cos(2*pi*n*T[i]) + B(n)*np.sin(2*pi*n*T[i])
			Y[i] += Ycurves[i,n-1]

	#Plots
	plt.figure(figsize=(11,5))
	plt.plot(T,Y,c='#0E2116',linewidth=1, color='white')
	if eachCurvePlot:
		for n in range(1,nMaxPlotted+1):
			if A(n) or B(n):
				plt.plot(T,Ycurves[:,n-1],linewidth=1)
	# plt.title("nMax = {}".format(nMax))
	plt.title(r'$\sum_{n=1}^{n_{max}} A_n cos(2 \pi n t) + B_n sin(2 \pi n t)$',color='white',pad=16)
	plt.grid(True,linestyle='dotted',color='black',markevery=0.1)
	for side in ['top','right']:
		plt.gca().spines[side].set(visible=False)
	for side in ['bottom','left']:
		plt.gca().spines[side].set(color='white')
	plt.gca().tick_params(axis='both', colors='white', which='both')
	Tint,Tstr = formateXTicks(tMax)
	plt.gca().set_xticks(Tint)
	plt.gca().set_xticklabels(Tstr)
	plt.gca().set_yticks([-sqrt(A(1)**2+B(1)**2),0,sqrt(A(1)**2+B(1)**2)])
	C1_latex = r'$\sqrt{A_1^2 + B_1^2}$'
	plt.gca().set_yticklabels(['-'+C1_latex,'0',C1_latex])
	plt.gca().set_xlim([-tMax,tMax])
	plt.tight_layout()
	plt.savefig('plots/static/plots/img/plotting', transparent=True)
	return render(request, 'plots/plotsPage.html', dict())