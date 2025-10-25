import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

BINARY_COLUMNS = ['default', 'housing', 'loan', 'deposit']
ONE_HOT_COLUMNS = ['job', 'marital', 'education', 'contact', 'month', 'poutcome']
NUMERIC_COLUMNS = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

def load_data(path):
    return pd.read_csv(path)

def replace_unknowns_with_nan(df):
    return df.replace('unknown', np.nan)

def impute_modes(df, cols):
    for c in cols:
        df[c] = df[c].fillna(df[c].mode()[0])
    return df

def fix_pdays(df):
    if 'pdays' in df.columns:
        df['pdays'] = df['pdays'].replace(-1, np.nan)
    return df

def encode_binaries(df):
    for c in BINARY_COLUMNS:
        df[c] = df[c].map({'yes': 1, 'no': 0})
    return df

def one_hot_encode(df):
    return pd.get_dummies(df, columns=ONE_HOT_COLUMNS, drop_first=True)

def scale_numeric(df):
    scaler = StandardScaler()
    df[NUMERIC_COLUMNS] = scaler.fit_transform(df[NUMERIC_COLUMNS])
    return df

def impute_numeric(df):
    df = df.copy()
    imp = SimpleImputer(strategy='median')
    existing = [c for c in NUMERIC_COLUMNS if c in df.columns]
    df[existing] = imp.fit_transform(df[existing])
    return df

def preprocess_pipeline(infile="data/bank.csv", outfile="data/bank_cleaned.csv"):
    df = load_data(infile)
    df = replace_unknowns_with_nan(df)
    df = impute_modes(df, ONE_HOT_COLUMNS)
    df = fix_pdays(df)
    df = impute_numeric(df)
    df = encode_binaries(df)
    df = one_hot_encode(df)
    df = scale_numeric(df)
    df.to_csv(outfile, index=False)
    print(f" Cleaned data saved to {outfile}")
    return df

if __name__ == "__main__":
    preprocess_pipeline()