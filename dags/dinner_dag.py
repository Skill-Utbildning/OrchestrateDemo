# Demo exercise together
# Breaking down a "workflow" into "tasks"

# We're going to create a workflow for all the tasks involved in making and consuming dinner.

# (1) Decide what to have for dinner
# (2) Ensure groceries
# -- Check pantry and fridge
# -- shop for groceries
# -- dont shop for groceries

# (3) prepare ingredients
# -- bringing out all the ingredients
# (4) prepare kitchen tools
# -- bringing out all of the necessary utensils

# (5) cook dinner
# -- cutting vegetables
# -- turning on oven
# -- frying pan + boiling pot

# (6) set the table
# (7) serve the food
# (8) eat
# -- have dessert & coffee

# (9) clean up (do dishes and clear table)


# (1) >> (2) >> [(3), (4)] >> (5) >> (7)
# (6) >> (7)
# (7) >> (8) >> (9)


### Python
def log(message):
    print(message)

# tasks
def _decide_dinner():
    log("Deciding what to have for dinner")

def _ensure_groceries():
    log("Ensuring grocery supplies")

def _prepare_ingredients():
    log("Preparing ingredients")

def _prepare_tools():
    log("Preparing kitchen utensils and tools")

def _cook_dinner():
    log("Cooking dinner")

def _set_table():
    log("Setting the table")

def _serve_food():
    log("Serving the food on the set table")

def _eat():
    log("Eating - yum!")

def _clean_up():
    log("Cleaning up :(")


# # Naive execution of tasks in a workflow with no real orchestration
# # runs all tasks in order
# def run_dag():
#     decide_dinner()
#     ensure_groceries()
#     prepare_ingredients()
#     prepare_tools()
#     cook_dinner()
#     set_table()
#     serve_food()
#     eat()
#     clean_up()
### /Naive execution of tasks in a workflow with no real orchestration

### Orchestrating with Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

import datetime as dt

with DAG(
    dag_id="dinner_dag",
    start_date=dt.datetime(2021, 1, 1),
    schedule="@hourly",
    catchup=False
):
    decide_dinner = PythonOperator(
        task_id="decide_dinner",
        python_callable=_decide_dinner
    )

    ensure_groceries = PythonOperator(
        task_id="ensure_groceries",
        python_callable=_ensure_groceries
    )

    prepare_ingredients = PythonOperator(
        task_id="prepare_ingredients",
        python_callable=_prepare_ingredients
    )

    prepare_tools = PythonOperator(
        task_id="prepare_tools",
        python_callable=_prepare_tools
    )

    cook_dinner = PythonOperator(
        task_id="cook_dinner",
        python_callable=_cook_dinner
    )

    set_table = PythonOperator(
        task_id="set_table",
        python_callable=_set_table
    )

    serve_food = PythonOperator(
        task_id="serve_food",
        python_callable=_serve_food
    )

    eat = PythonOperator(
        task_id="eat",
        python_callable=_eat
    )

    clean_up = PythonOperator(
        task_id="clean_up",
        python_callable=_clean_up
    )

    # Dependencies
    decide_dinner >> ensure_groceries >> [prepare_ingredients, prepare_tools] >> cook_dinner >> serve_food
    set_table >> serve_food
    serve_food >> eat >> clean_up

