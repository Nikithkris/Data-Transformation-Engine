import pandas as pd
import yaml

# Load Rules
with open("config/rules.yaml", "r") as file:
    rules = yaml.safe_load(file)

# Load Dataset
df = pd.read_csv(
    "input/regional_policy_data.csv"
)

# Rename Columns
df.rename(
    columns=rules["rename"],
    inplace=True
)

# Tax Calculation
tax_rate = rules["calculate"]["tax_rate"]

df["tax_amount"] = (
    df["premium"] * tax_rate / 100
)

# Total Premium
df["total_premium"] = (
    df["premium"] + df["tax_amount"]
)

print(df)
