from airflow.decorators import dag, task
from datetime import datetime

import pyspark.sql.functions as f
from pyspark import SparkContext
from pyspark.sql import SparkSession
from airflow.operators.python import get_current_context


@dag(
    start_date=datetime(2025, 2, 6),
    schedule="0 6 * * *",
    catchup=False,
)
def batch_postgres_daily():

    @task.pyspark(conn_id="my_spark_conn")
    def extract_coupons(spark: SparkSession, sc: SparkContext):
        context = get_current_context()
        execution_date = context.get("execution_date")
        src_df = (
            spark.read
            .format("jdbc")
            .option("url", "jdbc:postgresql://localhost:5433/postgres")
            .option("user", "postgres")
            .option("driver", "org.postgresql.Driver")
            .option(
                "query",
                (
                    f"SELECT * FROM coupons "
                    f"WHERE date = '{execution_date:%Y-%m-%d}'"
                ),
            )
            .load()
        )

        # TODO: Delete data that have load_date more than this exec date.

        tgt_df = (
            spark.read
            .format("jdbc")
            .option("url", "jdbc:postgresql://localhost:5433/postgres")
            .option("user", "postgres")
            .option("driver", "org.postgresql.Driver")
            .option("query", f"SELECT * FROM view_coupons_active ")
            .load()
        )

        result = (
            src_df.join(tgt_df, on='coupon_id', by='left')
            .withColumn(
                'updated',
                (
                    f.when(f.col("tgt.coupon_id").is_null(), f.lit(False))
                    .when(
                        (f.col("tgt.date") != f.col("src.date"))
                        | (f.col("tgt.amount") != f.col("src.amount")),
                        f.lit(True)
                    )
                    .otherwies(f.lit(False))
                )
            )
            .select("src.*", "updated")
        )
        insert_df = result.filter("updated is true").dropColumn("updated")
        update_df = result.filter("updated is true").dropColumn("updated")

        # TODO: insert is use append mode

        # TODO: update will split to the update and append mode for SCD2

    @task.pyspark(conn_id="my_spark_conn")
    def extract_orders(spark: SparkSession, sc: SparkContext):
        context = get_current_context()
        execution_date = context.get("execution_date")
        src_df = (
            spark.read
            .format("jdbc")
            .option("url", "jdbc:postgresql://localhost:5433/postgres")
            .option("user", "postgres")
            .option("driver", "org.postgresql.Driver")
            .option(
                "query",
                (
                    f"SELECT * FROM orders "
                    f"WHERE date::date = '{execution_date:%Y-%m-%d}'"
                ),
            )
            .load()
        )

        # TODO: Delete data that have load_date more than this exec date.

        (
            src_df.write
            .format('jdbc')
            .option("url", "jdbc:postgresql://localhost:5433/postgres")
            .option("user", "postgres")
            .option("driver", "org.postgresql.Driver")
            .option("dbtable", "test_table")
            .mode("append")
            .save()
        )


    @task
    def metric_coupons():
        # TODO: Create metric;
        #   a. For each day, how much the business team spends their budget on specific coupon
        ...


    @task
    def metric_orders():
        # TODO: Create metric;
        #   b. For each day, how many users are considered to be first-purchased use
        ...


    extract_coupons() >> metric_coupons()
    extract_orders() >> metric_orders()


batch_postgres_daily()
