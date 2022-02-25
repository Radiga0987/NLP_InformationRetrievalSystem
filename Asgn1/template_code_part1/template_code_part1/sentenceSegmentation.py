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
			new_s = [sentence.strip() for sentence in s]
			segmentedText = [sent for sent in new_s if sent != '']
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
			print("Error: Input text is not a string")
			return []
		return segmentedText

if __name__ == '__main__':
	# Testing
	ss = SentenceSegmentation()
	print(ss.naive("I like trains, but cars are better. Give me some sunshine!"))
	print(ss.punkt("I like trains, but cars are better. Give me some sunshine!"))