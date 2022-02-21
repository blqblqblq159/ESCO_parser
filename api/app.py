import numpy as np
from flask import Flask, request
import pandas as pd
import json
app = Flask(__name__)

# Load some stuff
with open('distance_matrix.npy','rb') as f:
    distance_mat = np.load(f)

embed_df = pd.read_csv('skill_embed.csv')
init_sort = pd.read_csv('initial_skill_sort.csv')

#make some functions
def get_id(skill):
    for i,skill_name in enumerate(embed_df['name']):
        if skill_name == skill:
            return i
    raise ValueError('skill not found')

def sort_by_total_distance(skill_list):
    distance_list = []
    id_list = []
    for skill in skill_list:
        id_list.append(get_id(skill))
    for i in range(len(distance_mat)):
        if i not in id_list:
            total_distance = 0
            for idx in id_list:
                total_distance += distance_mat[i,idx]
            distance_list.append(total_distance)
    distances = np.array(distance_list)
    idx = np.argsort(distances)
    top_distances = distances[idx]
    return top_distances, idx


@app.route('/',methods=['GET'])
def return_init():
    names = list(init_sort['name'])
    weights = list(init_sort['weight'])
    transposed = []
    for a,b in zip(names,weights):
        transposed.append({a:b})
    return json.dumps(transposed)

@app.route('/skills',methods=['POST','GET'])
def return_closest_skills():
    skills = json.loads(request.data.decode('utf-8'))
    for skill in skills:
        print(skill)
    dists, idx = sort_by_total_distance(skills)
    skills = list(embed_df['name'][idx])
    transposed = []
    for a,b in zip(skills,dists):
        transposed.append({a:b})
    return json.dumps(transposed)
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)