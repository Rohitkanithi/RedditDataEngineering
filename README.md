# Reddit Data Engineering Pipeline

## **Overview**
This project is an **ETL (Extract, Transform, Load) pipeline** that automates data extraction from Reddit using Apache Airflow and AWS services. The pipeline extracts Reddit posts using **Reddit API**, transforms the data, and stores it in an **AWS S3 bucket** for further analysis using **AWS Glue, Athena, and Redshift**. The data is then visualized using **Looker, Tableau, and Power BI**.

## **Architecture**

![image](https://github.com/user-attachments/assets/865bbf04-a2c8-45b1-857d-a4d7557f4b5c)


The pipeline consists of the following components:

1. **Apache Airflow (Orchestrator)** - Manages and schedules ETL tasks.
2. **Reddit API (Data Source)** - Extracts subreddit data using Reddit API.
3. **AWS S3 (Storage Layer)** - Stores raw and transformed data.
4. **AWS Glue (Data Processing)** - Cleans and transforms data.
5. **AWS Athena (Querying Engine)** - Enables SQL-based analysis.
6. **AWS Redshift (Data Warehouse)** - Stores structured data for advanced analytics.
7. **Visualization Tools** - Looker, Power BI, Tableau for data insights.


## **Pipeline Flow**
1. **Extract Data**: Airflow fetches top Reddit posts from a specific subreddit.
2. **Transform Data**: Cleans and processes the extracted data.
3. **Load Data**:
   - Stores the transformed data in an AWS S3 bucket.
   - AWS Glue processes and moves data to AWS Redshift.
   - AWS Athena is used to query S3 data for quick insights.
4. **Visualization**: The data is accessed via Looker, Power BI, and Tableau.

### **1. Clone the Repository**
```
https://github.com/Rohitkanithi/RedditDataEngineering.git
```

## **Create a virtual environment**
```
python3 -m venv venv
```

## **Set Up Environment Variables**
- Update config/config.conf with Reddit API keys, AWS credentials, and database connection details.

## **Install Dependencies**
```
pip install -r requirements.txt
```

## **Build and Run Airflow with Docker**
```
docker-compose up --build
```

This will start:
   - Apache Airflow (Web UI on localhost:8080)
   - PostgreSQL (Airflow metadata database)
   - Redis (Celery backend)

## **Initialize Airflow Database**
```
docker exec -it airflow-webserver airflow db init
docker exec -it airflow-webserver airflow db upgrade
docker exec -it airflow-webserver airflow users create --username admin --firstname admin --lastname admin --role Admin --email airflow@airflow.com --password admin
```

## **Run the DAG**
Open Airflow UI at http://localhost:8080
Enable and trigger etl_reddit_pipeline

## **Technologies Used**
* Programming Languages: Python
* Workflow Orchestration: Apache Airflow
* Cloud Services: AWS (S3, Glue, Athena, Redshift)
* Database: PostgreSQL (Airflow Metadata)
* Infrastructure: Docker, Docker Compose
* Visualization: Looker, Tableau, Power BI
