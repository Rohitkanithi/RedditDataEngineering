FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

# Explicitly uninstall any existing OpenLineage version and install the correct one
RUN pip uninstall -y apache-airflow-providers-openlineage && \
    pip install --upgrade apache-airflow-providers-openlineage>=1.8.0

# Ensure numpy installs the correct version before requirements.txt
RUN sed -i 's/numpy==2.2.3/numpy==2.0.2/' /opt/airflow/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /opt/airflow/requirements.txt