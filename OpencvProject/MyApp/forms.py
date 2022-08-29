from MyApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from django.conf import settings


class CriminalsSearchForm(forms.ModelForm):
	
	criminals = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Name'})

	)
	


	class Meta:
		model = Records
		fields =['criminals']
class AllCriminalsSearchForm(forms.ModelForm):
	
	name = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Name'})

	)
	


	class Meta:
		model = Criminals
		fields =['name']
class AddCriminalForm(forms.ModelForm):
	
	name = forms.CharField(
		required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Name'})

	)
	residence = forms.CharField(
		required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Residence'})

	)

	education = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Education Level'})

	)
	occupation = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal occupation '})

	)
	marital_status = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Marital Status'})

	)
	 	


	class Meta:
		model = Criminals
		fields = '__all__'


class UpdateCriminalForm(forms.ModelForm):
	
	name = forms.CharField(
		required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Name'})

	)
	residence = forms.CharField(
		required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Residence'})

	)

	education = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal Education Level'})

	)
	occupation = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Criminal occupation '})

	)
	marital_status = forms.CharField(
		#required=True,
		#label=False,
		widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Marital Status'})

	)
	 	


	class Meta:
		model = Criminals
		fields = '__all__'



class AddCriminalRecordsForm(forms.ModelForm):
	
	# criminals = forms.CharField(
	# 	required=True,
	# 	#label=False,
	# 	widget=forms.TextInput(attrs={'id' :'criminal_name', 'placeholder' : 'Enter Criminal Name'})

	# )
	
	 	


	class Meta:
		model = Records
		fields = '__all__'

class UpdateCriminalRecordsForm(forms.ModelForm):
	
	# criminals = forms.CharField(
	# 	required=True,
	# 	#label=False,
	# 	widget=forms.TextInput(attrs={'id' :'criminal_name', 'placeholder' : 'Enter Criminal Name'})

	# )
	
	 	


	class Meta:
		model = Records
		fields = '__all__'