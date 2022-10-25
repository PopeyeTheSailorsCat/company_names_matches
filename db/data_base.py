import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from qdrant_client.http.models import models as qdrant_models
from db.client_class import DataBaseClient
import config



# LOCAL_HOST = "0.0.0.0"
def create_collection_and_upload(vectors, payload, ids, col_name, vec_shape, bs):
    qdrant_client.recreate_collection(collection_name=col_name,
                                      vectors_config=qdrant_models.VectorParams(size=vec_shape,
                                                                         distance=qdrant_models.Distance.COSINE),
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


def get_qdrant_client_():
    return DataBaseClient(QdrantClient(host=config.LOCAL_HOST, port=config.PORT), config.COL_NAME)


if __name__ == "__main__":
    embeddings = np.load('data/tuned_2.npy')

    df_emb = pd.read_parquet('data/df_embs_preproc.parquet')  # TODO to new version

    df_names = pd.read_parquet('data/df_names_preproc.parquet')
    df_names = df_names.merge(df_emb[['name', 'emb']], how='left', left_on='Names', right_on='name')
    df_names = df_names.drop(columns=['Names', 'languages_langdetect'])
    df_names = df_names.rename({'name': 'original_name', 'name_preproc': 'preprocessed_name'}, axis=1)

    qdrant_client = QdrantClient(host=config.LOCAL_HOST, port=config.PORT)
    #
    vectors = embeddings
    payload = df_names[['original_name', 'preprocessed_name']].to_dict(orient='records')
    ids = df_names.index.values.tolist()
    col_name = COL_NAME
    vec_shape = vectors.shape[1]
    bs = 1024
    col = create_collection_and_upload(vectors, payload, ids, col_name, vec_shape, bs)
    #
    print("done", col.points_count)

    # col = qdrant_client.get_collection(col_name)
    # print(col.dict())

# payload = df_names[['original_name', 'preprocessed_name']].to_dict(orient='records')
# # ids = df_emb.index.values.tolist()
# col_name = 'companies-ft'
# vec_shape = vectors.shape[1]
# bs = 1024
# col = create_collection_and_upload(vectors, payload, ids, col_name, vec_shape, bs)
