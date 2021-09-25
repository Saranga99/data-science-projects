

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
st.write("")
st.subheader("Dataset")
st.dataframe(df)

#sub header
st.subheader("Data Description")
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































