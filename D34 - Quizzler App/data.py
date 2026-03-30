import requests
import pandas as pd

parameters = {
    "amount": 10,
    "type": "boolean",
}

api_call = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = api_call.json()
question_data = data["results"]

# Unnecessary but also works
# data_df = pd.DataFrame(data['results'])
# question_data = data_df.to_dict(orient="records")