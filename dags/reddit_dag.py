import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add project root to system path to import custom modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

# Define default arguments for Airflow DAG
default_args = {
    'owner': 'Rohit Kanithi',
    'start_date': datetime(2025, 2, 19) # Set DAG start date
}

# Generate a timestamped filename postfix for storing extracted data
file_postfix = datetime.now().strftime("%Y%m%d")

# Define the DAG
dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily', # Run daily
    catchup=False, # Prevent running past executions
    tags=['reddit', 'etl', 'pipeline']
)

# Task 1: Extract data from Reddit using the Reddit API
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline, # Function to call
    op_kwargs= {
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering', # Subreddit to extract data from
        'time_filter': 'day', # Fetch top posts from the last day
        'limit': 100 # Maximum number of posts to fetch
    },
    dag=dag
)

# Task 2: Upload extracted data to AWS S3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag = dag
)

# Define task execution order: Extract → Upload to S3
extract >> upload_s3