from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Define Tasks
def preprocess_data():
    print("Preprocess data.......")

def train_model():
    print("training model.......")

def evaluate_model():
    print("evaluating model.......")

# define DAG
with DAG(
    'my_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@weekly', # Or '0 0 * * 0' for weekly on Sunday at midnight
    # catchup=False, # Prevents backfilling for past missed runs
    tags=['ml', 'training'], # Add relevant tags for easier filtering in UI
) as dag:
    preprocess=PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate = PythonOperator(task_id="evaluate_task", python_callable=evaluate_model)

# set dependencies

preprocess >> train >> evaluate

