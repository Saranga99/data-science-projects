import os
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.utils import clean_wiki_text, convert_files_to_docs, print_answers
from haystack.retriever.dense import DensePassageRetriever
from haystack.reader import FARMReader
from haystack.pipelines import ExtractiveQAPipeline


class QAPipeline():
    class_name = os.path.basename(__file__)
    def __init__(self) -> None:
        # Connect to Elasticsearch
        document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="sampledata")
        doc_dir = "../data/sampleData"
        docs = convert_files_to_docs(dir_path=doc_dir, clean_func=clean_wiki_text, split_paragraphs=True)
        document_store.write_documents(docs)

        #retriever
        self.retriever=DensePassageRetriever.load("models/retriever",document_store)
        #reader
        self.reader=FARMReader(model_name_or_path="models/reader")
        #pipeline
        self.pipe = ExtractiveQAPipeline(self.reader, self.retriever)
    
    def get_content(self,question):
        content=self.retriever.retrieve(question)
        return content
    
    def get_answers(self,question):
        answers=self.pipe.run(question)
        return answers