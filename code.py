import pandas as pd
import numpy as np
import math
import time
t1 = 1
t2 = 3
t3 = 5
r_date1 = '2019/01/01'
r_date2 = '2020/08/31'

def date_to_int(t_str):
    t_str1 = t_str.split('/')
    t_str1 = ''.join(t_str1)
    return int(t_str1)

def check1(t_df, t_date):
    t_date1 = date_to_int(t_date)
    t_num = 0
    for obj in t_df:
        t_obj  = date_to_int(obj)
        if t_obj >= t_date1:                
            return t_num

        t_num = t_num + 1
        

def average_price_ext(t_df, t_date):
    if t_date == 1:
        return t_df
    else:
        r_data = pd.DataFrame(index=list(range(0, len(t_df))), columns=list('a'))
        for i in range(t_date - 1, len(t_df)):
            r_data['a'][i] = t_df[i - t_date + 1:i+1].mean()
        return r_data['a']

def buy_slope1(t_list):
    t_delta = []
    for i in range(len(t_list)-1):
        t_delta.append(t_list[i+1]-t_list[i])
    if t_delta[0] < 0 and t_delta[1] > 0:
        return True
    else:
        return False

def delta_abs_value(t1,t2):
    return abs(t1-t2)
    
def run():
    t_sum = 0
    for i in range(2,len(df)-2):
        if buy_slope1(list(df['3'][i:i+3])):
            if df['종가'][i+2] > df['시가'][i+2] and df['종가'][i+2] < df['시가'][i+3] and delta_abs_value(df['3'][i+1], df['3'][i+2])/delta_abs_value(df['3'][i], df['3'][i+1]) > 0.9:
                diff = df['종가'][i+3] - df['시가'][i+3]
                print(df['일자'][i+3],'매수 : ', df['시가'][i+3], '매도 : ', df['종가'][i+3], '차익 :',diff,'3일선 :',df['3'][i+3], sep = ' ')
                t_sum = t_sum + diff
    print("final : ", t_sum , sep = ' ')

    
def run1():
    diff = 0
    t_sum = 0
    flag = 0
    for i in range(len(df)):
        if math.isnan(df[str(t1)][i]) == False and math.isnan(df[str(t2)][i]) == False:
            if df[str(t1)][i] > df[str(t2)][i]:
                if flag == 0:
                    diff = df['종가'][i]
                    flag = 1
                               
            else:
                if diff != 0 and flag == 1:
                    tmp = df['종가'][i] - diff 
                    print(df['일자'][i],'매수 :',diff,'매도 :',df['종가'][i],'차익 :',tmp, sep = '   ') 
                    diff = df['종가'][i] - diff
                    t_sum = t_sum + diff
                    flag = 0
    print('손익 :',t_sum, sep = '   ')
    


    

t_df = pd.DataFrame()
for i in range(26):
    f_path = 'D://David//Documents//01_project//25_주식파이썬//10_kospi200//data ('+ str(i) +').xls'
    #excel_data_df = pandas.read_excel(f_path, sheet_name='Employees')
    excel_data_df = pd.read_excel(f_path)
    excel_data_df = excel_data_df.loc[::-1].reset_index()
    t_df = t_df.append(excel_data_df)
    
t_df = t_df.loc[::-1].reset_index()
df = pd.DataFrame(columns = ['일자','종가','시가','고가','저가'],index =range(len(t_df)))
df['일자'] = t_df['일자'] 
df['종가'] = t_df['현재지수'] 
df['시가'] = t_df['시가지수'] 
df['고가'] = t_df['고가지수'] 
df['저가'] = t_df['저가지수'] 

time.sleep(1)
df = df.dropna()
df = df.drop([84])
df = df.loc[::1].reset_index()
df = df.drop(['index'], axis = 1)
df[str(t1)] = average_price_ext(df['종가'], t1)
df[str(t2)] = average_price_ext(df['종가'], t2)
df[str(t3)] = average_price_ext(df['종가'], t3)

r_date1 = '2007/01/01'
r_date2 = '2020/08/31'

def check_red(t_df):
    if t_df['시가']-t_df['종가'] > 0:
        return True
    else:
        return False
    
def check_sell_trand(t_df):
    t_num = 0
    for i in t_df.index:
        if t_df[str(t2)][i] < t_df[str(t3)][i]:
            t_num = t_num + 1
    if t_num == len(t_df):
        return False
    else:
        return True
    
def check_buy_trand(t_df):
    t_num = 0
    for i in t_df.index:
        if t_df[str(t3)][i] < t_df[str(t3)][i]:
            t_num = t_num + 1
    if t_num == len(t_df):
        return False
    else:
        return True
    


def run2():    #매수함수 결과는 1계약당 수익 // ex) 5point 1계약 5point 25만원 ==> 1*5*25 125만원
    df2 = df.loc[check1(df['일자'],r_date1):check1(df['일자'],r_date2)] 
    diff = 0
    t_sum = 0
    flag = 0
    t_date = ''
    for i in df2.index:
        if math.isnan(df2[str(t1)][i]) == False and math.isnan(df2[str(t2)][i]) == False:
            t_var1 = np.var(df[str(t2)][i-t2+1:i+1])
            t_var2 = np.var(df[str(t3)][i-t3+1:i+1])
            if df2[str(t1)][i] > df2[str(t2)][i] and check_sell_trand(df2.loc[i-t2+1:i+1]):
                if flag == 0:
                    diff = df2['종가'][i]
                    flag = 1
                    t_date = df2['일자'][i]
                    t_var1 = np.var(df[str(t2)][i-t2+1:i+1])
                    t_var2 = np.var(df[str(t3)][i-t3+1:i+1])
            elif df2[str(t1)][i] < df2[str(t2)][i]:
                if diff != 0 and flag == 1:
                    tmp = df2['종가'][i] - diff 
                    print('매수일 :',t_date ,'환매도일 :',df2['일자'][i],'매수 :',diff,'환매도 :',df2['종가'][i],'차익 :',round(tmp,3),'분산1 : ',round(t_var1,3),'분산2 : ',round(t_var2,3), sep = ' ') 
                    diff = df2['종가'][i] - diff
                    
                    t_sum = t_sum + diff
                    flag = 0
    print('손익 :',t_sum, sep = '   ')
    

    
def run3(): #매도함수
    df2 = df.loc[check1(df['일자'],r_date1):check1(df['일자'],r_date2)] 
    diff = 0
    t_sum = 0
    flag = 0
    t_date = ''
    for i in df2.index:
        if math.isnan(df2[str(t1)][i]) == False and math.isnan(df2[str(t2)][i]) == False:
            t_var = np.var(df['종가'][i-4:i+1])
            if df2[str(t1)][i] < df2[str(t2)][i] and df2[str(t2)][i] < df2[str(t3)][i] and check_red(df2.loc[i]) and t_var > 1.0:
                if flag == 0:
                    diff = df2['종가'][i]
                    flag = 1
                    t_date = df2['일자'][i]                    
            elif df2[str(t1)][i] > df2[str(t2)][i] and check_sell_trand(df2.loc[i-t2+1:i+1]):
                if diff != 0 and flag == 1:
                    tmp =  diff - df2['종가'][i]
                    print('매도일 :',t_date ,'환매수일 :',df2['일자'][i],'매도 :',diff,'환매수 :',df2['종가'][i],'차익 :',round(tmp,3),'분산 : ',round(t_var,3), sep = '   ') 
                    diff = diff - df2['종가'][i] 
                    
                    t_sum = t_sum + diff
                    flag = 0
    print('손익 :',t_sum, sep = '   ')
