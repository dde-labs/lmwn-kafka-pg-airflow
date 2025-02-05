from pathlib import Path

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, URL



def reload_data_to_pg(url: URL, base_path: Path):
    data: dict[str, pd.DataFrame] = {
        "coupons": pd.read_csv(base_path / "data/coupons.csv"),
        "orders": pd.read_csv(base_path / "data/orders.csv"),
    }
    for table, df in data.items():
        conn = psycopg2.connect(
            host=url.host,
            dbname=url.database,
            user=url.username,
            password=url.password or "",
            port=url.port,
        )
        cur = conn.cursor()

        print(f"Drop table {table}")
        cur.execute(f"DROP TABLE IF EXISTS {table};")

        print(f"Create table {table}")
        with open(
            base_path / f"assignments/problem-0/{table}.sql", encoding='utf-8'
        ) as f:
            sql: str = "".join(f.readlines())
            assert sql != "", (
                "Found empty SQL, please make sure that you fill in table schema "
                "in coupons.sql or orders.sql files."
            )
            print(sql)
            cur.execute(query=sql)
        conn.commit()
        conn.close()

        print(f"Import data to table {table}")
        eng = create_engine(url)
        df.to_sql(
            name=table,
            con=eng,
            if_exists="append",
            chunksize=1000,
            index=False,

            # NOTE: Use the multi method for ingest perf.
            method='multi',
        )
        df = pd.read_sql(f"select count(1) as cnt from {table}", con=eng)
        print(f"Imported {df['cnt'][0]} rows")
