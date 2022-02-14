import pandas as pd
import json

df = pd.read_csv('title_uri_skills.csv')
expanded_list = []
for i, row in df.iterrows():
    title = row['job_title']
    uri = row['uri']
    for eSkill in row['essential_skills'].replace('[','').replace(']','').split(','):
        if eSkill:
            expanded_list.append([title, uri, eSkill, True])
    for oSkill in row['optional_skills'].replace('[','').replace(']','').split(','):
        if oSkill:
            expanded_list.append([title, uri, oSkill, False])
expanded_df = pd.DataFrame(expanded_list, columns=['job_title','uri','skill','essential'])
print(len(expanded_df))
#expanded_df.to_csv('expanded_title_uri_skills.csv',index=False)
