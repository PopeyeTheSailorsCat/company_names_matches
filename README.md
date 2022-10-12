# company_names_matches

## Project overview
This project was developed as part of the Practical Deep Learning course of the ITMO University Master's Degree program  
In the process of work, it was necessary to create a service that, when receiving the name of the company, was able to determine whether we had met with this company, only under a different name, or not.  
During the operation of the service, the problem of matching is solved
## Project structure
* data - Contains the source data and the datasets obtained during processing 
* model - Contains models used for text processing
* app - Contains the code responsible for the operation of the service
* db - Contains code related to the operation of the company database
* dev - Contains the code that was used during the development of the service

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

## Team
Splitting a team:
1) Dmitry  - Manager, Organization of the team's work, etc...
2) Pavel - Processing text into vectors, comparing vectors. Description in the README
3) Margarita - Data processing, Description of processing in README
