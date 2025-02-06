CREATE TABLE IF NOT EXISTS model_orders (
  order_id      varchar(16) NOT NULL,
  date          timestamp NOT NULL,
  user_id       varchar(16) NOT NULL,
  coupon_id     varchar(16) NOT NULL,
  status        varchar(16) NOT NULL,
  load_date     date NOT NULL,
  src_name      varchar(32) NOT NULL
)
