from django import forms
from django.forms import NumberInput

class DiabeticForm(forms.Form):
    Pregnancies = forms.IntegerField(label='Pregnancies',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    Glucose = forms.IntegerField(label='Glucose', widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    BloodPressure = forms.IntegerField(label='Blood Pressure',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    SkinThickness = forms.IntegerField(label='Skin Thickness',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    Insulin = forms.IntegerField(label='Insulin',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    BMI = forms.FloatField(label='BMI',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    DiabetesPedigreeFunction = forms.FloatField(label='Diabetes Pedigree Function',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    Age =forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))

class HeartForm(forms.Form):
    age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    sex = forms.IntegerField(label='Sex',widget=forms.Select(choices=[(1,"Male"),(0,"Female")],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    cp = forms.IntegerField(label='Chest Pain types',widget=forms.Select(choices=[(0,0),(1,1),(2,2),(3,3)],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    trestbps = forms.IntegerField(label='Resting Blood Pressure',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    chol = forms.IntegerField(label='Serum Cholestoral in mg/dl',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    fbs = forms.IntegerField(label='Fasting Blood Sugar',widget=forms.Select(choices=[(1,"Yes"),(0,"No")],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    restecg = forms.IntegerField(label='Resting Electrocardiographic results',widget=forms.Select(choices=[(0,0),(1,1),(2,2)],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    thalach =forms.IntegerField(label='Max Heart-rate',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    exang = forms.IntegerField(label='Exercise Induced Angina',widget=forms.Select(choices=[(1,"Yes"),(0,"No")],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    oldpeak = forms.FloatField(label='ST depression induced by exercise',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    slope = forms.IntegerField(label='Slope of the peak exercise ST segment',widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    ca = forms.IntegerField(label='Major vessels colored by flourosopy',widget=forms.Select(choices=[(0,0),(1,1),(2,2),(3,3)],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    thal =forms.IntegerField(label='thal',widget=forms.Select(choices=[(0,"Normal"),(1,"Fixed Defect"),(2,"Reversable Defect")],attrs={'style': 'width: 300px;', 'class': 'form-control'}))
