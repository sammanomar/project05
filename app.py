import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open(
    'models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    'models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(
    'models/parkinsons_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('Diseases Prediction System',

                           ['Project Summary',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Summary Page
if (selected == 'Project Summary'):
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Malaria is a parasitic infection transmitted by the bite of infected female "
        f"Anopheles mosquitoes.\n"
        f"* A blood smear sample is collected, mixed with a reagent and examined in "
        f"the microscope. Visual criteria are used to detect malaria parasites.\n"
        f"* According to [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria), "
        f"in 2019, there were an estimated  229 million cases of malaria worldwide and an "
        f"estimated 409 thousand deaths due to this disease. "
        f"Children <5 years are the most vulnerable group, accounting for 67% (274 thousand) "
        f"of all malaria deaths worldwide in 2019.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 5643 out of +27 thousand images taken from "
        f"blood smear workflow (when a drop of blood is taken on a glass slide) of "
        f"malaria-parasitised and uninfected cells.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cell visually.\n"
        f"* 2 - The client is interested in telling whether a given cell contains a malaria parasite or not. "
    )

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user

    Pregnancies = st.sidebar.slider('Number of Pregnancies', 0, 17, 3)

    Glucose = st.sidebar.slider('Glucose Level', 0, 200, 120)

    BloodPressure = st.sidebar.slider('Blood Pressure value', 0, 122, 70)

    SkinThickness = st.sidebar.slider('Skin Thickness value', 0, 100, 20)

    Insulin = st.sidebar.slider('Insulin Level', 0, 846, 79)

    BMI = st.sidebar.slider('BMI value', 0, 67, 20)

    DiabetesPedigreeFunction = st.sidebar.slider(
        'Diabetes Pedigree Function value', 0.0, 2.4, 0.47)

    Age = st.sidebar.slider('Age of the Person', 21, 81, 33)

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    age = st.sidebar.slider('Age', 29, 77, 54)

    sex = st.sidebar.slider('Sex', 0, 1)

    cp = st.sidebar.slider('Chest Pain types', 0, 1, 3)

    trestbps = st.sidebar.slider('Resting Blood Pressure', 94, 132, 200)

    chol = st.sidebar.slider('Serum Cholestoral in mg/dl', 126, 246, 564)

    fbs = st.sidebar.slider('Fasting Blood Sugar > 120 mg/dl', 0, 1)

    restecg = st.sidebar.slider(
        'Resting Electrocardiographic results', 0, 1, 2)

    thalach = st.sidebar.slider(
        'Maximum Heart Rate achieved', 71, 150, 202)

    exang = st.sidebar.slider('Exercise Induced Angina', 0, 1)

    oldpeak = st.sidebar.slider(
        'ST depression induced by exercise', float(0), float(1), float(6.2))

    slope = st.sidebar.slider(
        'Slope of the peak exercise ST segment', 0, 1, 2)

    ca = st.sidebar.slider('Major vessels colored by flourosopy', 0, 1, 4)

    thal = st.sidebar.slider(
        'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', 0, 2, 3)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    fo = st.sidebar.slider('MDVP:Fo(Hz)', 88.333, 154.229, 260.105)

    fhi = st.sidebar.slider('MDVP:Fhi(Hz)', 102.145, 197.105, 592.030)

    flo = st.sidebar.slider('MDVP:Flo(Hz)', 65.476, 116.325, 239.170)

    Jitter_percent = st.sidebar.slider(
        'MDVP:Jitter(%)', 0.00168, 0.00622, 0.03316)

    Jitter_Abs = st.sidebar.slider(
        'MDVP:Jitter(Abs)', 0.00001, 0.00004, 0.00026)

    RAP = st.sidebar.slider('MDVP:RAP', 0.00068, 0.00331, 0.02144)

    PPQ = st.sidebar.slider('MDVP:PPQ', 0.00092, 0.00345, 0.01958)

    DDP = st.sidebar.slider('Jitter:DDP', 0.00204, 0.00992, 0.06433)

    Shimmer = st.sidebar.slider(
        'MDVP:Shimmer', 0.00954, 0.02971, 0.11908)

    Shimmer_dB = st.sidebar.slider(
        'MDVP:Shimmer(dB)', 0.085, 0.282, 1.302)

    APQ3 = st.sidebar.slider('Shimmer:APQ3', 0.00455, 0.01566, 0.05647)

    APQ5 = st.sidebar.slider('Shimmer:APQ5', 0.0057, 0.01788, 0.0794)

    APQ = st.sidebar.slider('MDVP:APQ', 0.00719, 0.02408, 0.13778)

    DDA = st.sidebar.slider('Shimmer:DDA', 0.01364, 0.04699, 0.16942)

    NHR = st.sidebar.slider('NHR', 0.00065, 0.02485, 0.31482)

    HNR = st.sidebar.slider('HNR', 8.441, 21.886, 33.047)

    RPDE = st.sidebar.slider('RPDE', 0.256570, 0.498536, 0.685151)

    DFA = st.sidebar.slider('DFA', 0.574282, 0.718099, 0.825288)

    spread1 = st.sidebar.slider('spread1', -7.964984, -5.684397, -2.434031)

    spread2 = st.sidebar.slider('spread2', 0.006274, 0.226510, 0.450493)

    D2 = st.sidebar.slider('D2', 1.423287, 2.381826, 3.671155)

    PPE = st.sidebar.slider('PPE', 0.044539, 0.206552, 0.527367)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
