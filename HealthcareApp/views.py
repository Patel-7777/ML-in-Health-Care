from django.shortcuts import render
from .form import DiabeticForm, HeartForm

import pickle

# Create your views here.
def index(request):
    return render(request,'index.html')

def diabetic(request):
    if request.method == 'POST':
        form = DiabeticForm(request.POST)
        if form.is_valid():
            # logic of prediction


            diabetic_model = pickle.load(open(r'D:\Django\Health\Healthcare\diabetic_model.sav', 'rb'))

            Pregnancies = form.cleaned_data['Pregnancies']
            Glucose = form.cleaned_data['Glucose']
            BloodPressure = form.cleaned_data['BloodPressure']
            SkinThickness = form.cleaned_data['SkinThickness']
            Insulin = form.cleaned_data['Insulin']
            BMI = form.cleaned_data['BMI']
            DiabetesPedigreeFunction = form.cleaned_data['DiabetesPedigreeFunction']
            Age = form.cleaned_data['Age']

            diab_prediction = diabetic_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            print(diab_prediction[0])
            if (diab_prediction[0] == 1):
                result = 'The person is diabetic'
            else:
                result = 'The person is not diabetic'
            return render(request,'diabetic.html',{'form':form,'result':result})
    else:
        form=DiabeticForm()
        return render(request,'diabetic.html',{'form':form})

def heart(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            # logic of prediction


            heart_model = pickle.load(open(r'D:\Django\Health\Healthcare\heart_model.sav', 'rb'))

            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            cp = form.cleaned_data['cp']
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            thalach = form.cleaned_data['thalach']
            exang = form.cleaned_data['exang']
            oldpeak = form.cleaned_data['oldpeak']
            slope = form.cleaned_data['slope']
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']

            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
            
            if (heart_prediction[0] == 1):
                result = 'The person is having heart disease'
            else:
                result = 'The person does not have any heart disease'
            return render(request,'heart.html',{'form':form,'result':result})
    else:
        form=HeartForm()
        return render(request,'heart.html',{'form':form})