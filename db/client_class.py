import pandas as pd
from experiments.preprocess import preproc, stopwords
from qdrant_client.http.models import models


class DataBaseClient:
    def __init__(self, qdrant_client, column_name):
        self.client = qdrant_client
        self.table = column_name

        self.names = pd.read_parquet('data/df_names_preproc.parquet')  # TODO ADD NEW FILE
        # self.names = .merge(df_emb[['name', 'emb']], how='left', left_on='Names', right_on='name')
        self.names = self.names.drop(columns=['languages_langdetect'])
        self.names = self.names.rename({'Names': 'original_name', 'name_preproc': 'preprocessed_name'}, axis=1)

    def get_collection(self):
        return self.client.get_collection(self.table)

    def get_point_by_id(self, ids):
        return self.client.retrieve(
            collection_name=self.table,
            ids=ids,
            with_payload=True,
            with_vectors=True
        )

    def check_for_name_in_db(self, company_name):
        search = self.names[self.names['original_name'] == company_name]
        if not search.empty:
            return 0, search['original_name'][0]

        preprocess_name = preproc(company_name, stopwords)
        search = self.names[self.names['preprocessed_name'] == preprocess_name]
        if not search.empty:
            return 1, search['original_name'][0]

        return 2, ""

    def search_in_qdrant_with_model_filtering(self, vector, original_name, limit, threshold):
        qdr_resp = self.client.search(
            collection_name=self.table,
            query_vector=vector,
            query_filter=models.Filter(
                must_not=[
                    models.FieldCondition(
                        key="original_name",
                        match=models.MatchValue(value=original_name)
                    ),
                ]
            ),
            limit=limit,
            offset=0
        )

        score = 0
        i = 0
        resp = []
        while score > threshold and i < len(qdr_resp):
            resp.append(qdr_resp[i])
            score = qdr_resp[i].result['score']
            i += 1

        return resp

