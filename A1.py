import requests
import pandas as pd
from constants import *
import os
import logging
from datetime import datetime
logging.basicConfig(filename=str(os.getcwd()) +
                    '/logs/A1.log', level=logging.DEBUG)

REPO_COUNT = 6
MAX_COMMITS = 8


def make_api_call(repo_count, max_commit_count):
    """Make Authenticated api call to github API"""
    r = requests.get(URL, HEADERS).json()
    try:
        df = pd.DataFrame.from_records(r)[0:repo_count]
        create_repos_csv(df, max_commit_count)
        logging.info(str(datetime.now())+': Succesfully Created answer CSVs')
    except Exception as ex:
        logging.error(str(datetime.now())+':'+str(ex)+API_LIMIT)


def create_repos_csv(df, max_commit_count):
    """Create Repos Csv"""
    for key, value in DF_MAP.items():
        df = add_new_col(key, value, df[OWNER], df)
    df = df[REPO_COLUMNS]
    create_commits_csv(df, max_commit_count)
    df.to_csv(ANSWER1, encoding=UTF8)


def create_commits_csv(df, max_commit_count):
    """Create Commits Csv"""
    k = 0
    for url in df[COMMITS_URL]:
        url = url.replace('{/sha}', '')
        response = requests.get(url, HEADERS).json()
        repo_name = df[NAME][k]
        try:
            msg = response[MESSAGE]
            logging.error(str(datetime.now())+': ' +repo_name+': Empty Repository')
        except Exception as ex:
            commit_df = pd.DataFrame.from_records(
                response)[0:max_commit_count]
            
            util_map = create_util_df_map(commit_df)
            for i, j in COMMIT_COL_MAP.items():
                temp_df = get_temp_df(i, util_map)
                commit_df = add_new_col(i, j, temp_df, commit_df)

            commit_df = commit_df.rename(columns=COMMIT_RENAME_MAP)[COMMIT_COLUMNS]
            create_directory(repo_name)
            commit_df.to_csv(ANSWER2+repo_name+COMMITS_CSV, encoding=UTF8)
            logging.info(str(datetime.now()) +': Created Commits file for '+repo_name)
        k += 1


def create_util_df_map(commit_df):
    """Create Util Map"""
    commit = commit_df[COMMIT]
    return {
        COMMIT: commit,
        AUTHOR: commit_df[AUTHOR],
        COMMITTER: commit_df[COMMITTER],
        NESTED_AUTHOR: commit.apply(
            lambda x: x[AUTHOR] if x is not None else ''),
        NESTED_COMMITTER: commit.apply(
            lambda x: x[COMMITTER] if x is not None else '')
    }


def create_directory(repo_name):
    """Create Directory"""
    try:
        os.mkdir(ANSWER2+repo_name)
        logging.info(str(datetime.now()) +
                     ': Created Directory for repo - > '+repo_name)
    except Exception as ex:
        logging.info(str(datetime.now())+': '+repo_name+': '+str(ex))


def add_new_col(required_name, present_name, temp_df, final_df):
    """Add new Columns in the Dataframe"""
    final_df[required_name] = temp_df.apply(
        lambda x: x[present_name] if x is not None else '')
    return final_df


def get_temp_df(i, util_map):
    """Get temp df"""
    if i == AUTHOR_NAME or i == AUTHOR_EMAIL:
        return util_map[NESTED_AUTHOR]
    elif i == COMMITTER_NAME or i == COMMITTER_EMAIL:
        return util_map[NESTED_COMMITTER]
    elif i == AUTHOR_USERNAME or i == AUTHOR_URL:
        return util_map[AUTHOR]
    elif i == COMMITTER_USERNAME or i == COMMITTER_URL:
        return util_map[COMMITTER]
    elif i == COMMIT_MESSAGE:
        return util_map[COMMIT]


if __name__ == '__main__':
    """Main Function Change the variables"""
    make_api_call(REPO_COUNT, MAX_COMMITS)
