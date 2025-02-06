1. Please find which date is the first completed order for user `USER-0031`.

    ```
    SELECT MIN(date) AS the_first_completed_date
    FROM orders
    WHERE user_id = 'USER-0031' AND status = 'COMPLETE'
    ```
   
    ```
    2024-02-04 18:36:06
    ```
   
2. Please find how many times coupon `COUPON-0031` is used.

    ```
    SELECT COUNT(1) AS times_used
    FROM orders
    WHERE coupon_id = 'COUPON-0031' AND status = 'COMPLETE'
    ```

    ```
    18262
    ```

3. Please find how many users has used coupon `COUPON-0031` with amouth less than 90 baht

    ```
    SELECT COUNT(1) AS count_users
    FROM orders as o
    JOIN coupons as c
      ON o.coupon_id = c.coupon_id
      AND o.date::date = c.date
    WHERE o.coupon_id = 'COUPON-0031' AND o.status = 'COMPLETE' AND c.amount < 90 
    ```

    ```
    189
    ```
