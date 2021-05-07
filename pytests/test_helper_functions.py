import pytest
import pandas as pd
import numpy
from helper_functions import FriendlyError, train_test_split

def test_friendly_error():
    """
    Test whether the proper error is raised when train_test_split does not 
    receive a DataFrame as an argument
    """
    with pytest.raises(FriendlyError):
        train_test_split('hello')
    
    
