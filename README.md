# company_names_matches

## Project overview
This project was developed as part of the Practical Deep Learning course of the ITMO University Master's Degree program  
In the process of work, it was necessary to create a service that, when receiving the name of the company, was able to determine whether we had met with this company, only under a different name, or not.  
During the operation of the service, the problem of matching is solved
## Project structure
* data - Contains the source data and the datasets obtained during processing 
* models - Contains models used for text processing
* app - Contains the code responsible for the operation of the service
* db - Contains code related to the operation of the company database
* dev - Contains the code that was used during the development of the service

## Project architecture
Through the written interface, a request in the form of a company name is submitted to the program. The company name passes through the pre-trained Bert and is translated into a vector representation. We have built a database of company names and their instances on the training dataset. Vectors are matched in the database with the vector of the received company name. If a match is found, other names of this company are displayed. Otherwise, it is reported that no work has been carried out with such a company. A request is made to the user for permission to add this company to the database.

## Project RoadMap
At this stage, the expected development path looks like this: 

0) Repository maintenance
   - Maintain up-to-date information in the repository

1) Data processing
   - View data in Jupiter
   - Change the data format to tsv
   - Remove quotes
   - Remove broken lines

2) Berta (Pre - trained public)
   - Download and use
   - View different pretrain

3) Metric learning (Quaterion)
   - Explore how to do
   - Make a MVP
   - Compare different approaches

4) DB (Parquet, vector db, Qdrant):  
FORMAT: u_id, name, vector, Id_instance <- the universal designation of the company
   - View existing solutions
   - Select db

5) Configure the database to work with models:
   * Fill in the database using Bert-s and known identical companies
   * Make the process of the database working with models when researching a new name 
   * Adding a new entity to the database-a company

6) Make a startup interface

## Run program
To run program use terminal crom project root and write:
```commandline
python app/match_names.py yours_company_name
```

## Team
Splitting a team:
1) Dmitry  - Manager, Organization of the team's work, etc...
2) Pavel - Processing text into vectors, comparing vectors. Description in the README
3) Margarita - Data processing, Description of processing in README


## Original data
You can find original data by path data/train.csv
