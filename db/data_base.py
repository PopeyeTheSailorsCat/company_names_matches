import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from qdrant_client.http.models import models

LOCAL_HOST = "127.0.0.1"
PORT = 6333

# LOCAL_HOST = "0.0.0.0"
def create_collection_and_upload(vectors, payload, ids, col_name, vec_shape, bs):
    qdrant_client.recreate_collection(collection_name=col_name,
                                      vectors_config=models.VectorParams(size=vec_shape,
                                                                         distance=models.Distance.COSINE),
                                      on_disk_payload=True)
    qdrant_client.upload_collection(
        collection_name=col_name,
        vectors=vectors,
        payload=payload,
        ids=ids,
        batch_size=bs,
        parallel=6
    )
    col = qdrant_client.get_collection(col_name)
    return col


if __name__ == "__main__":
    df_embs = pd.read_parquet('data/df_embs_en.parquet')
    qdrant_client = QdrantClient(host=LOCAL_HOST, port=PORT)
    #
    vectors = np.stack(df_embs.emb)
    payload = df_embs[['name']].to_dict(orient='records')
    ids = df_embs.index.values.tolist()
    col_name = 'companies-EN'
    vec_shape = vectors.shape[1]
    bs = 1024
    #
    col = create_collection_and_upload(vectors, payload, ids, col_name, vec_shape, bs)
    print("done", col.points_count)

    # col = qdrant_client.get_collection(col_name)
    # print(col.dict())
