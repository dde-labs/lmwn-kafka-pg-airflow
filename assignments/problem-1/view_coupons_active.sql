CREATE VIEW IF NOT EXISTS view_coupons AS
SELECT
    coupon_id
    date
    amount
FROM model_coupons
WHERE active_flag is true
