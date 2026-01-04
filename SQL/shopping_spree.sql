'''
User Shopping Sprees

In an effort to identify high-value customers, Amazon asked for your help to obtain data about users who go on shopping sprees. A shopping spree occurs when a user makes purchases on 3 or more consecutive days.

List the user IDs who have gone on at least 1 shopping spree in ascending order.
'''

with cte1 as (
select user_id, amount, transaction_date,
  lag(transaction_date)
  over(
    partition by user_id
    order by transaction_date)
  as prev_day_1
from transactions
),
cte2 as (
select user_id, amount, transaction_date, prev_day_1,
  lag(prev_day_1)
  over(
    partition by user_id
    order by prev_day_1)
  as prev_day_2
from cte1
)
select distinct user_id 
from cte2
where transaction_date is not NULL
and prev_day_1 is not NULL
and prev_day_2 is not NULL
and date(transaction_date)-date(prev_day_1) = 1
and date(prev_day_1)-date(prev_day_2) = 1;



