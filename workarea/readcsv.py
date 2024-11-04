import pandas as pd
import requests 

account_df = pd.read_csv("./scripts/data/account.csv")
print(account_df.head())

def print_random_quote():
    response = requests.get('https://zenquotes.io/api/random')
    quote = response.json()[0]['q']
    print('Quote of the day: "{}"'.format(quote))

print_random_quote()
