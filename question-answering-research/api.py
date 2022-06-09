from fastapi import FastAPI
from haystack.document_stores.elasticsearch import ElasticsearchDocumentStore
from haystack.nodes import FARMReader, BM25Retriever
from haystack.pipelines import ExtractiveQAPipeline
doc_store = ElasticsearchDocumentStore(
    host='localhost',
    username='', password='',
    index='sampledata'
)
retriever = BM25Retriever(document_store=doc_store)
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
pipeline=ExtractiveQAPipeline(reader=reader,retriever=retriever)

app = FastAPI()

@app.get("/question")
async def query():
    return pipeline.run("Helpful Links about toilet training?")