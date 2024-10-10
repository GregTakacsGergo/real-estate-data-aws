from apartment_data_fetcher import ApartmentDataFetcher
from dynamodb_handler import ApartmentDataDatabase
import json

def lambda_handler():
    url = "https://ingatlan.jofogas.hu/hajdu-bihar/debrecen/lakas?max_size=60&min_size=50&st=s"
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
