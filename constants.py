# PATH TO CHANGE:
# ASSIGNMENT 1
import os
cwd= os.getcwd()
ANSWER1 = str(cwd) +'/created_data/repos.csv'
ANSWER2 = str(cwd)+'/created_data/'

# ASSIGNMENT 2
PATH = str(cwd)
DATA_PATH = str(cwd)+'/datasets-master/'


# A1
URL = 'https://api.github.com/repositories?since=10000'
TOKEN_VALUE = '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'
AUTHERIZATION = 'Authorization'
TOKEN = 'token '
AUTH_TOKEN = 'auth_token '

COMMITS_CSV = '/commits.csv'
NESTED_AUTHOR = 'nested_author'
NESTED_COMMITTER = 'nested_committer'


# COLUMNS NAME
DESCRIPTION = 'description'
ID = 'id'
NAME = 'name'
FULL_NAME = 'full_name'
NODE_ID = 'node_id'
PRIVATE = 'private'
FORK = 'fork'
OWNER = 'owner'
OWNER_USERNAME = 'owner_username'
TYPE = 'type'
HTML_URL = 'html_url'
LOGIN = 'login'
SITE_ADMIN = 'site_admin'
OWNER_ADMIN = 'owner_site_admin'
OWNER_URL = 'owner_url'
OWNER_TYPE = 'owner_type'

COMMITS_URL = 'commits_url'
MESSAGE = 'message'
AUTHOR = 'author'
COMMIT = 'commit'
COMMITTER = 'committer'
EMAIL = 'email'
SHA = 'sha'

COMMIT_HASH = 'commit_hash'
COMMIT_MESSAGE = 'commit_message'
COMMIT_URL = 'commit_url'

AUTHOR_NAME = 'author_name'
AUTHOR_USERNAME = 'author_username'
AUTHOR_EMAIL = 'author_email'
AUTHOR_URL = 'author_url'

COMMITTER_NAME = 'committer_name'
COMMITTER_USERNAME = 'committer_username'
COMMITTER_EMAIL = 'committer_email'
COMMITTER_URL = 'committer_url'

# A2

CSV = '.csv'
USER_DATA = 'user_dataset'
ACTIVITY = 'activity_'
NO_OF_ACTIVITY_FILES = 5
UTF8 = 'utf-8'

HEADERS = {AUTHERIZATION: AUTH_TOKEN+TOKEN_VALUE}

# ARRAYS AND MAPS

DF_MAP = {OWNER_TYPE: TYPE, OWNER_URL: HTML_URL,
          OWNER_USERNAME: LOGIN, OWNER_ADMIN: SITE_ADMIN}
REPO_COLUMNS = [ID, NAME, FORK, FULL_NAME, OWNER_URL, OWNER_USERNAME, OWNER_ADMIN,
                PRIVATE, DESCRIPTION, NODE_ID, HTML_URL, OWNER_TYPE, COMMITS_URL]

COMMIT_COLUMNS = [COMMIT_HASH, COMMIT_URL, COMMIT_MESSAGE, AUTHOR_NAME, AUTHOR_EMAIL,
                  AUTHOR_USERNAME, AUTHOR_URL, COMMITTER_NAME, COMMITTER_EMAIL, COMMITTER_USERNAME, COMMITTER_URL]

COMMIT_COL_MAP = {AUTHOR_NAME:  NAME,
                  AUTHOR_EMAIL: EMAIL,
                  COMMITTER_NAME: NAME,
                  COMMITTER_EMAIL: EMAIL,
                  AUTHOR_USERNAME: LOGIN,
                  AUTHOR_URL: HTML_URL,
                  COMMITTER_USERNAME: LOGIN,
                  COMMITTER_URL:  HTML_URL,
                  COMMIT_MESSAGE: MESSAGE}

COMMIT_RENAME_MAP = {HTML_URL: COMMIT_URL, SHA: COMMIT_HASH}

# ERRORS
API_LIMIT = 'Api Limit Excedeed'
FOLDER_ALREADY_EXIST = 'folder already exist'