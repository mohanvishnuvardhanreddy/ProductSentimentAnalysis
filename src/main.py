from preprocess import load_and_clean_data
from analyzer import compute_sentiment
import os

def run_pipeline():
    input_path = os.path.join('data', 'reviews.csv')
    output_path = os.path.join('data', 'analyzed_reviews.csv')
    
    print("🚀 Initializing data ingestion pipeline...")
    df = load_and_clean_data(input_path)
    
    print("🧠 Extracting text sentiment mappings...")
    df['Sentiment'] = df['Cleaned_Review'].apply(compute_sentiment)
    
    # Save the output file
    df.to_csv(output_path, index=False)
    print(f"✅ Analysis complete! Saved file to: {output_path}")
    
    # Display quick summary metrics
    print("\n--- Summary Metrics ---")
    print(df['Sentiment'].value_counts())

if __name__ == '__main__':
    run_pipeline()