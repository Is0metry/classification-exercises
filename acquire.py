import numpy as np
import pandas as pd
from env import get_db_url
import os
def clean_data_path(filename):
    if not filename.startswith('data/'):
        filename = 'data/' + filename
    if not filename.endswith('.csv'):
        filename = filename + '.csv'
    return filename
def build_dataframe(query,database,filename=''):
    if filename == '':
        filename += 'data/' + database + '.csv'
    else:
        filename = clean_data_path(filename)
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    url = get_db_url(database)
    df = pd.read_sql(query, url)
    df.to_csv(filename,index=False)
    return df

def get_titanic_data():
    query = '''
    SELECT * FROM passengers
    '''
    return build_dataframe(query, 'titanic_db','titanic')


def get_iris_data():
    query = '''
    SELECT * FROM measurements
    JOIN species USING(species_id)
    '''
    return build_dataframe(query,'iris_db','iris')

def get_telco_data():
    query = '''
    SELECT * FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id)
    '''
    return build_dataframe(query, 'telco_churn')
if __name__ == '__main__':
    print(get_titanic_data().head())
    print(get_iris_data().head())
    print(get_telco_data().head())
