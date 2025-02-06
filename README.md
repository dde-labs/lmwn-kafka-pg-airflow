# LMWN: Kafka Postgres via Airflow

**LMWN Assignment** that Extract & Load data from Postgres and Kafka via Airflow.

```text
coupons (465 rows)    --> Postgres, Kafka
orders (3660000 rows) --> Postgres, Kafka
```

> [!NOTE]
> This assignment use python version `3.9`.

## Prerequisite

- Install necessary Python package on your virtual environment.

    ```shell
    (.vnev) pip install -U uv
    (.vnev) uv pip install -r ./requirements.txt
    ```

- Create `.env` file

    ```dotenv
    LOCAL_PG_URL="postgresql+psycopg2://postgres@localhost:5432/postgres"
    LOCAL_KAFKA_HOST="localhost:9094"
    ```

- Provision Airflow

    ```shell
    docker build -t airflow-local -f .\.container\Dockerfile .
    docker compose -f ./.container/docker-compose.airflow.yml --env-file .env up -d
    ```

- Provision Docker container for source services

    ```shell
    docker compose -f ./.container/docker-compose.yml --env-file .env up -d
    ```

- Run Init scripts for uploading data to data source services. For running the
  initial scripts, I ues pytest because it easy to force the root path and passing
  the `.env` file to running context.

    - Load data to Postgres tables

      ```shell
      pytest -vv -s .\tests\test_init_scripts.py::test_reload_data_to_pg
      ```
      
    - Publish data to Kafka topics

      ```shell
      pytest -vv -s .\tests\test_init_scripts.py::test_publish_data_to_kafka
      ```

- Add the [Kafka cluster to UI](http://localhost:8080/) by config: `kafka:9092`

- Create the model tables for receive raw data

## Getting Started

- Go to Airflow UI and start running 

## Issue

I still stuck the spark installation issue when I want to install it on my airflow image.

```shell
(.venv) uv pip install pyspark
 x Failed to download and build `pyspark==3.5.4`
  |-> Failed to extract archive
  |-> failed to unpack `C:\Users\korawica\AppData\Local\uv\cache\sdists-v7\.tmp2Lg8cG\pyspark-3.5.4\deps\jars\JTransforms-3.1.jar`
  |-> failed to unpack `pyspark-3.5.4/deps/jars/JTransforms-3.1.jar` into `C:\Users\korawica\AppData\Local\uv\cache\sdists-v7\.tmp2Lg8cG\pyspark-3.5.4\deps\jars\JTransforms-3.1.jar`
  |-> error decoding response body
  |-> request or response body error
  `-> operation timed out
```

## Clear

```shell
docker compose -f ./.container/docker-compose.yml --env-file .env down
docker compose -f ./.container/docker-compose.airflow.yml --env-file .env down
```
