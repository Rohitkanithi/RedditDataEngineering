from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

# Function to upload extracted Reddit data to AWS S3
def upload_s3_pipeline(ti):
    # Retrieve the file path from previous task using XCom
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    # Connect to AWS S3
    s3 = connect_to_s3()

    # Create the S3 bucket if it does not already exist
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)

    # Upload the file to the S3 bucket
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])
