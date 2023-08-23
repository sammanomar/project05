## Dataset Content

- 1 The diabetes dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/nancyalaswad90/review). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a sample was taken from a female patient, each column contains anattribute. The samples are either diabetic or not diabetic.

- 2 The heart disease dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a patient sample, each column contains an attribute. The samples are either have a heart disease or doesn't have any heart disease.


## Business Requirements
- 1 The client is interested in telling whether a given sample taken from a female patient is diabetic or not.
- 2 The client is interested to predict whether a patient has heart disease or not base on 13 features


## Hypothesis and how to validate?
* We suspect that diabetic female patient have high level of glucose in blood.
- An average data study can help to investigate it

* We suspect that heart disease patient have a chest pain and high heart rate.
- An average data study can help to investigate it


## The rationale to map the business requirements to the Data Visualizations and ML tasks

- **Business Requirement 1**: Classification
  - We want to predict if a sample given from female patient makes her diabetic or not.
  - We want to build a binary classifier and generate reports.
  
- **Business Requirement 2**: Classification
  - We want to predict if a sample given from patient make him/her have a heart disease or not
  - We want to build a binary classifier and generate reports.


## ML Business Case

### Diabetes

- We want an ML model to predict if a given sample from a female patient is diabetes or not, based on 8 attributes. It is a supervised model, a 2-class, single-label, classification model.
- Our ideal outcome is to provide the medical team a faster and more reliable diagnostic for diabetes detection.
- The model success metrics are
  - Accuracy of 75% or above on the test set.
- The model output is defined as a flag, indicating if the female patient has diabetes or not and the associated probability of being diabetic or not. The medical staff will do the blood smear workflow as usual and gather the required attributes for the App.
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish between diabetic and non diabetic female patients. A blood smear sample and other attributes are collected and examined in the lab. This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.
- The training data to fit the model comes from the [Kaggle](https://www.kaggle.com/datasets/nancyalaswad90/review).
  - Train data - Outcome: diabetic or not; features: 8 attributes

### Heart Disease

- We want an ML model to predict if a given sample from patient make him/her have a heart disease or not or not, based 13 attributes. It is a supervised model, a 2-class, single-label, classification model.
- Our ideal outcome is to provide the medical team a faster and more reliable diagnostic for heart disease detection.
- The model success metrics are
  - Accuracy of 75% or above on the test set.
- The model output is defined as a flag, indicating if the patient has heart disease or not and the associated probability of suffering from a heart disease or not. The medical staff will do the blood smear workflow as usual and gather the required attributes for the App.
- Heuristics: The current diagnostic needs an experienced staff and detailed inspection to distinguish between healthy and heart disease patients. A blood smear sample and other attributes are collected and examined in the lab. This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.
- The training data to fit the model comes from the [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci).
  - Train data - target: heart disease or not; features: 13 attributes


## Dashboard Design (Streamlit App User Interface)

### Page 1: Diabetes Summary

- Quick project summary
    **General Information**
  - Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.
  - Early diagnosis can be accomplished through relatively inexpensive testing of blood glucose.
  - According to [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria), In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years.
  **Project Dataset**
  - The available dataset contains 768 blood smear. The objective of the dataset is to diagnostically predict whether a patient has diabetes or not based on certain diagnostic measurements included in the dataset. 
  - All patients here are females at least 21 years old.

### Page 2: Heart Disease Summary

- Quick project summary
    **General Information**
  - Heart disease describes a range of conditions that affect the heart. Heart diseases include: Blood vessel disease, such as coronary artery disease. Irregular heartbeats (arrhythmias) Heart problems you're born with (congenital heart) defects
  - This database contains 76 attributes, but all published experiments refer to using a subset of 13 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to this date.
  - According to [WHO](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)#:~:text=Cardiovascular%20diseases%20(CVDs)%20are%20the,%2D%20and%20middle%2Dincome%20countries.), An estimated 17.9 million people died from CVDs in 2019, representing 32% of all global deaths. Of these deaths, 85% were due to heart attack and stroke. Over three quarters of CVD deaths take place in low- and middle-income "countries.
    **Project Dataset**
  - The available dataset contains 303 sample taken and gathered by Cleveland UCI with 13 attribute.

### Page 3: Diabetes Prediction

- Page title
- Table with subheader and the first 5 rows of the training dataset
- Dynamic sidebar sliders represting every single attribute in the dataset
- Bar chart with subheader
- Accuracy score of the test data
- Diabetes test result button
- Business requirement 1 information - "The client is interested in telling whether a given sample taken from a female patient is diabetic or not."

### Page 4: Heart Disease Prediction

- Page title
- Table with subheader and the first 5 rows of the training dataset
- Dynamic sidebar sliders represting every single attribute in the dataset
- Bar chart with subheader
- Accuracy score of the test data
- Heart disease test result button
- Business requirement 2 information - "The client is interested to predict whether a patient has heart disease or not base on 13 features"

## Credits 
* WalkthroughProject01 (Malaria Detector)
* WalkthroughProject01 (churnometer)
* Kaggle website
* Stackoverflow
* Heroku
* bootstrap icons
* WHO
* Streamlit



