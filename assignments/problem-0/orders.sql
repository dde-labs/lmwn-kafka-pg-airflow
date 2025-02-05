--  place your answer here
CREATE TABLE IF NOT EXISTS orders (
  order_id      varchar(16) NOT NULL,
  date          timestamp NOT NULL,
  user_id       varchar(16) NOT NULL,
  coupon_id     varchar(16) NOT NULL,
  status        varchar(16) NOT NULL
)
