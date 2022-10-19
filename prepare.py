from attr import validate
import pandas as pd
from sklearn.model_selection import train_test_split
def tvt_split(df:pd.DataFrame,stratify):
    train, test = train_test_split(df,test_size=.2,random_state=123,stratify=df[stratify])
    train, validate = train_test_split(train,test_size=.3,random_state=123,stratify=train[stratify])
    return train,validate,test
def prep_iris(iris_df):
    ret_df = iris_df.drop(columns=['species_id','measurement_id'])
    ret_df = ret_df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(ret_df[['species']])
    ret_df = pd.concat([ret_df,dummy_df],axis=1)
    return tvt_split(ret_df,'species')

def prep_titanic(titanic_df):
    titanic_df = titanic_df.drop(columns=['embarked','class','deck','age'])
    dummy_df = pd.get_dummies(titanic_df,columns=['sex','embark_town'])
    titanic_df = pd.concat([titanic_df,dummy_df],axis=1) 
    return tvt_split(titanic_df,'survived')