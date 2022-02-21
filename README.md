# skill recommender

Assuming a person has some subset of skills from the ESCO_dataset, recommend other skills from ESCO that the person is likely to also have.

## how to run the notebook

1. Set up the neo4j database locally
- create new database. Using 'admin' as password is recommended. Otherwise you will have to change the 'credentials.txt' to connect from the notebook to the database.
- copy the files 'data/expanded_title_uri_skills.csv' and 'data/expanded_df_with_skills.csv' into the import folder of the database
- from the database browser, run the fqueries in 'useful_queries.txt'. We now have the relevant portion of the ESCO dataset in neo4j.

2. Run the notebooks
- normally everything should go smoothly.
- calculating the distance matrix could take a long time (for me it took some 15 minutes) as it calculates all the pairwise distances between the ~15k skill embeddings, so about 225 million distances have to be calculated. But after this is done, we have a lookup table ready.
- It is recommended that you write distance_mat to file, so that you never have to recalculate it later. Note that this file will take up about 2GB memory.

# job recommender

We randomly assign people from the dataset 'New_LinkedIn_users.csv' (in folder data) skills from the ESCO dataset based on their job history. From this linked dataset, we implement 2 recommendation patterns:
1. for each person, we predict which ESCO occupations they are likely to be proficient at.
2. for each ESCO occupation, we predict which people in our dataset are likely to be proficient at this occupation

## how to run the notebook

1. local neo4j database
- We use the same database as in the skill recommender notebook.

2. Run the notebook
- There's no special distance calculation here, The node2vec algorithm may take a while to run, but other than that everything should be fine.
