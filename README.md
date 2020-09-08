# Bias

Data and code for bias and fairness evaluation of encoders.

The repo is structured as follows:

*resources/* contains the input files for extracting summaries from Wikipedia as well as the summarization models that have been tried out.
The names of the input files correspond to the Wikidata class the elements in the file belong to, e.g. "person" (with gender) and "natural disasters". *./old* contains initial trial data for Wikipedia pages on restaurants, films and speeches, in EN, DA and NL.

*data/* contains the raw Wikipedia data (wikipedia_raw/), the preprocessed data for the PreSumm summarisation model (wikipedia_bert/), and the summaries from each model in summaries/. 
The extracted summaries from Wikipedia along with the length of the summary. The files are JSON, each key is a page, each value a dictionary with the summary and the length of the summary. The naming in *data/* is the same as in *resources/*.
The preprocessed data has been sentence split and tokens \[CLS\] and \[SEP\] are added for sentence ends as per the [PreSumm](https://github.com/nlpyang/PreSumm/tree/main) documentation in the [paper](https://arxiv.org/pdf/1908.08345.pdf).
The files containing summaries are named according to the subject of the texts (e.g. "women") as well as the model that has produced the summaries. Currently the summaries folder contains summaries from [TextRank](https://github.com/summanlp/textrank/tree/master/summa) and [Bert Extractive Summarizer](https://pypi.org/project/bert-extractive-summarizer/).

*code/* contains the code for the project, so far: code for extracting the Wikipedia summaries, preprocessing for PreSumm and summary creation code for TextRank and Bert Extractive Summarizer. Later this will also include the analysis and visualisation code as well as resources and other data sources used in the project. 

## Data statistics and additional information
While there are data for more Wikidata classes, there are only summaries for "Women" and "Men" biographies from Wikipedia. These can be found in *data/summaries*.
The lists are extracted from Wikidata:
* Film = Q11424, cut off at 5000.
* Restaurants = Q11707, full list.
* Speeches = Q861911, full list.
* Aviation accident = Q744913, full list.
* Natural disasters = Q8065, full list.
* Women = Q6581072, cut off at 2500.
* Men = Q6581097, cut off at 2500

## Preprocessing
The two models currently in use, TextRank and Bert Extractive Summarizer, take raw text as input, and the input files have not been preprocessed beyond the initial extraction from Wikipedia.

For other ongoing work:
I didn't go with the CoreNLP toolkit preprocessing as described in the paper, as all was needed was sentence splits and additional tokens after each sentence. CoreNLP tokenizes as well, and although you can turn it off, it seemed overkill. To re-add, use either CoreNLP (in Java) or Stanza (same deal, and recommended for Python).
Only texts (Wikipedia summaries) with length >50 are included in the "bert" ready data (as per the PreSumm [paper](https://arxiv.org/pdf/1908.08345.pdf).)




