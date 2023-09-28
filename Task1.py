import requests
import pandas as pd

try:
    responseData = requests.get("https://data.binance.com/api/v3/ticker/24hr")
    dataset = responseData.json()
    df = pd.DataFrame(dataset)
    df.to_csv("result_dataset.csv")
    print("Dataset created successfully\n")
except:
    print("Error occurred connecting with the file")
