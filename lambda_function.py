from apartment_data_fetcher import ApartmentDataFetcher
from dynamodb_handler import ApartmentDataDatabase
import json
from config import SCRAPING_TARGET 

def lambda_handler():
    url = SCRAPING_TARGET
    data_fetcher = ApartmentDataFetcher(url)
    apartment_data = data_fetcher.get_apartment_data()
    if apartment_data:
        date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur = apartment_data
        data = [str(date), universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur]
      
        
        db_handler = ApartmentDataDatabase()
        db_handler.insert_data_db(*data)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data fetched and saved successfully.')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to fetch apartment data.')
        }
lambda_handler()
