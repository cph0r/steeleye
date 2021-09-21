import requests
import json
import pandas as pd
import csv
from constants import *

def generate_csv(df,name):
    df.to_csv(PATH+name+CSV, encoding=UTF8)

def merge_df(df1,df2):
    """left Join df1 and df2"""
    df1 = df1.rename(columns={'source_ip': 'ip_address'})
    result = df1.merge(df2,on='ip_address',how='left')
    return result
    
def get_most_used_application(df):
    df['C'] = df.groupby('application')['application'].cumcount()
    df.sort_values(by=['C', 'application'], inplace=True)
    generate_csv(df,'csv3')


def create_df(from_date, to_date):
    """Create Df"""
    activity_df = create_activity_df(from_date,to_date)
    user_df = get_user_df()
    merged_df = merge_df(activity_df,user_df)
    get_most_used_application(merged_df)

def get_user_df():
    """Generate user data df"""
    user_df = pd.read_csv(DATA_PATH+USER_DATA+CSV,skipinitialspace = True)
    user_df.dropna(subset = ["ip_address"], inplace=True)
    return user_df
   
    
def create_activity_df(f_data,t_date):
    """Generate activity data df"""
    activity_data_list = []
    for i in range(1,NO_OF_ACTIVITY_FILES+1):
        activity_data_list.append(pd.read_csv(DATA_PATH+ACTIVITY+str(i)+CSV,skipinitialspace = True))

    activity_df = pd.concat(activity_data_list, ignore_index=True)
    activity_df = filter_date(activity_df)
    activity_df.dropna(subset = ["source_ip",'date'], inplace=True)
    return activity_df

def filter_date(activity_df):
    """Filter Date"""
    activity_df['date'] = pd.to_datetime(activity_df['date'], format='%Y-%m-%d')
    activity_df = activity_df.loc[(activity_df['date'] >= '2020-09-01')
                     & (activity_df['date'] < '2020-09-15')]
                     
    return activity_df
   

create_df(1, 10)

def get_most_active_users(df):
    """Get Most Active Users"""
    # user_id, first_name, last_name, email, total_hits
    generate_csv(df,'csv1')


def get_countries_with_most_website_visits(df):
    """Get Countries of Most visited website"""
    # country_name, country_code, total_hits
    generate_csv(df,'csv2')