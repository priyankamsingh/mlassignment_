import pandas as pd
import numpy as np

def preprocess_data(df_1):
    # Loading required data

    
    # Drop columns which are not required
    df_1 = df_1.drop(['Unnamed: 0'], axis=1)

    # Code for Preprocessing steps as in provided notebook
    
    # 1. Missing value imputation; numerical columns with median values
    numerical_cols = [
        'BOUWJAAR_PAND',
        'VLOEROPPERVLAK_VERBLIJFSOBJECT',
        'age',
        'electricity_annual_consumption_estimated_offpeak',
        'electricity_annual_consumption_estimated_peak',
        'electricity_annual_consumption_estimated_total',
        'electricity_last_contract_annual_consumption_estimated_offpeak',
        'electricity_last_contract_annual_consumption_estimated_peak',
        'electricity_last_contract_annual_consumption_estimated_total',
        'gas_annual_consumption_estimated',
        'gas_last_contract_annual_consumption_estimated'
    ]
    for col in numerical_cols:
        if col in df_1.columns:
            fill_val = df_1[col].median()
            df_1[col].fillna(fill_val, inplace=True)
    
    # Impute categorical columns
    df_1[['electricity_last_contract_term', 'province']] = df_1[['electricity_last_contract_term', 'province']].fillna("onbekend")
    
    # Impute boolean columns
    boolean_cols = [
        'bought_toon',
        'has_active_boiler_rent_contract',
        'has_active_electricity_contract',
        'has_phone_number'
    ]
    for col in boolean_cols:
        if col in df_1.columns:
            fill_val = df_1[col].mode().head(1)[0]
            df_1[col].fillna(fill_val, inplace=True)
    
    # Check if there are any missing values remaining
    missing_values = df_1.isna().sum().sum()
    if missing_values > 0:
        print(f"There are still {missing_values} missing values after preprocessing.")
    df_1= pd.get_dummies(df_1, columns=['electricity_last_contract_term','province'], drop_first=True)
    
    return df_1