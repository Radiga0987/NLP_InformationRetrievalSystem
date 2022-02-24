from util import *

# Add your import statements here

import nltk
nltk.download('wordnet')

class InflectionReduction:

	def __init__(self):
		self.stemmer = nltk.stem.SnowballStemmer('english')
		self.lemmatizer = nltk.stem.WordNetLemmatizer()

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""
		
		isStem = True
		
		if isStem:
			reducedText = self.stem(text)
		else:
			reducedText = self.lemmatize(text)

		return reducedText

	def stem(self, text):
		"""
		Stemming using the Snowball stemmer from NLTK
		https://stackoverflow.com/questions/24647400/what-is-the-best-stemming-method-in-python
		
		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed tokens representing a sentence
		"""
		
		reducedText = [[self.stemmer.stem(token) for token in sent] for sent in text]
		
		return reducedText

	def lemmatize(self, text):
		"""
		Lemmatization using Wordnet from NLTK
		
		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			lemmatized tokens representing a sentence
		"""
		
		reducedText = [[self.lemmatizer.lemmatize(token) for token in sent] for sent in text]
		
		return reducedText

if __name__=='__main__':
	ir = InflectionReduction()
	print(ir.lemmatize([['cars', 'suitcases']]))
