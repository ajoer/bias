#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 
	Get summaries from input (Wikipedia biographies) with BERT extractive summarizer:
	- https://pypi.org/project/bert-extractive-summarizer/
	Input = json file where each key is a person name, and values are text length and text body.
	Output = json file where each key is a person name, and value is the summary. 
	NB: Only output summaries, where summary length is 5000 > X > 150 (heuristic).

"""

import argparse
import glob
import json
import os

from summarizer import Summarizer

parser = argparse.ArgumentParser(description='''''')
parser.add_argument("gender", help="file name, either men or women")

args = parser.parse_args()

input_file = f"data/wikipedia_raw/en_{args.gender}_summaries.json"
data = json.load(open(input_file))
model = Summarizer()

output_data = {}

for person in data:
	if data[person]["text_length"] < 150: continue
	text = data[person]["text"]
	result = model(text, min_length=60)
	full = ''.join(result)
	output_data[person] = full

with open(f'data/summaries/en_{args.gender}_bert_extractive.json', 'w') as outfile:
    json.dump(output_data, outfile)