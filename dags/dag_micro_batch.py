import json

from airflow.decorators import dag, task
from datetime import datetime

import pandas as pd
from airflow.providers.apache.kafka.operators.consume import ConsumeFromTopicOperator


def consume_coupons_func(message):
    message_content = json.loads(message.value())
    df = pd.DataFrame.from_dict(message_content)


def consume_coupons_func(message):
    message_content = json.loads(message.value())
    df = pd.DataFrame.from_dict(message_content)



@dag(
    start_date=datetime(2025, 2, 6),
    schedule="5 * * * *",
    catchup=False,
)
def micro_batch_kafka():

    consume_coupons = ConsumeFromTopicOperator(
        task_id="consume_coupons",
        kafka_config_id="kafka_default",
        topics=["coupons"],
        apply_function=consume_function,
        poll_timeout=60,
        max_messages=10_000,
        max_batch_size=10_000,
    )

    consume_orders = ConsumeFromTopicOperator(
        task_id="consume_orders",
        kafka_config_id="kafka_default",
        topics=["orders"],
        apply_function=consume_function,
        poll_timeout=60,
        max_messages=10_000,
        max_batch_size=10_000,
    )

    consume_coupons
    consume_orders


micro_batch_kafka()
