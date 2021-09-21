import requests
import pandas as pd
from constants import *
import os

def get_repos(repo_count, max_commit_count):
    headers = {AUTHERIZATION: AUTH_TOKEN+TOKEN_VALUE}
    r = requests.get(URL,headers).json()
    df = pd.DataFrame.from_records(r)[0:repo_count]
    owner = df[OWNER]
    df[OWNER_TYPE] = owner.apply(lambda x: x[TYPE])
    df[OWNER_URL] = owner.apply(lambda x: x[HTML_URL])
    df[OWNER_USERNAME] = owner.apply(lambda x: x[LOGIN])
    df[OWNER_ADMIN] = owner.apply(lambda x: x[SITE_ADMIN])

    df = df[[ID,NAME,FORK ,FULL_NAME,OWNER_URL,OWNER_USERNAME,OWNER_ADMIN,
    PRIVATE, DESCRIPTION, NODE_ID, HTML_URL,OWNER_TYPE,COMMITS_URL]]
    
    
    k=0
    for url in df[COMMITS_URL]:
        url = url.replace('{/sha}','')
        response = requests.get(url,headers).json()
        try:
            msg = response['message']
            print(msg)
        except:
            print(url)
            commit_df = pd.DataFrame.from_records(response)[0:max_commit_count]
            commit = commit_df[COMMIT]
            author = commit_df[AUTHOR]
            committer = commit_df[COMMITTER]

            nested_author = commit.apply(lambda x: x[AUTHOR] if x is not None else '')
            nested_committer = commit.apply(lambda x: x[COMMITTER] if x is not None else '')
            
            commit_df[AUTHOR_NAME] = nested_author.apply(lambda x: x[NAME] if x is not None else '')
            commit_df[AUTHOR_EMAIL] = nested_author.apply(lambda x: x[EMAIL] if x is not None else '')
            commit_df[COMMITTER_NAME] = nested_committer.apply(lambda x: x[NAME] if x is not None else '')
            commit_df[COMMITTER_EMAIL] = nested_committer.apply(lambda x: x[EMAIL] if x is not None else '')

            commit_df[AUTHOR_USERNAME] = author.apply(lambda x: x[LOGIN] if x is not None else '')
            commit_df[AUTHOR_URL] = author.apply(lambda x: x[HTML_URL] if x is not None else '')
            commit_df[COMMITTER_USERNAME] = committer.apply(lambda x: x[LOGIN] if x is not None else '')
            commit_df[COMMITTER_URL] = committer.apply(lambda x: x[HTML_URL] if x is not None else '')
            
            commit_df[COMMIT_MESSAGE] = commit.apply(lambda x: x[MESSAGE] if x is not None else '')
            commit_df = commit_df.rename(columns={HTML_URL:COMMIT_URL,SHA:COMMIT_HASH})

            
            commit_df = commit_df[[COMMIT_HASH,COMMIT_URL,COMMIT_MESSAGE,AUTHOR_NAME,AUTHOR_EMAIL,
            AUTHOR_USERNAME,AUTHOR_URL,COMMITTER_NAME,COMMITTER_EMAIL,COMMITTER_USERNAME,COMMITTER_URL]]
            repo_name = df[NAME][k]
            try:
                os.mkdir(ANSWER2+repo_name)
            except Exception as ex:
                pass

            commit_df.to_csv(ANSWER2+repo_name+COMMITS_CSV, encoding=UTF8)
            k+=1

    df.to_csv(ANSWER1, encoding=UTF8)

get_repos(4, 4)