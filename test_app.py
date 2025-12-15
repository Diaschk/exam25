import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import main
import pytest

def test_sum_progression():

    assert sum([2]) == 2
    
    assert sum([2, 4, 6]) == 12
    
    assert sum([2, 4, 6, 8, 10]) == 30

    assert sum([2, 4, 6, 8, 10, 12]) == 42       
    assert sum([2, 4, 6, 8, 10, 12, 14, 16]) == 72  # 
    
    print("Всі тести пройдені")

if __name__ == "__main__":
    test_sum_progression() 