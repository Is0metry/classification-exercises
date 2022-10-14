from genericpath import isfile
from webbrowser import get
import numpy as np
import pandas as pd
from env import get_db_url
from os import path

def get_df_from_sql_cached(query,database,filename=''):
    if filename == '':
        filename = 'data/' + database + '.csv'
    if path.isfile(filename):
        return pd.read_csv(filename)
    url = get_db_url(database)
    df = pd.read_sql(query, url)
    df.to_csv(database + '.csv')
    return df

def get_titanic_data():
    query = '''
    SELECT * FROM passengers
    '''
    return get_df_from_sql_cached(query, 'titanic_db','titanic')


def get_iris_data():
    query = '''
    SELECT * FROM measurements
    JOIN species USING(species_id)
    '''
    return get_df_from_sql_cached(query,'iris_db','iris')

def get_telco_data():
    query = '''
    SELECT * FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id)
    '''
    return get_df_from_sql_cached(query, 'telco_churn')
if __name__ == '__main__':
    print(get_titanic_data().head())
    print(get_iris_data().head())
    print(get_telco_data().head())
