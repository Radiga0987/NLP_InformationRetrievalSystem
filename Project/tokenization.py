from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer



class Tokenization():

	def __init__(self):
		self.punct_symbols = ['\"','?', ':', '!', '.', ',', ';','&','#','(',')','[',']','{','}','_','|','-',' ','']

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
			new_text = []
			for s in text:
				if isinstance(s, str):
					new_s = []
					tokens = re.split("\W+", s) # splitting at non-alphanumeric characters
					for i in range(len(tokens)):
						# removing empty characters
						if tokens[i] == '':
							continue
						else:
							new_s.append(tokens[i])
					new_text.append(new_s) 
				else:
					print("Error: Text input list does not contain strings")
					return []
			
			tokenizedText = new_text
		else:
			print("Error: Text input is not a list")
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
					Tokens = TreebankWordTokenizer().tokenize(s)
					tokens = []
					for t in Tokens: 
						tokens.extend(re.split('[^a-zA-Z\d\']', t))
					tokenizedText.append(tokens)

				else:
					print("Error: Text input list does not contain strings")
					return []
			
			for s_i in range(len(tokenizedText)): # Remove tokens that are lone punctuation symbols
				new_s = []
				for t_i in range(len(tokenizedText[s_i])):
					if tokenizedText[s_i][t_i] not in self.punct_symbols:
						new_s.append(tokenizedText[s_i][t_i])
				tokenizedText[s_i] = new_s.copy()
		else:
			print("Error: Text input is not a list")
			return []
		return tokenizedText

if __name__ == '__main__':
	# Testing
	
	tk = Tokenization()
	print(tk.naive(['I like trains, but cars are better.', 'Give me some sunshine!', 'Don\'t take that']))
	print(tk.pennTreeBank(['I like trains, \'but cars are-better.', 'Give me some sunshine!', 'Don\'t take that']))
