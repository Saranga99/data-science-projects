

# import pip
# pip.main(["install","streamlit"])
import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt


#dataset
df=pd.read_csv("diabetes.csv")
df.head()
st.header("Diabetes Detection Application")
st.write("Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.")
image=Image.open("diabetes.jpg")

#image
st.image(image)

#description of the context
st.subheader("Context")
st.write("The datasets consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.")

#dataset
st.subheader("Dataset")
st.write("Dataset : [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database)")

st.subheader("Inspiration")
st.write("Can you build a machine learning model to accurately predict whether or not the patients in the dataset have diabetes or not?")


st.write("")
st.subheader("Dataset")
st.dataframe(df)

#sub header
st.subheader("Data Description (Statistical Context)")
st.write(df.iloc[:,:8].describe())


#outcome dectribution
st.subheader("Destribution of the Target variable in the dataset")
labels = 'Diabetes', 'Non-Diabetes'
diabetes = df.query('Outcome == 1').Outcome.count()
non_diabetes = df.query('Outcome == 0').Outcome.count()
sizes = [diabetes, non_diabetes]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.2f%%',
        startangle=90)
ax1.axis('equal')
fig1 = plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig1)


#machine learning
st.subheader("Machine Learning")
X=df.iloc[:,:8].values
y=df.iloc[:,8].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
model=RandomForestClassifier(n_estimators=500)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)
st.write("Accuracy Score of RandomForestClassifier : ",acc*100," %")

#user inputs
st.subheader("Check Your Diabetes Status")



def user_inputs():
    #st.slider(name , min , max , default)
    preg=st.slider("Pregnancies",0,20,0)
    glu=st.slider("Glucose Level",0,200,0)
    bp=st.slider("Blood Preasure",0,130,0)
    skin=st.slider("Skin Thickness",0,100,0)
    ins=st.slider("Insulin Level",0.0,1000.0,0.0)
    bmi=st.slider("BMI",0.0,70.0,0.0)
    dpf=st.slider("DPF ",0.000,3.000,0.000)
    age=st.slider("Age",0,100,0)


    #inputes for the model
    inputs={"Pregnancies":preg,
            "Glucose Level":glu,
            "Blood Preasure":bp,
            "Skin Thickness":skin,
            "Insulin Level":ins,
            "BMI":bmi,
            "DPF":dpf,
            "Age":age}

    #user inputs as a dataframe
    return pd.DataFrame(inputs,index=["User Inputs"])

#call the function
userInputs=user_inputs()

st.write("Entered User Inputs")
#show the user imput dataframe
st.write(userInputs)


st.subheader("Predictions")

output=model.predict(userInputs)

if output[0]==1:
    st.write("You have Diabetes")
else:
    st.write("You haven't Diabetes")








# #test
# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.model_selection import train_test_split
# from sklearn.decomposition import PCA
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score
# import plotly.express as px



# st.write("""
# # Explore different classifier with BARG dataset
# Which one is the best?
# """)

# dataset_name = "Sentiment"
# classifier_name = st.sidebar.selectbox(
#     'Select classifier',
#     ('KNN', 'SVM', 'Random Forest', "Naive Bayes")
# )





# def add_parameter_ui(clf_name):
#     params = dict()
#     if clf_name == 'SVM':
#         C = st.sidebar.slider('C', 0.01, 10.0)
#         params['C'] = C
#     elif clf_name == 'KNN':
#         K = st.sidebar.slider('K', 1, 15)
#         params['K'] = K
#     elif clf_name == 'Naive Bayes':
#         alpha = st.sidebar.slider('alpha', 0.0, 10.0)
#         params['alpha'] = alpha
#     else:
#         max_depth = st.sidebar.slider('max_depth', 2, 15)
#         params['max_depth'] = max_depth
#         n_estimators = st.sidebar.slider('n_estimators', 1, 500)
#         params['n_estimators'] = n_estimators
#     return params


# params = add_parameter_ui(classifier_name)


# def get_classifier(clf_name, params):
#     clf = None
#     if clf_name == 'SVM':
#         clf = SVC(C=params['C'])
#     elif clf_name == 'KNN':
#         clf = KNeighborsClassifier(n_neighbors=params['K'])
#     elif clf_name == 'Naive Bayes':
#         clf = MultinomialNB(alpha=params['alpha'])
#     else:
#         clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'],
#                                            max_depth=params['max_depth'], random_state=1234)
#     return clf


# clf = get_classifier(classifier_name, params)
# #### CLASSIFICATION ####

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0)

# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)

# acc = accuracy_score(y_test, y_pred)

# st.write(f'Classifier = {classifier_name}')
# st.write(f'Accuracy =', acc)






















