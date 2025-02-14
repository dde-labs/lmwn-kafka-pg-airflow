FROM apache/airflow:2.8.1-python3.9

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      openjdk-17-jre-headless \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

# NOTE: This path will change to `/usr/lib/jvm/java-17-openjdk-arm64` if you
#   run on MAC.
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

RUN export JAVA_HOME

RUN uv pip install apache-airflow apache-airflow-providers-apache-spark \
    pyspark
