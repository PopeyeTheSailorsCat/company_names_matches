# Data base setup.
1) Install .parquet files from:
<br>https://drive.google.com/drive/folders/1jgBJvnyaFJrMETpaaEqpSWwnVG44cgMn?usp=sharing  
To /data folder
2) Install Docker Desktop.
3) Run in terminal: ```docker pull qdrant/qdrant```
4) ```docker run --name qdrant -d -p 6333:6333 --net=bridge qdrant/qdrant```  
Port is 6333. If you choose diffenet change PORT in data_base.py
5) Run from root ```python db/data_base.py``` to upload data to qdrant Docker.  
Now your database is set!