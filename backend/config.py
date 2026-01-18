import os
from dotenv import load_dotenv

## Simple configuration file to get api key without exposing it

load_dotenv() 

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')