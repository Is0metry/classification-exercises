from genericpath import isfile
import numpy as np
import pandas as pd
from env import get_db_url
import os

def get_titanic_data():
    filename = 'titanic.csv'
    if os.isfile(filename):
        return pd.read_csv(filename)
    url = get_db_url('titanic_db')
    query = '''
    SELECT * FROM passengers
    '''
    titanic_df = pd.read_sql(query,url)
    titanic_df.to_csv(filename)
    return titanic_df


def get_iris_data():
    filename = 'iris.csv'
    if os.isfile(filename):
        return pd.read_csv(filename)
    query = '''
    SELECT * FROM measurements
    JOIN species USING(species_id)
    '''
    url = get_db_url('iris')
    iris_df = pd.read_sql(query,url)
    iris_df.to_csv(filename)
    return iris_df

def get_telco_data():
    filename = 'telco.csv'
    if os.isfile(filename):
        return pd.read_csv(filename)
    url = get_db_url('telco_churn')
    query = '''
    SELECT * FROM employees
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id)
    '''
    df = pd.read_csv(query,url)
    df.to_csv(filename)
    return df