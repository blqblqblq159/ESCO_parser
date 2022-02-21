import json
import requests


#test of initial
print(json.loads(requests.get("http://127.0.0.1:5000/").content)[0:5])
print('')

#test with input 'dance' and 'maintain safe working conditions in performing arts'
print(json.loads(requests.post("http://127.0.0.1:5000/skills", data=json.dumps(['dance','maintain safe working conditions in performing arts'])).content)[0:5])