import requests
import json
import pandas as pd
import time

def get_url(url):
    try:
        return requests.get(url)
    except:
        print("\nrequest failed. trying again in 10 minutes")
        time.sleep(600)
        return get_url(url)


limit = 10000
url = f"https://ec.europa.eu/esco/api/search?language=en&type=occupation&limit={limit}"
def skill_url(uri):
    return f"https://ec.europa.eu/esco/api/resource/occupation?uri={uri}&language=en"
s = get_url(url)
response = json.loads(s.content.decode('utf-8'))
title_uri = []
for counter, result in enumerate(response['_embedded']['results']):
    print(f"processing job title number {counter+1}...",end = '\r')
    skill_get = get_url(skill_url(result['_links']['self']['uri']))
    skill_response = json.loads(skill_get.content.decode('utf-8'))
    essential_skills = []
    optional_skills = []
    try:
        for skill in skill_response['_links']['hasEssentialSkill']:
            essential_skills.append(skill['title'])
    except:
        pass
    try:
        for skill in skill_response['_links']['hasOptionalSkill']:
            optional_skills.append(skill['title'])
    except:
        pass
    title_uri.append([result['title'], result['_links']['self']['uri'],essential_skills,optional_skills])
df = pd.DataFrame(title_uri, columns=["job_title","uri","essential_skills","optional_skills"])
df.to_csv('title_uri_skills.csv',index=False)
# print(df.head())
# print(len(df))
# with open('response.json','w') as f:
#     f.write(s.content.decode("utf-8"))

# url = "https://ec.europa.eu/esco/api/resource/occupation?uri=http://data.europa.eu/esco/occupation/52df9d56-efd4-48d0-ad93-59231943fc4c"
# s=requests.get(url)
# with open('response.json','w') as f:
#     f.write(s.content.decode('utf-8'))

