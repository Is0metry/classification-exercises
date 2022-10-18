import pandas as pd
def prep_iris(iris_df):
    ret_df = iris_df.drop(columns=['species_id','measurement_id'])
    ret_df = ret_df.rename(columns={'species_name':'species'})
    dummy_df = pd.get_dummies(ret_df[['species']])
    ret_df = pd.concat([ret_df,dummy_df],axis=1)
    return ret_df

def prep_titanic(titanic_df):
    ret_df = titanic_df.drop(columns=['embarked','class','deck','age'])
    dummy_df = pd.get_dummies(titanic_df,columns=['sex','embark_town'])
    ret_df = pd.concat([ret_df,dummy_df],axis=1) 
    return ret_df