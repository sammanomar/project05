## Dataset Content

1- The diabetes dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/nancyalaswad90/review). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a sample was taken from a female patient, each column contains anattribute. The samples are either diabetic or not diabetic.

2- The heart disease dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. Each row represents a patient sample, each column contains an attribute. The samples are either have a heart disease or doesn't have any heart disease.


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


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).


## Deployment
### Heroku

* The App live link is: <https://predict-disease-6e1bbf9de2b5.herokuapp.com>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
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

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

