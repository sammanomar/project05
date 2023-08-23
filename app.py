import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# loading the saved models

diabetes_model = pickle.load(open(
    'models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    'models/heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('Diseases Prediction System',

                           ['Diabetes Summary',
                            'Heart Disease Summary',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',],
                           icons=['cast', 'cast',  'activity', 'heart'],
                           default_index=0)
    st.write("This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.")


# Summary Page
if (selected == 'Diabetes Summary'):
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or "
        f"when the body cannot effectively use the insulin it produces.\n"
        f"* Early diagnosis can be accomplished through relatively inexpensive testing of blood glucose.\n"
        f"* According to [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria), "
        f"In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause "
        f"of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 768 blood smear. The objective of the dataset is to diagnostically predict "
        f"whether a patient has diabetes or not based on certain diagnostic measurements included in the dataset. "
        f"All patients here are females at least 21 years old.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/sammanomar/project05/blob/main/README.md).")

    st.success(
        f"The project has 1 business requirements:\n"
        f"* 1 - The client is interested in telling whether a given blood sample taken from a patient is diabetic or not. "
    )
if (selected == 'Heart Disease Summary'):
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Heart disease describes a range of conditions that affect the heart. Heart diseases include: Blood vessel "
        f" disease, such as coronary artery disease. Irregular heartbeats (arrhythmias) Heart problems you're born with "
        f"(congenital heart defects)\n"
        f"* This database contains 76 attributes, but all published experiments refer to using a subset of 13 of them. "
        f"In particular, the Cleveland database is the only one that has been used by ML researchers to this date.\n"
        f"* According to [WHO](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)#:~:text=Cardiovascular%20diseases%20(CVDs)%20are%20the,%2D%20and%20middle%2Dincome%20countries.), "
        f"An estimated 17.9 million people died from CVDs in 2019, representing 32% of all global deaths. Of these deaths, "
        f"85% were due to heart attack and stroke. Over three quarters of CVD deaths take place in low- and middle-income "
        f"countries.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 303 sample taken and gathered by Cleveland UCI with 13 attribute.")
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/sammanomar/project05/blob/main/README.md).")

    st.success(
        f"The project has 1 business requirements:\n"
        f"* 1 - The client is interested to predict whether a patient has heart disease or not."
    )

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')
    

    # getting the input data from the user

    Pregnancies=st.sidebar.slider('Number of Pregnancies', 0, 17, 3)

    Glucose=st.sidebar.slider('Glucose Level', 0, 200, 120)

    BloodPressure=st.sidebar.slider('Blood Pressure value', 0, 122, 70)

    SkinThickness=st.sidebar.slider('Skin Thickness value', 0, 100, 20)

    Insulin=st.sidebar.slider('Insulin Level', 0, 846, 79)

    BMI=st.sidebar.slider('BMI value', 0, 67, 20)

    DiabetesPedigreeFunction=st.sidebar.slider(
        'Diabetes Pedigree Function value', 0.0, 2.4, 0.47)

    Age=st.sidebar.slider('Age of the Person', 21, 81, 33)

    # code for Prediction
    diab_diagnosis=''

    # loading the diabetes dataset to a pandas DataFrame
    diabetes_dataset=pd.read_csv('dataset/diabetes.csv')

    # printing the first 5 rows of the dataset
    st.subheader('Training Data')
    st.write(diabetes_dataset.head())

    # chart visualisations
    st.subheader('Visualisations')
    st.bar_chart(diabetes_dataset)

    # separating the data and labels
    X=diabetes_dataset.drop(columns='Outcome', axis=1)
    Y=diabetes_dataset['Outcome']

    # Splitting the Data into Training data & Test Data
    X_train, X_test, Y_train, Y_test=train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=2)

    # train the model
    classifier=svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)

    # accuracy score on the test data
    X_test_prediction=classifier.predict(X_test)
    test_data_accuracy=accuracy_score(X_test_prediction, Y_test)
    st.write('Accuracy score of the test data : ', test_data_accuracy)

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    age=st.sidebar.slider('Age', 29, 77, 54)

    sex=st.sidebar.slider('Sex: 1 = male; 0 = female', 0, 1)

    cp=st.sidebar.slider('Chest Pain types', 0, 3, 1)

    trestbps=st.sidebar.slider('Resting Blood Pressure', 94, 200, 132)

    chol=st.sidebar.slider('Serum Cholestoral in mg/dl', 126, 564, 246)

    fbs=st.sidebar.slider('Fasting Blood Sugar > 120 mg/dl', 0, 1)

    restecg=st.sidebar.slider(
        'Resting Electrocardiographic results', 0, 2, 1)

    thalach=st.sidebar.slider(
        'Maximum Heart Rate achieved', 71, 202, 150)

    exang=st.sidebar.slider('Exercise Induced Angina', 0, 1)

    oldpeak=st.sidebar.slider(
        'ST depression induced by exercise', float(0), float(6.2), float(1))

    slope=st.sidebar.slider(
        'Slope of the peak exercise ST segment', 0, 2, 1)

    ca=st.sidebar.slider('Major vessels colored by flourosopy', 0, 4, 1)

    thal=st.sidebar.slider(
        'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', 0, 3, 2)

    # code for Prediction
    heart_diagnosis=''

    # loading the csv data to a Pandas DataFrame
    heart_data=pd.read_csv('dataset/heart.csv')

    # print first 5 rows of the dataset
    st.subheader('Training Data')
    st.write(heart_data.head())

    # chart visualisations
    st.subheader('Visualisations')
    st.bar_chart(heart_data)

    # splitting the Features and Target
    X=heart_data.drop(columns='target', axis=1)
    Y=heart_data['target']

    # splitting the Data into Training data & Test Data
    X_train, X_test, Y_train, Y_test=train_test_split(
        X, Y, test_size=0.2, stratify=Y, random_state=2)

    # model training
    model=LogisticRegression()
    # training the LogisticRegression model with Training data
    model.fit(X_train, Y_train)

    # accuracy score on the test data
    X_test_prediction=model.predict(X_test)
    test_data_accuracy=accuracy_score(X_test_prediction, Y_test)
    st.write('Accuracy score of the test data : ', test_data_accuracy)

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis='The person is having heart disease'
        else:
            heart_diagnosis='The person does not have any heart disease'

    st.success(heart_diagnosis)
