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
    """ Import a CSV into a pandas df based on the specified path """
    df_name = pd.read_csv(path)
    return df_name
    