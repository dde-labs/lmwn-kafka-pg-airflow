FROM apache/airflow:2.10-python3.9

USER root

#ENV SPARK_VERSION 3.5.4
#ENV SPARK_HADOOP_PROFILE 3
#
#ENV SPARK_SRC_URL https://www.apache.org/dist/spark/spark-$SPARK_VERSION/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_PROFILE}.tgz
#ENV SPARK_HOME=/opt/spark
#ENV PATH $PATH:$SPARK_HOME/bin

#RUN apt update \
#    && apt-get install -y wget \
#    && apt-get clean \
#    && wget ${SPARK_SRC_URL} \
#    && tar -xzf spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_PROFILE}.tgz \
#    && mv spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_PROFILE} /opt/spark \
#    && rm -f spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_PROFILE}.tgz

# Install OpenJDK-17
#RUN #apt update \
#    && apt-get install -y --no-install-recommends openjdk-17-jre-headless \
#    && apt-get autoremove -yqq --purge \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# RUN apt update \
#     && apt-get install -y --no-install-recommends openjdk-17-jre-headless \
#     && apt-get autoremove -yqq --purge \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
#
# # Set JAVA_HOME
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
# ENV JAVA_VERSION=17

RUN uv pip install --upgrade pip \
    && uv pip install --no-cache-dir \
      "pyspark"

#USER airflow
#
#RUN uv pip install --upgrade pip \
#    && uv pip install --no-cache-dir \
#      "apache-airflow==${AIRFLOW_VERSION}" \
#      "pyspark" \
#      "apache-airflow-providers-apache-spark"
