import pandas as pd

def load_and_clean_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Handle missing values and lowercase the text for consistency
    df['Cleaned_Review'] = df['Review_Text'].fillna("").str.lower().str.strip()
    return df