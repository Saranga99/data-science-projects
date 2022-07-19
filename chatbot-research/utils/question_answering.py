import torch
import numpy as np
import pandas as pd

from transformers import BertTokenizer
from transformers import BertForQuestionAnswering

model = BertForQuestionAnswering.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')


def question_answer(question, text):
    predicted_answers = []
    input_ids = tokenizer.encode(question, text)

    tokens = tokenizer.convert_ids_to_tokens(input_ids)

    sep_idx = input_ids.index(tokenizer.sep_token_id)
    num_seg_a = sep_idx+1
    num_seg_b = len(input_ids) - num_seg_a

    segment_ids = [0]*num_seg_a + [1]*num_seg_b
    assert len(segment_ids) == len(input_ids)

    output = model(torch.tensor([input_ids]),
                   token_type_ids=torch.tensor([segment_ids]))

    answer_start = torch.argmax(output.start_logits)
    answer_end = torch.argmax(output.end_logits)
    if answer_end >= answer_start:
        answer = tokens[answer_start]


        for i in range(answer_start+1, answer_end+1):
            if tokens[i][0:2] == "##":
                answer += tokens[i][2:]
            else:
                answer += " " + tokens[i]

    if answer.startswith("[CLS]"):
        answer = "Unable to find the answer to your question."

    answer = ("\nAnswer to your question is  \n{}".format(answer.capitalize()))
    # predicted_answers.append(answer.capitalize())
    return answer
