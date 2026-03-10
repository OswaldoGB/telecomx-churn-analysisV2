import pandas as pd
import json

def load_json(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    df = pd.json_normalize(data)

    return df