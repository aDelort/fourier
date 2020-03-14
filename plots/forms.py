from django import forms
from django.db import models

class SettingForm(forms.Form):
	nMax = forms.IntegerField(label="Nombre de termes",required=False)
	nbPoints = forms.IntegerField(label="Nombre de points",required=False)
	eachTermPlotted = forms.BooleanField(label="Composantes",required=False)
	tMax = forms.FloatField(label="tMax",required=False)
	a_n = forms.CharField(label='An',required=False)
	b_n = forms.CharField(label='Bn',required=False)