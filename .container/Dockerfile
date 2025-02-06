FROM apache/airflow:2.10.4-python3.11

USER root

COPY ./packages.txt /

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
    && grep -vE '^\s*#' /packages.txt | sed -e 's/\r//g' | tr "\n" " " | xargs sudo apt-get install -y \
    && apt-get autoremove -yqq --purge \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y openjdk-17-jdk-headless \
    && apt-get install -y ant \
    && apt-get clean \

ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.5.jar
RUN mv postgresql-42.2.5.jar /opt/spark/jars

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

COPY --chown=airflow:root ./airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

COPY --chown=airflow:root ./requirements.airflow.txt /

RUN uv pip install  \
    --no-cache-dir \
    "apache-airflow==${AIRFLOW_VERSION}" \
    -r ./requirements.airflow.txt
