# skill recommender

Assuming a person has some subset of skills from the ESCO_dataset, recommend other skills from ESCO that the person is likely to also have.

## how to run the notebook

1. Set up the neo4j database locally
- create new database. Using 'admin' as password is recommended. Otherwise you will have to change the 'credentials.txt' to connect from the notebook to the database.
- copy the file expanded_title_uri_skills.csv into the import folder of the database
- from the database browser, run the first query in 'useful_queries.txt'. We now have the relevant portion of the ESCO dataset in neo4j.
- now run the following queries in 'useful_queries.txt' in order to set up the database for our algorithms in the notebook.

2. Run the notebook
- normally everything should go smoothly.
- calculating the distance matrix could take a long time (for me it took some 15 minutes) as it calculates all the pairwise distances between the ~15k skill embeddings, so about 225 million distances have to be calculated. But after this is done, we have a lookup table ready.
- It is recommended that you write distance_mat to file, so that you never have to recalculate it later. Note that this file will take up about 2GB memory.

