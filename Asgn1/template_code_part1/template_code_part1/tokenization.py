from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer



class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		
		tokenizedText = []
		if isinstance(text, list):
			for s in text:
				if isinstance(s, str):
					tokens = re.split( "[' ,-/]", s) # spliting the sentences into words and symbols
					for i in range(len(tokens)):
						# removing punctuation symbols
						if tokens[i]==['\'','\"','?', ':', '!', '.', ',', ';','&','#','(',')','[',']','{','}','_','|']:
							del tokens[i]
						# removing unwanted spaces and empty characters
						elif (tokens[i] ==' ') or (tokens[i] ==''):
							del tokens[i]
					tokenizedText.append(tokens) 
				else:
					print("Error:text input list does not contain strings")
					return []
		else:
			print("Error:text input is not a list")
			return []
			
		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""
		tokenizedText = []
		if isinstance(text, list):
			for s in text:
				if isinstance(s, str):
					tokens = TreebankWordTokenizer().tokenize(s)
					tokenizedText.append(tokens)
				else:
					print("Error:text input list does not contain strings")
					return []
		else:
			print("Error:text input is not a list")
			return []
		return tokenizedText