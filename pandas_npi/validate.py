import pandas as pd
import numpy as np


# reference abbreviations for street names
from pkg_resources import resource_filename
nppes_filepath = resource_filename(__name__, 'nppes_subset.csv')



def clean_npi_field(dfa, npi_column):
    dfa[npi_column] = dfa[npi_column].astype(str)
    dfa[npi_column] = dfa[npi_column].replace("[.][0-9]+$", '', regex=True)
    dfa[npi_column] = dfa[npi_column].replace('[^\d]','', regex=True)
    dfa = dfa[dfa[npi_column].str.len()==10].copy()

def remove_filler_npi(x):
    if x == '9999999999':
        return np.nan
    elif x == '8888888888':
        return np.nan
    elif x == '7777777777':
        return np.nan
    elif x == '6666666666':
        return np.nan
    elif x == '5555555555':
        return np.nan
    elif x == '4444444444':
        return np.nan
    elif x == '3333333333':
        return np.nan
    elif x == '2222222222':
        return np.nan
    elif x == '1111111111':
        return np.nan
    else:
        return x
    
fields = ['NPI',
          'Entity Type Code',
          'nppes_name']
        
def clear_previous(df):
    try:
        return df.drop(columns=['Entity Type Code', 'nppes_name'])
    except:
        return df

def validate(df, npi_field, nppes_path=nppes_filepath):
    df = clear_previous(df)
    df_nppes = pd.read_csv(nppes_path, usecols=fields, dtype=str)
    df_nppes = df_nppes.rename({'NPI': npi_field}, axis=1)
    clean_npi_field(df, npi_field)
    clean_npi_field(df_nppes, npi_field)
    df[npi_field] = df[npi_field].apply(lambda x: remove_filler_npi(x))
    df_nppes[npi_field] = df_nppes[npi_field].apply(lambda x: remove_filler_npi(x))
    df = df.merge(df_nppes, how='left', on=npi_field)
    df['Entity Type Code'] = df['Entity Type Code'].fillna('invalid')
    return df