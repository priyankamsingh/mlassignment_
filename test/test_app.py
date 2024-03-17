import pandas as pd
import pytest
from src.data_preprocessing import preprocess_data

#edit this later with other pytest


@pytest.fixture
def sample_data():
    # Create sample data for testing
    data = pd.DataFrame({
        'col1': range(40),  # Assuming there are 40 rows
        'col2': range(40)   # Add more columns if needed
        
    })
    return data

def test_preprocessed_data_shape(sample_data):
    # Preprocess the sample data
    preprocessed_data = preprocess_data(sample_data)
    
    # Check the shape of the preprocessed data
    assert preprocessed_data.shape[0] == 40  #model built on this dimension