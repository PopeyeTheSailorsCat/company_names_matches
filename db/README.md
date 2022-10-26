# Data base setup.
1) Install files from:
<br>https://drive.google.com/drive/folders/1jgBJvnyaFJrMETpaaEqpSWwnVG44cgMn?usp=sharing  
To /data folder
2) Install and Run Docker Desktop.
3) Run in terminal: ```docker pull qdrant/qdrant```
4) ```docker run --name qdrant -d -p 6333:6333 --net=bridge qdrant/qdrant```  
Port is 6333. If you choose different change PORT in db/config.py. Local host hardcoded as 127.0.0.1. If you have different - change in same config.
5) Run from root of project ```python -m db.database``` to upload data to qdrant Docker. It may take some time, it finish then print "Done". You may get error, then restart and do nothing on your computer.
Now your database is set!
