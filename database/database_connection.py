from sqlalchemy import create_engine
import pandas as pd

class NFLDatabase:
    def __init__(self, username, password, host='localhost', database='nfl_database'):
        # Build connection string
        self.connection_string = f'postgresql://{username}:{password}@{host}/{database}'
        self.engine = create_engine(self.connection_string)
        
    def test_connection(self):
        """Test if database connection works"""
        try:
            with self.engine.connect() as conn:
                result = conn.execute("SELECT 1")
                print("Database connection successful!")
                return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
            
    def load_dataframe(self, df, table_name, if_exists='replace'):
        """Load pandas DataFrame into database table"""
        try:
            df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
            print(f"Successfully loaded {len(df)} records to {table_name}")
        except Exception as e:
            print(f"Failed to load data: {e}")