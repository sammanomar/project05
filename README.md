## Dataset Content

- 1 The diabetes dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/nancyalaswad90/review). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a sample was taken from a female patient, each column contains anattribute. The samples are either diabetic or not diabetic.

- 2 The heart disease dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a patient sample, each column contains an attribute. The samples are either have a heart disease or doesn't have any heart disease.


## Business Requirements
- 1 The client is interested in telling whether a given blood sample taken from a female patient is diabetic or not.
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
  - Diabetes is a chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.
  - Early diagnosis can be accomplished through relatively inexpensive testing of blood glucose.
  - According to [WHO](https://www.who.int/news-room/fact-sheets/detail/malaria), In 2014, 8.5% of adults aged 18 years and older had diabetes. In 2019, diabetes was the direct cause of 1.5 million deaths and 48% of all deaths due to diabetes occurred before the age of 70 years.
    **Project Dataset**
  - The available dataset contains 768 blood smear. The objective of the dataset is to diagnostically predict whether a patient has diabetes or not based on certain diagnostic measurements included in the dataset.
  - All patients here are females at least 21 years old.

### Page 3: Malaria Detector

- Business requirement 2 information - "The client is interested in telling whether a given cell contains a malaria parasite or not."
- Link to download a set of parasite-contained and uninfected cell images for live prediction.
- User Interface with a file uploader widget. The user should upload multiple malaria cell images. It will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated with this statement.
- Table with the image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- Block for each project hypothesis, describe the conclusion and how you validated it.


## Deployment
### Heroku

* The App live link is: <https://predict-disease-6e1bbf9de2b5.herokuapp.com>
* Set the runtime.txt Python version to python-3.9.17 [all stacks](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* 



