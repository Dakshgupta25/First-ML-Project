import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv

def read_sql_data():
