import glob
import json
import os
#import stanza

input_directory = glob.glob("../data/wikipedia_summaries_raw/*.json")

# stanza.download('en', logging_level='WARN')
# nlp = stanza.Pipeline('en', processors='tokenize')

end_punct = "!?."

for file in input_directory:
	data = json.load(open(file))

	out_directory = file.replace("raw", "bert").replace("_summaries.json", "/")

	if not os.path.exists(out_directory):
		os.makedirs(out_directory)

	for article in sorted(data):
		article_name = '_'.join(x for x in article.split()).replace("/", "_")
		outfile_name = f"{article_name}.txt"
		outfile = open(out_directory+outfile_name, "w")

		sentence_split_data = []
		if data[article]["text_length"] < 50: continue
		for word in data[article]["text"].split():
			sentence_split_data.append(word)
			if word[-1] in end_punct:
				sentence_split_data.append("[CLS] [SEP]")

		outfile.write(" ".join(sent for sent in sentence_split_data)+"\n\n")
		outfile.close()


