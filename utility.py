# My utility funtions for Kaggle...
import random as rnd
import os
import numpy as np
import pandas as pd


def seed_everything(seed = 42):
    """ Seed everything function for python """
    rnd.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed) 


def read_csv(path, df_name):
    """ Import a CSV into a Pandas Dataframe based on the specified path """
    df_name = pd.read_csv(path)
    return df_name
    

def describe_categorical(df, sample_fields = 5):
    ''' Describe categoricals datasets, in more details to have ageneral idea of the values on each column '''
    text_variables = []
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df = df.select_dtypes(exclude = numerics)
    for col in df.columns:
        text_variables.append(col)
        pct_valid_data = 1 - (df[col].isnull().sum() / df.shape[0])
        unique_fields = list(set(df[col]))
        print('Variable Name: {:<15} % Data: {:0.2f} # Unique Fields:{:<5} Samples: {}'.format(col,pct_valid_data, len(unique_fields), unique_fields[:sample_fields]))
    return text_variables