from random import seed
from random import randrange
from datetime import date, timedelta
import random


def daily_moods_insert(user_id, date, was_happy, created_at, updated_at):
    inster_query = """insert into dw.daily_moods values ({}, {}, {}, {}, {});""".format(user_id, date, was_happy,
                                                                                        created_at, updated_at)
    return inster_query


"""
:param n: number of random rows to be generated
:param start_date: date(2021, 8, 1),  
:param end_date: date(2015, 8, 31)
:return: list of random dates: ['/2015/06/08', '/2015/06/22', '/2015/06/20']
:usage: res = gen_random_date(5, date(2015, 7, 1), date(2015, 7, 5))
"""
def gen_random_date(n, start_date, end_date):
    print("The original range : " + str(start_date) + " " + str(end_date))
    dates_bet = end_date - start_date
    total_days = dates_bet.days
    res = []
    for idx in range(n):
        random.seed(a=None)
        # getting random days
        randay = random.randrange(total_days)
        # getting random dates
        random_date_object = start_date + timedelta(days=randay)
        res.append(random_date_object.strftime('%Y/%m/%d'))
    return res

def simulate_daily_moods():
    seed(1)
    # select a subset without replacement
    user_id = [randrange(1, 201) for i in range(15)]
    was_happy = [randrange(0, 2) for i in range(15)]
    health_date = gen_random_date(15, date(2021, 8, 1), date(2021, 8, 31))
    rows = 10
    rows_dict = {'user_id': user_id,
                 'date': health_date,
                 'was_happy': was_happy,
                 'created_at': '2021-08-23',
                 'updated_at': '2021-08-23'
                 }

    daily_moods_queries = []
    for i in range(rows):
        insert_query = daily_moods_insert(rows_dict['user_id'][i]
                                          , rows_dict['date'][i]
                                          , rows_dict['was_happy'][i]
                                          , rows_dict['created_at']
                                          , rows_dict['updated_at'])
        daily_moods_queries.append(insert_query)
    return daily_moods_queries