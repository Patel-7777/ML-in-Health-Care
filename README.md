# Multiple Disease Predictor
## About
This webapp was developed using Flask Web Framework . The models used to predict the diseases were trained on large Datasets. All the links for datasets and the python notebooks used for model creation are mentioned below in this readme. The webapp can predict following Diseases:
* Diabetes
* Breast Cancer
* Heart Disease
* Kidney Disease
* Liver Disease


## Models giving best Accuracy of Prediction
We have compared accuracy of all the algorithms and then selected the best algorithm for that particular disease.

Disease | Type of Model | Accuracy
--- | --- | ---
Diabetes | Logistic Regression | 80%
Breast Cancer | Naive Bayes | 97.38%
Heart Disease | Logistic Regression | 88.53%
Kidney Disease | Random Forest & Naive Bayes | 100%
Liver Disease | XGBoost | 77.77%

## Steps to run the WebApp in local Computer
**Step-1:** Download the files in the repository.<br>
**Step-2:** Get into the downloaded folder, open command prompt in that directory and install all the dependencies using following command<br>
```python
pip install -r requirements.txt
```
**Step-3:** After successfull installation of all the dependencies, run the following command<br>
```python
python app.py
```

## Dataset Links
All the datasets were used from kaggle.
* [Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
* [Breast Cancer Dataset](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
* [Heart Disease Dataset](https://www.kaggle.com/ronitf/heart-disease-uci)
* [Kidney Disease Dataset](https://www.kaggle.com/mansoordaku/ckdisease)
* [Liver Disease Dataset](https://www.kaggle.com/uciml/indian-liver-patient-records)

