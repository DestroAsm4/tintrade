from dotenv import dotenv_values
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
config = dotenv_values(dotenv_path)
TOKEN = config['TINVEST_TOKEN']