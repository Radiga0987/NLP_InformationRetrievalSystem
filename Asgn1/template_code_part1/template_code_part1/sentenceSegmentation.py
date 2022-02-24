from util import *

# Add your import statements here
import re
from nltk.tokenize import PunktSentenceTokenizer




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		if isinstance(text, str):
			s = re.split('[.?!]', text)
			segmentedText = [sentence.strip() for sentence in s]
		else:
			print("Error:Input text is not a string")
			return []

		return segmentedText



	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""
		if (isinstance(text, str)):
			tokenizer_object = PunktSentenceTokenizer(text)  #This creates a  PunktSentenceTokenizer object
			segmentedText = tokenizer_object.tokenize(text)
		else:
			print("Error:Input text is not a string")
			return []
		return segmentedText