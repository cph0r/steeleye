from pandas.core.reshape import merge
import requests
import json
import pandas as pd
import csv
from constants import *

def generate_csv(df,name):
    print('inside')
    df.to_csv(PATH+name+CSV, encoding=UTF8)

def merge_df(df1,df2):
    df1 = df1.rename(columns={'source_ip': 'ip_address'})
    result = df1.merge(df2,on='ip_address',how='left')
    return result
    
def get_most_used_application(df):
    df['C'] = df.groupby('application')['application'].cumcount()
    df.sort_values(by=['C', 'application'], inplace=True)
    print (df)
    generate_csv(df,'csv3')


def create_df(from_date, to_date):
    activity_data_list = []
    for i in range(1,NO_OF_ACTIVITY_FILES+1):
        activity_data_list.append(pd.read_csv(DATA_PATH+ACTIVITY+str(i)+CSV,skipinitialspace = True))

    activity_df = pd.concat(activity_data_list, ignore_index=True)
    activity_df.dropna(subset = ["source_ip",'date'], inplace=True)
    # print(activity_df)
    user_df = pd.read_csv(DATA_PATH+USER_DATA+CSV,skipinitialspace = True)
    user_df.dropna(subset = ["ip_address"], inplace=True)
    # generate_csv(user_df,'user_data')
    # generate_csv(activity_df,'act_data')

    merged_df = merge_df(activity_df,user_df)
    get_most_used_application(merged_df)
    # merged_df.dropna(subset = ["ip_address",'date'], inplace=True)
    # generate_csv(merged_df,'activity_data')
    # generate_csv(user_df,)

create_df(1, 10)

def get_most_active_users(df):
    print('most activate users')
    # user_id, first_name, last_name, email, total_hits
    generate_csv(df,'csv1')


def get_countries_with_most_website_visits(df):
    # country_name, country_code, total_hits
    print(df)
    generate_csv(df,'csv2')