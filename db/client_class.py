import pandas as pd
from experiments.preprocess import preproc, stopwords


class DataBaseClient:
    def __init__(self, qdrant_client, column_name):
        self.client = qdrant_client
        self.table = column_name

        self.names = pd.read_parquet('data/df_names_preproc.parquet')  # TODO ADD NEW FILE
        # self.names = .merge(df_emb[['name', 'emb']], how='left', left_on='Names', right_on='name')
        self.names = self.names.drop(columns=['languages_langdetect'])
        self.names = self.names.rename({'Names': 'original_name', 'name_preproc': 'preprocessed_name'}, axis=1)
        print(self.names.head())

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
        print(preprocess_name)
        search = self.names[self.names['preprocessed_name'] == preprocess_name]
        print(search)
        if not search.empty:
            return 1, search['original_name'][0]

        return 2, ""
