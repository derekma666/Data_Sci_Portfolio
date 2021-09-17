# Sparkify: Predicting Churn for a Music Streaming Service

## Installations
 - NumPy
 - Pandas
 - Seaborn
 - Matplotlib
 - PySpark SQL
 - PySpark ML

## Project Motivation
Customer churn is the measure of how many customers stop using a service. This type of churn is very bad for business. In this project, we will identify which customers are most likely to churn. As decision-makers at music streaming service providers, Sparkify, we would like to understand the contributing factors of churning behaviors - that will serve as the primary objective of our project. In addition, we will predict customer churn using the history of customer interactions. Proactive actions suggested by predictive models can be taken to retain their customers and save company's revenue.

The project involved:
 - Loading and cleaning a small subset (128MB) of a full dataset available (12GB)
 - Exploratory Data Analysis to understand the data and what features are useful for predicting churn
 - Feature Engineering to create features that will be used in the modelling process
 - Modelling using machine learning algorithms

## File Descriptions
There is one exploratory notebook and html file of the notebook available here to showcase my work in predicting churn.

## Medium Blog Post
The main findings of the code can be found at the Medium Blog post available [here](https://derekma666.medium.com/churn-prediction-in-sparkify-with-pyspark-2b1ad45db989) explaining the details. 

It can be found that the linear SVM model and Naive Bayes obtained the highest F1 score and accuracy. The Naive Bayes model is the most effecient model in this project. In addition, a Random Forest Classifier was chosen to further tune, which is evaluated by F1 score and accuracy metrics. The final model achieved an F1 of 0.77.


## Licensing, Authors, Acknowledgements, etc.
I'd like to acknowledge Udacity for the project idea and workspace.
