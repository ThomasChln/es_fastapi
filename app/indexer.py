from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import json

# Connect to Elasticsearch
es = Elasticsearch("http://es:9200")

# Index name
index_name = "test1"

# Example data
#f = open('app/epmc_1700_suic_ftext.json')
f = open('app/epmc_suic_ftext.json')
data = json.load(f)

# Create Elasticsearch index and mapping
if not es.indices.exists(index=index_name):
    es_index = {
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": 768}
            }
        }
    }
    es.indices.create(index=index_name, body=es_index, ignore=[400])

# Upload documents to Elasticsearch with text embeddings
model = SentenceTransformer('quora-distilbert-multilingual')

for doc in data:
    # Calculate text embeddings using the SentenceTransformer model
    embedding = model.encode(doc["text"], show_progress_bar=False)

    # Create document with text and embedding
    document = {
        "text": doc["text"],
        "embedding": embedding.tolist()
    }

    # Index the document in Elasticsearch
    es.index(index=index_name, id=doc["id"], body=document)

f.close()
