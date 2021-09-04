# Disaster Response Pipeline Project
<img src="https://user-images.githubusercontent.com/44194994/131757055-72e55b9a-af30-4f01-9ad6-3ad03082c170.jpeg" alt="drawing" width="800"/>

## Table of Contents
 * [Project Motivation](#project-motivation)
 * [File Structure](#file-structure)
 * [Components](#components)
 * [Instructions of Project](#instructions-of-project)
 * [Licensing, Authors, Acknowledgements, etc.](#licensing-authors-acknowledgements-etc)
 
### Project Motivation:

In this project, disaster data were analyzed from Figure Eight to build a model for an API which classifies disaster messages.

The datasets adopted real messages that were sent during disaster events. A machine learning pipline with multi-output classifier were built to categorize these event to reach out for a relevant relief agency. 

The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data.

### File Structure:

	- app
	| - template
	| |- master.html  # main page of web app
	| |- go.html  # classification result page of web app
	|- run.py  # Flask file that runs app

	- data
	|- disaster_categories.csv  # data to process 
	|- disaster_messages.csv  # data to process
	|- process_data.py
	|- DisasterResponse.db   # database to save clean data to

	- models
	|- train_classifier.py # train model
	|- classifier.pkl  # saved model 

	- README.md
    
### Components
There are three components I completed for this project. 

#### 1. ETL Pipeline
A Python script, `process_data.py`, writes a data cleaning pipeline that:

 - Loads the messages and categories datasets
 - Merges the two datasets
 - Cleans the data
 - Stores it in a SQLite database
 
A jupyter notebook `ETL Pipeline Preparation` was used to prepare the process_data.py python script. 
 
#### 2. ML Pipeline
A Python script, `train_classifier.py`, writes a machine learning pipeline that:

 - Loads data from the SQLite database
 - Splits the dataset into training and test sets
 - Builds a text processing (NLP) and machine learning pipeline
 - Trains and tunes a model using GridSearchCV
 - Outputs results on the test set
 - Exports the final model as a pickle file
 
A jupyter notebook `ML Pipeline Preparation` was used to prepare the train_classifier.py python script. 

#### 3. Flask Web App
The project includes a web app where an emergency worker can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

### Instructions of Project:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
        
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

### Example 

Type a message such as: 
![image](https://user-images.githubusercontent.com/44194994/131758567-146c3329-a40b-4039-a7bc-38b0c03dc9e8.png)

![image](https://user-images.githubusercontent.com/44194994/131758687-6cc9a782-d359-492c-9865-75afa840c6d0.png)

![newplot (1)](https://user-images.githubusercontent.com/44194994/131758715-2264456e-baab-4b8a-a7a1-391e9e334f95.png)



### Licensing, Authors, Acknowledgements, etc.
Thanks to Udacity for starter code for the web app. 
