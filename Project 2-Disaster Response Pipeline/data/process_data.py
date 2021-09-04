#import libraries
import sys
import pandas as pd
import numpy as n

import sqlite3
import sqlalchemy
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    Load data from csv files and merge dataset
    
    Parameters:
    messages_filepath: messages csv file
    categories_filepath: categories csv file
    
    Return:
        df: messages and categories merged dataframe
    '''
    #load messages and categories
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    #merge two dataframes into one
    df = messages.merge(categories, how='inner', on= 'id')
    return df



def clean_data(df):
    """
    Clean the dataframe.
    
        1. Rename columns of different categories
        2. Remove Duplicates
        
    Parameters:
        df: DataFrame
        
    Returns: 
        df: messages and categories merged dataframe
    """

    # split the categories columns
    categories = df['categories'].str.split(';', expand = True)

    # select the first row
    row = categories.head(1)
    # create a new columns for categories
    category_colnames = row.applymap(lambda x: x[:-2]).iloc[0,:]
    categories.columns = category_colnames

    # replace original values into 1 and 0
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)

    # replace the categories column
    df.drop('categories', axis = 1, inplace = True)
    df = df.join(categories)
    
    # drop duplicates
    df.drop_duplicates(inplace = True)
    
    # Remove rows with a  value of 2 from df
    df = df[df['related'] != 2]
    return df


def save_data(df, database_filename):
    '''
    save the dataframe to SQLite database
    '''
    # save data into a sqlite database
    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('message', engine, index = False, if_exists = 'replace') 


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()