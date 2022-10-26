# company_names_matches

## Project overview
This project was developed as part of the Practical Deep Learning course of the ITMO University Master's Degree program  
In the process of work, it was necessary to create a service that, when receiving the name of the company, was able to determine whether we had met with this company, only under a different name, or not.  
During the operation of the service, the problem of matching is solved
## Project structure
* data - Contains the source data and the datasets obtained during processing 
* models - Contains models used for text processing
* experiments - contains notebooks with test processing experiments
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
1) pip install -r requirements.txt. We recommend using Python 3.9
2) Setup db. Check for this db/README.md
3) Setup models. Check for this models/README.md
4) To run program use terminal from project root and write:
```commandline
python -m app.match_names "yours_company_name" threshold(float) [limit(int)]
```

## Methods
The task to find same company based on another company input can be factorized as a matching problem. Basically it is similarity search between objects that represent companies. We use pretrained sentence-transformers models as base embedding models to represent companies in a common vector space. 
Metric Learning is a common approach for matching task. 
We use Similarity Learning where model is trained to learn similarity between objects by passing positive and negative objects to it. Our main tool for similarity learning is Quaterion. Similarity model acts like an Encoder, which consists of other encoders, and a Head Layer, which combines outputs of encoder components. This head layer redefines weights according to positive and negative input samples. 
As a storage we use Vector Search Engine called Qdrant. You can get it run with 2 commands:

    docker pull qdrant/qdrant
    docker run --name qdrant -d -p 6333:6333 --net=bridge qdrant/qdrant


## Evaluation
We evaluate our methods with basic retrieval metric called Precision@1.
Table 1. Precision@1 with different methods.
| Method\Model | distiluse-base-multilingual-cased-v2 | all-MiniLM-L6-v2 | all-MiniLM-L12-v2 | paraphrase-MiniLM-L6-v2 | paraphrase-MiniLM-L12-v2 | all-mpnet-base-v2 | LaBSE | paraphrase-multilingual-MiniLM-L12-v2 |
|--|--|--|--|--|--|--|--|--|
| Qdrant + Not Preprocessed | 0.3256 | 0.5746 | 0.5860 | 0.5817 | 0.5839 |  |  |
| Qdrant + Preprocessed | 0.4569 | 0.6183 | 0.6233 | 0.6248 | 0.6162 |  |  |
| Qdrant + Quanterion Preprocessed |  | 0.6205 |  | 0.6219 |  |  |  |

Based on table 1 we can conclude that processing is crucial step in this task as it dramatically increases quality of the model as well as fine tuning with similarity learning. Even though fine-tuning didn't gave us much of quality improvement there are a lot of room for future work and adjustments to similarity model.


## Team
Splitting a team:
1) Dmitry  - Manager, Organization of the team's work, etc...
2) Pavel - Processing text into vectors, comparing vectors. Description in the README
3) Margarita - Data processing, Description of processing in README


## Original data
You can find original data in folder data.
