import pandas as pd

# Test for DataFrame creation
def test_dataframe_creation():
    df = pd.read_csv('./costco_ca_ratings_reviews.csv')
    assert isinstance(df, pd.DataFrame)

# Test for the shape of the DataFrame
def test_dataframe_shape():
    df = pd.read_csv('./costco_ca_ratings_reviews.csv')
    assert df.shape == (18027, 10)

# Test for the average_ratings_per_sku calculation
def test_average_ratings_per_sku():
    df = pd.read_csv('./costco_ca_ratings_reviews.csv')
    average_ratings_per_sku = df.groupby('sku')['average_ratings'].mean()
    
    # Add your specific assertions for average_ratings_per_sku here
    assert isinstance(average_ratings_per_sku, pd.Series)
    assert len(average_ratings_per_sku) > 0

# Run the tests
if __name__ == '__main__':
    test_dataframe_creation()
    test_dataframe_shape()
    test_average_ratings_per_sku()
