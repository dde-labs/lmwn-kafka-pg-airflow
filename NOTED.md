# Noted

## Prepare Airflow Docker image.

A development noted.

```shell
docker build --rm --force-rm `
  -t airflow-java-local `
  -f .\.container\java.Dockerfile . `
  --build-arg AIRFLOW_VERSION=2.10.4
```

```shell
docker image ls
```

```text
REPOSITORY             TAG        IMAGE ID       CREATED          SIZE
airflow-java-local     latest     f94727e84d2a   39 seconds ago   3.17GB
```

```shell
docker build --rm --force-rm `
  -t airflow-local `
  -f .\.container\use.java.Dockerfile .
```

```shell
docker image ls
```

```text
REPOSITORY             TAG        IMAGE ID       CREATED          SIZE
airflow-local          latest     7ac684f3a12f   19 seconds ago   3.18GB
airflow-java-local     latest     f94727e84d2a   12 minutes ago   3.17GB
```
