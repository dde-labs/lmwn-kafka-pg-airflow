# LMWN: Kafka Postgres via Airflow

**LMWN Assignment** that Extract & Load data from Postgres and Kafka via Airflow.

**Sizing data for this assignment:**

```text
coupons (465 rows)    --> Postgres, Kafka
orders (3660000 rows) --> Postgres, Kafka
```

> [!NOTE]
> This assignment use python version `3.9` and WSL Docker on Windows11 for testing.

> [!NOTE]
> Spark and Hadoop versions follow the versions as defined at [Spark Download Page](https://spark.apache.org/downloads.html)

## Prerequisite

- Install necessary Python packages on your Python virtual environment.

    ```shell
    (.vnev) pip install -U uv
    (.vnev) uv pip install -r ./requirements.txt
    ```

- Create the `.env` file for keep credential and connection values.

    ```dotenv
    LOCAL_PG_URL="postgresql+psycopg2://postgres@localhost:5432/postgres"
    LOCAL_KAFKA_HOST="localhost:9094"
    ```

- Provision the Airflow containers

    > [!WARNING]
    > This step, I still got the error when install Pyspark on the building Docker
    > image.

    ```shell
    docker build --rm --force-rm `
      -t airflow-image-local `
      -f .\.container\Dockerfile . `
      --build-arg AIRFLOW_VERSION=2.10.4
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

- Create the model and stream tables for receive raw data from batch and micro-batch DAGs

  ```shell
  pytest -vv -s .\tests\test_init_models_and_streams.py::test_create_models_and_streams
  ```

## Getting Started

- Go to the Airflow UI and start navigate to the batch DAG and run it.

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

After I investigate this issue, it might be permission of my cache folder because
when I try to install via `uv pip install pyspark --target ./installed`, it worked!!!.

## Clear

```shell
docker compose -f ./.container/docker-compose.yml --env-file .env down
docker compose -f ./.container/docker-compose.airflow.yml --env-file .env down
```
