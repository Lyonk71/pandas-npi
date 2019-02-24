import pandas as pd
import numpy as np

def extract_nppes_subset(nppes_path='nppes.csv'):

    fields = ['NPI',
              'Entity Type Code',
              'Provider Organization Name (Legal Business Name)',
              'Provider First Name' ,
              'Provider Last Name (Legal Name)']

    df_nppes = pd.read_csv(nppes_path, usecols=fields, dtype=str)

    df_nppes['nppes_name'] = df_nppes['Provider Organization Name (Legal Business Name)'].fillna('') + df_nppes['Provider First Name'].fillna('') + " " + df_nppes['Provider Last Name (Legal Name)'].fillna('')
    df_nppes['nppes_name'] = df_nppes['nppes_name'].str.lower()
    df_nppes['nppes_name'] = df_nppes['nppes_name'].apply(lambda x: x.rstrip())
    df_nppes = df_nppes.drop(columns=['Provider Organization Name (Legal Business Name)', 'Provider First Name', 'Provider Last Name (Legal Name)'])
    df_nppes['Entity Type Code'] = df_nppes['Entity Type Code'].replace({'1':'provider', '2': 'facility', np.nan: 'deactivated'})

    df_nppes.to_csv('nppes_subset.csv', index=False)
