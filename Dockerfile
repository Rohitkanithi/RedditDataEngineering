FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

# Modify requirements.txt to change numpy version before installation
RUN sed -i 's/numpy==2.2.3/numpy==2.0.2/' /opt/airflow/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /opt/airflow/requirements.txt
