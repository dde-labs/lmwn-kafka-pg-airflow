FROM apache/airflow:2.10.4-python3.11

USER root

COPY ./packages.txt /

# NOTE: Install OpenJDK-17
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
    && grep -vE '^\s*#' /packages.txt | sed -e 's/\r//g' | tr "\n" " " | xargs sudo apt-get install -y \
    && apt-get autoremove -yqq --purge \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# NOTE: Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64/
RUN export JAVA_HOME

USER airflow

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

COPY --chown=airflow:root ./airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

COPY --chown=airflow:root ./requirements.airflow.txt /

RUN uv pip install  \
    --no-cache-dir \
    "apache-airflow==${AIRFLOW_VERSION}" \
    -r /requirements.airflow.txt
