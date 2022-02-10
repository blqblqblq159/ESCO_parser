import requests
import json
import pandas as pd

limit = 10000
url = f"https://ec.europa.eu/esco/api/search?language=en&type=occupation&limit={limit}"
s = requests.get(url)
response = json.loads(s.content.decode('utf-8'))
title_uri = []
for result in response['_embedded']['results']:
    title_uri.append([result['title'], result['_links']['self']['uri']])
df = pd.DataFrame(title_uri, columns=["job_title","uri"])
df.to_csv('title_uri.csv',index=False)
print(df.head())
print(len(df))
# with open('response.json','w') as f:
#     f.write(s.content.decode("utf-8"))
