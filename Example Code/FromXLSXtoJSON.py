import pandas as pd

df = pd.read_excel("dataforgpsflot.xlsx")
df.to_json("data.json", orient='records')
