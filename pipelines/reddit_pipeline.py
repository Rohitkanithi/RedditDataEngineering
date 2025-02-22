import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

# Function to orchestrate the Reddit ETL process
def reddit_pipeline(file_name: str, subreddit: str, time_filter= 'day', limit= None):
    # Connect to Reddit API
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    # Extract posts from specified subreddit
    posts = extract_posts(instance, subreddit, time_filter, limit)

    # Convert extracted data to Pandas DataFrame
    post_df = pd.DataFrame(posts)

    # Apply transformations
    post_df = transform_data(post_df)

    # Define the output file path
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'

    # Save the transformed data to CSV
    load_data_to_csv(post_df, file_path)

    return file_path