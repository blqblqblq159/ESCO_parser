# Requirements

This API requires the distance_matrix.npy in the api folder.
This distance matrix is calculated in the skill_recommender/skill_recommender.ipynb notebook.

# API for skill recommendations

The API will run on localhost:5000
It has 2 available functions:

## GET request on localhost:5000

a GET request on localhost:5000 will yield an initial sort of the skills in the ESCO dataset, given no other skill is allocated.
This should be used to create the initial dropdown list of the front-end.
It yields a list of dictionaries. The list is sorted from most important initial skill to least important initial skill.
The dictionary contains the skill as a key and the importance as a value. The importance is a weighted measurement of the amount of skills that require said skill. (higher is better.) So the most important skill is required in the most occupations in the ESCO dataset.

## POST request in localhost:5000/skills

a POST request on localhost:5000/skills will yield a sorted list of the skills in the ESCO dataset, with the most recommended skill first, and the least recommended skill last.
The post request requires an input list, containing a string of every skill that is already allocated.
It then again returns a sorted list of dictionaries. the key of every dictionary contains the skill (as a string) and the value of every dictionary contains the total distance of the skill to the skill that are already allocated (lower is better)

## example

When the API (app.py) is running, you can run the script api_test.py. This gives an example of both previously detailed functionalities.
