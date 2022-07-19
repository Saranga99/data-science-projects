import os
from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

def summarize(text):
    summary_text = summarizer(text, max_length=100, min_length=5, do_sample=False)[0]['summary_text']
    print(summary_text)
    return summary_text

