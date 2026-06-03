import pandas as pd

df = pd.read_csv(
    "output/transformed_policy_data.csv"
)

report = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Columns",
        "Average Premium"
    ],
    "Value": [
        len(df),
        len(df.columns),
        round(df["premium"].mean(), 2)
    ]
})

report.to_excel(
    "output/transformation_report.xlsx",
    index=False
)

print("Transformation Report Generated")
