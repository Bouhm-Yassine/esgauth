import os

from dotenv import load_dotenv

load_dotenv()

def read_env():
    print('====== READ')
    print(os.getenv('ABCD'))