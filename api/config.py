import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_PORT = os.getenv('FLASK_PORT')
    REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')