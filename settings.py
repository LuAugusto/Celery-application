from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    MONGO_DB_URL=os.getenv('MONGO_DB_URL')
    WEATHER_API_URL=os.getenv('WEATHER_API_URL')
    KEY=os.getenv('KEY')
    KEY_TEST=os.getenv('KEY_TEST')
    COLLECTION_FORECAST=os.getenv('COLLECTION_FORECAST')
    COLLECTION_LOCATION=os.getenv('COLLECTION_LOCATION')
    COLLECTION_LOGS_ERROR=os.getenv('COLLECTION_LOGS_ERROR')
    RABBIT_MQ_BROKER=os.getenv('RABBIT_MQ_BROKER')
    COUNTRY='PT'
    DAYS=5
    
variables = Settings()