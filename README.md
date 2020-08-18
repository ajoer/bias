# Bias

Data and code for bias and fairness evaluation of encoders.

The repo is structured as follows:

*resources/* contains the input files for extracting summaries from Wikipedia. The names of the files correspond to the Wikidata class the elements in the file belong to, e.g. "person" (with gender) and "natural disasters". *./old* contains initial trial data for Wikipedia pages on restaurants, films and speeches, in EN, DA and NL.

*data/* contains the extracted summaries from Wikipedia along with the length of the summary. The files are JSON, each key is a page, each value a dictionary with the summary and the length of the summary. The naming in data/ is the same as in resources/

*code/* contains the code for the project. So far this is only the code for extracting the Wikipedia summaries. Later this will also include the analysis and visualization code as well as resources and other data sources used in the project. 

## Data statistics and additional information
The lists are extracted from Wikidata:
* Film = Q11424, cut off at 5000.
* Restaurants = Q11707, full list.
* Speeches = Q861911, full list.
* Aviation accident = Q744913, full list.
* Natural disasters = Q8065, full list.
* Women = Q6581072, cut off at 2500.
* Men = Q6581097, cut off at 2500.


