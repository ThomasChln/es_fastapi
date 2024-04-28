from fastapi import FastAPI
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
# Connect to Elasticsearch
es = Elasticsearch("http://es:9200")

app = FastAPI()

@app.get("/search/")
async def search(query: str):
    # Perform text embedding using SentenceTransformer
    model = SentenceTransformer('quora-distilbert-multilingual')
    embedding = model.encode(query, show_progress_bar=False)

    # Build the Elasticsearch script query
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": embedding.tolist()}
            }
        }
    }

    # Execute the search query
    search_results = es.search(index="test1", body={"query": script_query})

    # Process and return the search results
    results = search_results["hits"]["hits"]
    return {"results": results}
