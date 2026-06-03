import pandas as pd

def validate_data(df):

    issues = []

    if df.isnull().sum().sum() > 0:
        issues.append("Missing Values Found")

    if df.duplicated().sum() > 0:
        issues.append("Duplicate Records Found")

    if (df["premium"] <= 0).sum() > 0:
        issues.append("Invalid Premium Values")

    return issues
