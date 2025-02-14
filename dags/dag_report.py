from datetime import datetime

from airflow.decorators import dag, task


@dag(
    start_date=datetime(2025, 2, 6),
    schedule=None,
    catchup=False,
)
def make_report():

    @task
    def report_01():
        # TODO: Please find which date is the first completed order for user `USER-0031`.
        ...


    @task
    def report_02():
        # TODO: Please find how many times coupon `COUPON-0031` is used.
        ...

    @task
    def report_03():
        # TODO: Please find how many users has used coupon `COUPON-0031` with amouth less than 90 baht
        ...

    @task
    def report_04():
        # TODO: I want to visualize the total usage of coupon COUPON-0001 on a daily basis in Q3 of 2024
        ...

    @task
    def report_05():
        # TODO: I want to visualize the number of first-purchase users on a daily basis in Q2 of 2024
        ...


    [
        report_01(),
        report_02(),
        report_03(),
    ] >> [
        report_04(),
        report_05()
    ]

make_report()
