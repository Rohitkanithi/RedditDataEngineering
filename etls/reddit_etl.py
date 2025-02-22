import sys
import pandas as pd
import numpy as np
import praw
from praw import Reddit

from utils.constants import POST_FIELDS

# Function to connect to Reddit API
def connect_reddit(client_id, client_secret, user_agent):
    try:
        reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent)
        print("Connected to reddit..!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

# Function to extract top Reddit posts from a given subreddit
def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post) # Convert Reddit post object to dictionary
        post = {key: post_dict.get(key, None) for key in POST_FIELDS} # Select only required fields
        post_lists.append(post)
    return post_lists

# Function to transform extracted data
def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s') # Convert timestamp to datetime
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False) # Convert boolean values
    post_df['author'] = post_df['author'].astype(str) # Convert author to string
    edited_mode = post_df['edited'].mode() # Get mode for 'edited' column
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int) # Ensure numeric columns are integers
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str) # Convert title to string
    return post_df

# Function to save transformed data as CSV
def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)