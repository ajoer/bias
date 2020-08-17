#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 
	Get summaries from Wikipedia.
	For now, for English only. For other languages, get title of Wikipedia page, something like this:
		https://www.wikidata.org/w/api.php?action=wbgetentities&format=xml&props=sitelinks&ids=Q19675&sitefilter=frwiki

"""

import argparse
import json
from Wikipedia.wikipedia import wikipedia
from Wikipedia.wikipedia.exceptions import DisambiguationError, PageError

parser = argparse.ArgumentParser(description='''''')
parser.add_argument("language", default="en")
parser.add_argument("source", default="restaurants")

args = parser.parse_args()

def get_summary(event):

	try:
		event = '_'.join(x for x in list(event.strip().split()))
		print(event)
		try: 
			return wikipedia.summary(event)
		except (DisambiguationError, PageError) as e: 
			#print(e) 
			return None

	except ValueError:
		print("this event is not processed", line)
		return None

def main():
	input_data = set(open(f"resources/{args.language}_{args.source}.tsv").readlines())
	output_dictionary = {}
	wikipedia.set_lang(args.language)

	for line in input_data:
		if not line.startswith("http://www.wikidata.org/entity/"): continue
		event = line.strip().split("\t")[-1]

		summary = get_summary(event)
		if summary is None: continue
		output_dictionary[event] = summary
		
	with open(f"data/{args.language}_{args.source}_summaries.json", 'w') as outfile:
		json.dump(output_dictionary, outfile, indent=4)

if __name__ == "__main__":
	main()