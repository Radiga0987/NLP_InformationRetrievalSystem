from numpy import isin
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
		https://stackoverflow.com/questions/10554052/what-are-the-major-differences-and-benefits-of-porter-and-lancaster-stemming-alg
		
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
		
		reducedText = []

		if isinstance(text, list):
			new_text = []
			for sent in text:
				if isinstance(sent, list):
					new_sent = []
					for token in sent:
						if isinstance(token, str):
							new_sent.append(self.stemmer.stem(token))
						else:
							print("Error: Expected string token, received a " + str(type(token)))
							return []

					new_text.append(new_sent)
				
				else:
					print("Error: Expected sentence as a list, received a " + str(type(sent)))
					return []
			
			reducedText = new_text
		
		else:
			print("Error: Expected document as list, received a " + str(type(text)))
			return []
		
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
		
		reducedText = []

		if isinstance(text, list):
			new_text = []
			for sent in text:
				if isinstance(sent, list):
					new_sent = []
					for token in sent:
						if isinstance(token, str):
							new_sent.append(self.lemmatizer.lemmatize(token))
						else:
							print("Error: Expected string token, received a " + str(type(token)))
							return []

					new_text.append(new_sent)
				
				else:
					print("Error: Expected sentence as a list, received a " + str(type(sent)))
					return []
			
			reducedText = new_text
		
		else:
			print("Error: Expected document as list, received a " + str(type(text)))
			return []
		
		return reducedText

if __name__=='__main__':
	# Testing
	ir = InflectionReduction()
	print(ir.stem([['cars', 'suitcases', 'radii']]))  # car, suitcas, radii
	print(ir.lemmatize([['cars', 'suitcases', 'radii']]))  # car, suitcase, radius
