import pandas as pd
import numpy as np
from typing import Union,Tuple
from acquire import get_iris_data, get_titanic_data, get_telco_data
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
def tvt_split(df:pd.DataFrame,stratify:Union[str,pd.Series] = None,test_split:float = .2,validate_split:int = .3):
    '''This function takes a pandas DataFrame as well as either a string or pd.Series and returns a train, validate and test split of the DataFame'''
    if type(stratify) is str:
        strat = df[stratify]
    else:
        strat = stratify
    train_validate, test = train_test_split(df,test_size=test_split,random_state=123,stratify=strat)
    strat = train_validate[stratify]
    train, validate = train_test_split(train_validate,test_size=validate_split,random_state=123,stratify=strat)
    return train,validate,test
def prep_iris(iris_df):
    ret_df = iris_df.drop(columns=['species_id','measurement_id'])
    ret_df = ret_df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(ret_df[['species']])
    ret_df = pd.concat([ret_df,dummy_df],axis=1)
    return tvt_split(ret_df,'species')

def prep_titanic(titanic_df,dummies:bool = True):
    ret_df = titanic_df.drop(columns=['embarked','class','deck'])
    if dummies:
        ret_df = pd.get_dummies(ret_df,columns=['sex','embark_town'])
    train,validate,test = tvt_split(ret_df,'survived')
    imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
    imputer = imputer.fit(train[['age']])
    train['age'] = imputer.transform(train[['age']])
    validate['age'] = imputer.transform(validate[['age']])
    test['age'] = imputer.transform(test[['age']])
    return train,validate,test


def clean_rows(row:pd.Series):
    cols_to_clean = ['multiple_lines','online_security','online_backup','device_protection','tech_support','streaming_tv','streaming_movies']
    for c in cols_to_clean:
        if 'service' in row[c]:
            row[c] = 'No'
    return row
def prep_telco(telco_df):
    telco_df = telco_df.drop(['payment_type_id','internet_service_type_id','contract_type_id'],axis=1)
    telco_df = telco_df.apply(clean_rows,axis='columns')
    return tvt_split(telco_df)
def get_prepared_iris()-> Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    '''Returns a prepared version of the iris dataset'''
    return prep_iris(get_iris_data())
def get_prepared_titanic()-> Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    return prep_titanic(get_titanic_data())
def get_prepared_telco()-> Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    return prep_telco(get_telco_data())