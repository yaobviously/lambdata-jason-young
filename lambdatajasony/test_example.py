from random import randint
import pytest
from example import increment, COLORS 

def test_increment():
    """ testing increment function """
    assert increment(3) == 5
