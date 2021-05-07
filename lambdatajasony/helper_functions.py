import pandas as pd
import matplotlib.pyplot as plt
import numpy

""" 

Classes and methods that I will find helpful when exploring and analysing data
    
"""

class NullCount(pd.DataFrame):
    """
    
    A subclass of Pandas DataFrames with a new method attached that returns
    the sum of nulls in all of the cells
    
    """
    def nulls(self, df):
      
      return df.isnull().sum().sum()


class RandomizedDataFrame(pd.DataFrame):
  """
  
  Another subclass with an extra method to quickly shuffle its contents. It occurs
  to me that I should include the nulls method in this one, but that's for the
  weekend
  
  """
  def __init__(self, df, seed = 50):
    self.df = df
    self.randomseed = seed

  def shuffle(self):
    return self.df.sample(frac = 1, replace = False)


class HungryDataFrame:
    """
    An object that takes both a DataFrame and a list with a method to 
    combine them. Useless!
    """

  def __init__(self, listy, df):
    self.listy = listy
    self.df = df

  
  def mutate(self):
    self.df['list'] = pd.Series(self.listy)

    return self.df



def train_test_split(df, frac = 0.2):
    """
    A simple function that splits a DataFrame into a train and test set
    

    Parameters
    ----------
    df : a Pandas DataFrame
        
    frac : the fraction of the DataFrame that goes into the test set. the 
           default is 0.2

    Returns
    -------
    train : A Pandas DataFrame with 1-frac of the data
    
    test : A Pandas DataFrame with frac of the data

    """
    train = df.sample(frac = 1 - frac, replace = False, random_state = 60)
    test = df.drop(train.index)
    
    return train, test



