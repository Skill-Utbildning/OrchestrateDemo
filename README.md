# OrchestrateDemo
Airflow demo and connector templates

To set up and run Airflow:
1. Create a directory for your Airflow project.
2. Create a dags subdirectory and place your DAG file there.
3. Create a logs subdirectory for Airflow logs.
4. Save the docker-compose.yml file in your project directory.
5. Run the following commands:

`docker-compose up -d`

This will start Airflow and its dependencies. The webserver will be accessible at `http://localhost:8080`. The default username and password are both airflow.

Take down with:
`docker-compose down`

Remember to replace `your_oracle_password`, `your_mysql_root_password`, `your_database_name`, `your_mysql_user`, and `your_mysql_password` with appropriate values for your setup
