FROM airflow-java-local:latest

USER airflow

COPY --chown=airflow:root ./airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

COPY --chown=airflow:root ./requirements.airflow.txt /requirements.airflow.txt

RUN uv pip install  \
    --no-cache-dir \
    "apache-airflow==${AIRFLOW_VERSION}" \
    -r /requirements.airflow.txt
