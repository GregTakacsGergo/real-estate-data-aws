import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from decimal import Decimal

class ApartmentDataDatabase:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table_name = 'real_estate_market_data'
        self.table = self.dynamodb.Table(self.table_name)

    def ensure_table_exists(self):
        try:
            existing_tables = self.dynamodb.meta.client.list_tables()['TableNames']
            if self.table_name not in existing_tables:
                self.create_table()
            else: print("Table already exists so I won't create it again!")    
        except (NoCredentialsError, PartialCredentialsError) as e:
            print(f"Error with AWS credentials: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def create_table(self):
        self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'date',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'date',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        # Wait until the table exists.
        self.table.meta.client.get_waiter('table_exists').wait(TableName=self.table_name)
        print("Table created and is now active.")

    def check_existing_data(self, date):
        try:
            response = self.table.get_item(Key={'date': date})
            return 'Item' in response
        except Exception as e:
            print(f"Error checking existing data: {e}")
            return False

    def insert_data_db(self, date, universal_sqm_price_huf, universal_sqm_price_eur, one_million_huf_to_eur):
        if not self.check_existing_data(date):
            try:
                self.table.put_item(
                    Item={
                        'date': date,
                        'avg_sqm_price_huf': Decimal(universal_sqm_price_huf),
                        'avg_sqm_price_eur': Decimal(universal_sqm_price_eur),
                        'one_million_huf_to_eur': Decimal(one_million_huf_to_eur)
                    }
                )
                print("Data inserted successfully.")
            except Exception as e:
                print(f"Error inserting data: {e}")
        else:
            print("Data already exists in the database.")

    def fetch_data_from_db(self):
        try:
            response = self.table.scan()
            return response.get('Items', [])
        except Exception as e:
            print(f"Error fetching data from DB: {e}")
            return []

def main():
    handler = ApartmentDataDatabase()
    handler.ensure_table_exists()

    handler.insert_data_db('2024-07-04', 500000, 1300, 2)
    
    
if __name__ == "__main__":
    main()
