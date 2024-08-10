from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Importing the task functions
from extract_air_pollution import extract_air_pollution
from transform import transform_data
from load import load_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'pollution_air_dags',
    default_args=default_args,
    description='ETL DAG for CSV files to pollution air',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

def extract_data_task(**kwargs):
    ti = kwargs['ti']
    data = extract_air_pollution()
    ti.xcom_push(key='extracted_data', value=data)

def transform_data_task(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(key='extracted_data', task_ids='extract_air_pollution')
    transformed_data = transform_data(data)
    ti.xcom_push(key='transformed_data', value=transformed_data)

def load_data_task(**kwargs):
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(key='transformed_data', task_ids='transform_data')
    load_data(transformed_data)

# Define the tasks with unique names

extract_task = PythonOperator(
    task_id='extract_air_pollution',
    python_callable=extract_data_task,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data_task,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data_task,
    provide_context=True,
    dag=dag,
)

# Set the task dependencies
extract_task >> transform_task >> load_task
