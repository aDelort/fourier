from django.shortcuts import render
import numpy as np
from math import *
import matplotlib.pyplot as plt
from .forms import SettingForm

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
	def A(n):
		return 0

	def B(n):
		if n%2:
			return 2/pi/n
		else:
			return 0

	#Creating the form
	formDefaultValues = {
	'nMax': 20,
	'nbPoints' :1000,
	'tMax' :2.2,
	'eachTermPlotted': True,
	'a_n' : '0',
	'b_n' : '0'
	}
	form = SettingForm(request.POST or formDefaultValues)

	if form.is_valid():
		nMax = form.cleaned_data['nMax']
		nbPoints = form.cleaned_data['nbPoints']
		eachTermPlotted = form.cleaned_data['eachTermPlotted']
		tMax = form.cleaned_data['tMax']
		a_n = form.cleaned_data['a_n']
		b_n = form.cleaned_data['b_n']
		#def A(n):
		#	return 1/n #eval(form.cleaned_data['a_n'])

		#Default values
		if nMax == None or nMax <= 0:
			nMax = formDefaultValues['nMax']
			form.cleaned_data['nMax'] = nMax
		elif nMax > 100:
			nMax = 100
			form.cleaned_data['nMax'] = nMax
		if nbPoints == None or nbPoints <= 0:
			nbPoints = formDefaultValues['nbPoints']
			form.cleaned_data['nbPoints'] = nbPoints
		if tMax == None or tMax <= 0:
			tMax = formDefaultValues['tMax']
			form.cleaned_data['tMax'] = tMax
		if not a_n:
			a_n = formDefaultValues['a_n']
			form.cleaned_data['a_n'] = a_n
		A = lambda n: eval(a_n)
		if not b_n:
			b_n = formDefaultValues['b_n']
			form.cleaned_data['b_n'] = b_n
		B = lambda n: eval(b_n)

		form = SettingForm(form.cleaned_data)

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
		if eachTermPlotted:
			for n in range(1,nMax+1):
				if A(n) or B(n):
					plt.plot(T,Ycurves[:,n-1],linewidth=1)
		plt.plot(T,Y,c='#0E2116',linewidth=1, color='white')
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

	return render(request,'plots/plotsPage.html',locals())