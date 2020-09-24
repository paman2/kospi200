import pandas as pd
import numpy as np
import math


def average_price_ext(t_df, t_date):
    r_data = pd.DataFrame(index=list(range(0, len(t_df))), columns=list('a'))
    for i in range(t_date - 1, len(t_df)):
        r_data['a'][i] = t_df[i - t_date + 1:i].mean()
    return r_data['a']


df = pd.DataFrame()
for i in range(26):
    f_path = 'D://data (' + str(i) + ').xls'
    # excel_data_df = pandas.read_excel(f_path, sheet_name='Employees')
    excel_data_df = pd.read_excel(f_path)
    excel_data_df = excel_data_df.loc[::-1].reset_index()
    df = df.append(excel_data_df)
df = df.loc[::-1].reset_index()
t1 = 3
t2 = 20

for i in [t1, t2]:
    df[str(i)] = average_price_ext(df['현재지수'], i)

import numpy as np


def check_up_down(df1):
    # print(math.isnan(df1['5']))
    if math.isnan(df1[str(t1)]) or math.isnan(df1[str(t2)]) or math.isnan(df1['시가지수']):
        return False

    if df1[str(t1)] > df1[str(t2)]:
        return True
    else:
        return False


t_hole = False
t_sell = False
sum = 0
for i in range(len(df)):
    if check_up_down(df.loc[i]) and (t_hole == False):
        if t_sell == True:
            sum = t_now - df['시가지수'][i + 1]
        # print(df['시가지수'][i+1])
        t_now = df['시가지수'][i + 1]
        t_hole = True
        t_day = df['일자'][i + 1]
        t_sell == False

    if (check_up_down(df.loc[i]) == False) and (t_hole == True):
        print('매수일 : ', t_day, '매수가격 : ', t_now, sep='  ')
        # print('매도일 : ' , df['일자'][i+1], '매도가격 : ',df['시가지수'][i+1] , sep = '  ' )
        # t_diff = df['시가지수'][i+1] - t_now
        print('매도일 : ', df['일자'][i], '매도가격 : ', df['현재지수'][i], sep='  ')
        t_diff = df['현재지수'][i] - t_now
        print('차액', t_diff, sep='')
        t_now = df['현재지수'][i]
        t_hole = False
        t_sell = True
        sum = sum + t_diff

print('최종수익 : ', sum, sep=' ')