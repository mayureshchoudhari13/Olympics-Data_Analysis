import pandas as pd
import numpy as np

def preprocess(df,region_df):

    # filter data for summer olympics
    df = df[df['Season']=='Summer']
    # merge with the region_df
    df = df.merge(region_df,on='NOC',how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medels
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis = 1)
    return df



