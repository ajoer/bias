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
from nltk import sent_tokenize
##### Todo: fix input text so there's space before all full stops.

parser = argparse.ArgumentParser(description='''''')
parser.add_argument("gender", help="file name, either men or women")
parser.add_argument("model", help="name of the summarization model to use, bert or textrank")

args = parser.parse_args()

input_file = f"data/wikipedia_raw/en_{args.gender}_summaries.json"
data = json.load(open(input_file))

if args.model == "bert":
	from summarizer import Summarizer
	model = Summarizer()

elif args.model == "textrank":
	from summa.summarizer import summarize

output_data = {}

def evaluate_summary_length(result):
	summary_sentences = sent_tokenize(result)
	if len(summary_sentences) < 6: return summary_sentences
	else: return None

def main():
	for person in data:
		text = data[person]["text"]
		all_sentences = sent_tokenize(text)
		if len(all_sentences) < 10: continue

		print(person)

		if args.model == "textrank":
			result = summarize(text)
			sentences = evaluate_summary_length(result)

		elif args.model == "bert":
			result = model(text)
			sentences = evaluate_summary_length(result)

		if sentences == None: continue
		out = ' '.join(x for x in sentences)
		output_data[person] = out

	with open(f'data/summaries/en_{args.gender}_{args.model}.json', 'w') as outfile:
	    json.dump(output_data, outfile, sort_keys=True, indent=4,)

if __name__ == "__main__":
	 main()