from django import forms
from django.db import models

class ComponentsForm(forms.Form):
	nMax = forms.IntegerField(label="nMax",required=False)
	eachTermPlotted = forms.BooleanField(label="Composantes",required=False)

class GraphicForm(forms.Form):
	nbPoints = forms.IntegerField(label="Points",required=False)
	tMax = forms.FloatField(label="Périodes",required=False)
	
class ValuesForm(forms.Form):
	a_n = forms.CharField(label='An',required=False)
	b_n = forms.CharField(label='Bn',required=False)