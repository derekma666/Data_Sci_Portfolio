# import libraries
import sys
import sqlite3
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


# import tokenize
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# import sklearn
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from sklearn.metrics import classification_report

import pickle

nltk.download('punkt')
nltk.download('wordnet')


def load_data(database_filepath):
    """
    Load data from the sqlite databse
    Input:
        database_filepath: database file path
    Output:
        X (DataFrame): message list
        Y (DataFrame): training 
        category_names (List)  
    """
    # load data from database
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table('message',con = engine)
    
    # define features and target
    X = df.message
    Y = df.iloc[:,4:]
    category_names = list(df.columns[4:])
    
    return X, Y, category_names


def tokenize(text):
    """
    Tokenization process, the text data to normalize tokenize text. 
    Input: 
         Text data
    Output:
         List of clean tokens 
    """
    
    #tokenize text
    tokens = word_tokenize(text)
    
    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []    
    for token in tokens:
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_toks = lemmatizer.lemmatize(token).lower().strip()
        clean_tokens.append(clean_toks)
        
    return clean_tokens


def build_model():
    """
    Build ML pipleine using adaboost classifier
    Input:
       None
    Output: 
        cv: Classifier Model
    """
    #pipeline
    pipeline = Pipeline([
    ('vect', CountVectorizer(tokenizer = tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    
    # Gridsearch parameters
    parameters = {
        'clf__estimator__n_estimators' : [50, 100]
    }
    
    #create search object
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=3)
    
    return cv


def evaluate_model(model, X_test, Y_test):
    """
    classification report for the given model 
    Input:
        model: trained model
        X_test: test data for the predication 
        Y_test: true test labels for the X_test data
    Output:
        classification report
    """
    # predict 
    y_pred = model.predict(X_test)
    
    # print the metrics
    for index, column in enumerate(Y_test):
        print(column, classification_report(Y_test[column], y_pred[:, index]))

        
def save_model(model, model_filepath):
    """
    Export a model as a pickle file
    Input:
        model: trained model 
        model_filepath: location to store the model
    Output: None
    """
    pickle.dump(model, open(model_filepath, 'wb'))
    

def main():
    """
    model building, training, evaluation, and saving
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()