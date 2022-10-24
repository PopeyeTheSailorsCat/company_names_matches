from quaterion_models import SimilarityModel
import numpy as np
from experiments.preprocess import preproc, stopwords
import os
import random
import sys
from typing import Any, Dict, List, Union

from quaterion_models.encoders import Encoder
from quaterion_models.types import CollateFnType

from sentence_transformers import SentenceTransformer

PRETRAIN = 'all-MiniLM-L6-v2'


class CompanyEncoder(Encoder):
    def __init__(self, pretrained_name: str):
        super().__init__()
        self.encoder = SentenceTransformer(pretrained_name)
        self._pretrained_name = pretrained_name

    @property
    def trainable(self) -> bool:
        return False

    @property
    def embedding_size(self) -> int:
        return self.encoder.get_sentence_embedding_dimension()

    def get_collate_fn(self) -> CollateFnType:
        return self.extract_texts

    def extract_texts(self, batch: List[Union[str, Dict[str, Any]]]):
        if isinstance(batch[0], str):
            return batch
        elif isinstance(batch[0], Dict):
            return [item["preprocessed_name"] for item in batch]
        else:
            raise TypeError("Expecting list of strings or dicts as inputs")

    def forward(self, inputs):
        return self.encoder.encode(
            inputs, convert_to_numpy=False, convert_to_tensor=True
        )

    def save(self, output_path: str):
        self.encoder.save(os.path.join(output_path, self._pretrained_name))

    @classmethod
    def load(cls, input_path: str) -> "Encoder":
        return CompanyEncoder(input_path)


def inference(company_name_original, db_client, threshold, limit=10, df_embs=None, preproc_text=False,
              debug=False):
    enc = CompanyEncoder(pretrained_name=PRETRAIN)
    setattr(sys.modules["__main__"], 'CompanyEncoder', enc)
    model = SimilarityModel.load('models/companies_2')
    model.eval()

    # model.to('cuda')
    if preproc_text:
        company_name = preproc(company_name_original, stopwords)
    else:
        company_name = company_name_original

    if debug:
        print(f'company name:{company_name}')

    if df_embs is None:
        qvector = model.encode(company_name)
    else:
        qvector = np.stack(df_embs[df_embs['name'] == company_name].emb)[0]

    if qvector.shape[0] == 1:
        qvector = qvector[0]

    search_result = db_client.search_in_qdrant_with_model_filtering(qvector, company_name_original, limit, threshold)

    return search_result  # [r for r in search_result if r.payload['name'] != company_name]
