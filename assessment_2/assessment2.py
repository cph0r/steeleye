import pandas as pd
from constants import *
import logging
import datetime
from datetime import datetime

# CONSTANTS
FROM_DATE = '2021-08-17'
END_DATE = '2021-08-18'
logging.basicConfig(filename=str(os.getcwd())+'/generated_data/assessment2.log', level=logging.DEBUG)


def create_df(from_date, to_date):
    """Create Df"""
    try:
        f_date = datetime.strptime(from_date, '%Y-%m-%d')
        t_date = datetime.strptime(to_date, '%Y-%m-%d')
        if t_date < f_date:
            logging.error(str(datetime.now())+': to date should be greater than from date')
        else:
            merged_df = pd.concat([create_activity_df(), create_user_df()], axis=1)
            merged_df.dropna(subset=[DATE, WEBSITE], inplace=True)
            merged_df = filter_date(merged_df, from_date, to_date)
            generate_answer(merged_df, [ID, FIRST_NAME, LAST_NAME, EMAIL], 10, CSV1)
            generate_answer(merged_df, [COUNTRY, COUNTRY_CODE], 3, CSV2)
            generate_answer(merged_df, [APPLICATION], 3, CSV3)
            logging.info(str(datetime.now())+': Successfully Created all Answer CSVs,' )

    except Exception as ex:
        logging.error(str(datetime.now())+': '+ str(ex))

def create_user_df():
    """Generate user data df"""
    user_df = pd.read_csv(DATA_PATH+USER_DATA+CSV, skipinitialspace=True)
    data_list = [user_df]
    for i in range(1, NO_OF_ACTIVITY_FILES):
        data_list.append(user_df)
    return pd.concat(data_list, ignore_index=True)


def create_activity_df():
    """Generate activity data df"""
    activity_data_list = []
    for i in range(1, NO_OF_ACTIVITY_FILES+1):
        activity_data_list.append(pd.read_csv(
            DATA_PATH+ACTIVITY+str(i)+CSV, skipinitialspace=True))

    return pd.concat(activity_data_list, ignore_index=True)


def filter_date(activity_df, f_date, t_date):
    """Filter Date"""
    activity_df[DATE] = pd.to_datetime(activity_df[DATE], format='%Y-%m-%d')
    activity_df = activity_df.loc[(activity_df[DATE] >= f_date)
                                  & (activity_df[DATE] < t_date)]

    return activity_df


def generate_answer(df, column_array, n, name):
    """Generate Answer"""
    df1 = df
    df1.dropna(subset=column_array, inplace=True)
    df1 = df.groupby(column_array).size().sort_values(
        ascending=False).reset_index(name=TOTAL_HITS)[0:n]
    df1.to_csv(CREATED_PATH+name+CSV, encoding=UTF8)
    logging.info(str(datetime.now())+': '+"Created "+ name)


if __name__ == '__main__':
    create_df(FROM_DATE, END_DATE)
