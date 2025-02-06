CREATE TABLE IF NOT EXISTS stream_coupons (
  id            SERIAL PRIMARY KEY,
  coupon_id     varchar(16) NOT NULL,
  date          date NOT NULL,
  amount        integer NOT NULL,
  start_date    TIMESTAMP,
  end_date      TIMESTAMP,
  active_flag   BOOLEAN,
  load_date     date NOT NULL,
  src_name      varchar(32) NOT NULL
)
