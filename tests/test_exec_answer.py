import os

import psycopg2
import pytest
from sqlalchemy import make_url, URL


@pytest.fixture(scope='module')
def url() -> URL:
    return make_url(os.getenv("LOCAL_PG_URL"))


def test_answer_01(url):
    conn = psycopg2.connect(
        host=url.host,
        dbname=url.database,
        user=url.username,
        password=url.password or "",
        port=url.port,
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT MIN(date) AS the_first_completed_date
        FROM orders
        WHERE user_id = 'USER-0031' AND status = 'COMPLETE'
        """
    )
    rs = cur.fetchone()
    print(rs)
    conn.commit()
    conn.close()


def test_answer_02(url):
    conn = psycopg2.connect(
        host=url.host,
        dbname=url.database,
        user=url.username,
        password=url.password or "",
        port=url.port,
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT COUNT(1) AS times_used
        FROM orders
        WHERE coupon_id = 'COUPON-0031' AND status = 'COMPLETE'
        """
    )
    rs = cur.fetchone()
    print(rs)
    conn.commit()
    conn.close()


def test_answer_03(url):
    conn = psycopg2.connect(
        host=url.host,
        dbname=url.database,
        user=url.username,
        password=url.password or "",
        port=url.port,
    )
    cur = conn.cursor()
    cur.execute(
        """
        SELECT COUNT(1) AS count_users
        FROM orders AS o
        JOIN coupons AS c
          ON o.coupon_id = c.coupon_id
          AND o.date::date = c.date
        WHERE o.coupon_id = 'COUPON-0031' AND o.status = 'COMPLETE' AND c.amount < 90 
        """
    )
    rs = cur.fetchone()
    print(rs)
    conn.commit()
    conn.close()
