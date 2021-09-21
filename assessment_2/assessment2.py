import pandas as pd
from constants import *

# CONSTANTS
FROM_DATE = '2020-08-08'
END_DATE = '2021-08-18'

def create_df(from_date, to_date):
    """Create Df"""
    activity_df = create_activity_df(from_date,to_date)
    user_df = get_user_df()
    get_most_used_application(activity_df)
    get_most_active_users(user_df,activity_df)
    get_countries_with_most_website_visits(user_df,activity_df)

def get_user_df():
    """Generate user data df"""
    user_df = pd.read_csv(DATA_PATH+USER_DATA+CSV,skipinitialspace = True)
    user_df.dropna(subset = [IP_ADDRESS,ID], inplace=True)
    return user_df
   
    
def create_activity_df(f_date,t_date):
    """Generate activity data df"""
    activity_df = merge_all_activity_data()
    activity_df = filter_date(activity_df,f_date,t_date)
    # activity_df[APPLICATION_WITH_VERSION] = activity_df[APPLICATION] + ' '+activity_df[VERSION] 
    activity_df.dropna(subset = [SRC_IP ,DATE], inplace=True)
    return activity_df

def merge_all_activity_data():
    """Merge all activity csv"""
    activity_data_list = []
    for i in range(1,NO_OF_ACTIVITY_FILES+1):
        activity_data_list.append(pd.read_csv(DATA_PATH+ACTIVITY+str(i)+CSV,skipinitialspace = True))

    activity_df = pd.concat(activity_data_list, ignore_index=True)
    return activity_df

def filter_date(activity_df,f_date,t_date):
    """Filter Date"""
    activity_df[DATE] = pd.to_datetime(activity_df[DATE], format='%Y-%m-%d')
    activity_df = activity_df.loc[(activity_df[DATE] >= f_date)
                     & (activity_df[DATE] < t_date)]
                     
    return activity_df

def generate_csv(df,name):
    """Generate csv"""
    df.to_csv(CREATED_PATH+name+CSV, encoding=UTF8)

def merge_df(df1,df2):
    """left Join df1 and df2"""
    df1 = df1.rename(columns={SRC_IP: IP_ADDRESS})
    result = df1.merge(df2,on=IP_ADDRESS,how='left')
    return result
    
def get_most_used_application(df):
    """Get most used application"""
    df1 = df.groupby(APPLICATION).size().sort_values(ascending=False).reset_index(name=TOTAL_HITS)[0:3]
    generate_csv(df1,CSV3)

def get_most_active_users(df,activity_df):
    """Get Most Active Users"""
    df2 = activity_df.groupby(SRC_IP).size().sort_values(ascending=False).reset_index(name=TOTAL_HITS)[0:10]
    result = merge_df(df2,df)[[ID,FIRST_NAME,LAST_NAME,EMAIL,GENDER,TOTAL_HITS]]
    generate_csv(result,CSV1)


def get_countries_with_most_website_visits(user_df,activity_df):
    """Get Countries of Most visited website"""
    df1 = activity_df.groupby(SRC_IP).size().sort_values(ascending=False).reset_index(name=TOTAL_HITS)
    result =  merge_df(df1,user_df)[[COUNTRY,COUNTRY_CODE,TOTAL_HITS]]
    generate_csv(result,CSV2)

if __name__ == '__main__':
    create_df(FROM_DATE,END_DATE)