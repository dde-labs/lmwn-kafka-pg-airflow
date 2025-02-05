import json
from pathlib import Path

from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer
import pandas as pd


def publish_data_to_kafka(host: str, base_path: Path):
    data: dict[str, pd.DataFrame] = {
        "coupons": pd.read_csv(base_path / "data/coupons.csv"),
        "orders": pd.read_csv(base_path / "data/orders.csv"),
    }
    admin = AdminClient({"bootstrap.servers" : host})

    for my_topic, df in data.items():

        # NOTE: delete and recreate topic
        print(f"Deleting topic {my_topic} if exists")
        ops = admin.delete_topics([my_topic], operation_timeout=30)
        for topic, f in ops.items():
            try:
                f.result()
                print(f"Topic {topic} is deleted")
            except Exception as e:
                print(f"Failed to delete topic {topic}: {e}")

        print(f"Creating topic {my_topic}")
        new_topics = [NewTopic(my_topic, num_partitions=3, replication_factor=1)]
        ops = admin.create_topics(new_topics)
        for topic, f in ops.items():
            try:
                f.result()
                print(f"Topic {topic} is created")
            except Exception as e:
                print(f"Failed to create topic {topic}: {e}")

        # NOTE: import data to Kafka
        producer = Producer({ "bootstrap.servers" : host })
        print(f"Importing {my_topic} data")

        cnt: int = 0
        batch_size: float = 5e4
        for _, row in df.iterrows():

            if cnt % batch_size==0 and cnt!=0:
                producer.flush()
                print(f"{cnt} message is imported")

            producer.produce(my_topic, json.dumps(row.to_dict()))
            cnt += 1

        producer.flush()
