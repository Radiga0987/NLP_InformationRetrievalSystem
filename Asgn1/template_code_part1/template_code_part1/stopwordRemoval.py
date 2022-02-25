from util import *

# Add your import statements here
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

class StopwordRemoval():

	def __init__(self):
		self.sw_set = set(stopwords.words('english'))	# Use set for fast membership check
	
	def fromList(self, text):
		"""
		Stopword removal using NLTK Stopwords collection

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = []

		if isinstance(text, list):
			new_text = []

			for sent in text:
				if isinstance(sent, list):
					new_sent = []

					for token in sent:
						if isinstance(token, str):
							if token not in self.sw_set:
								new_sent.append(token)
						else:
							print("Error: Expected string token, received a " + str(type(token)))
							return []
				
					new_text.append(new_sent)

				else:
					print("Error: Expected sentence as a list, received a " + str(type(sent)))
					return []
			
			stopwordRemovedText = new_text

		else:
			print("Error: Expected document as list, received a " + str(type(text)))
			return []
			
		return stopwordRemovedText

if __name__ == '__main__':
	# Testing
	swr = StopwordRemoval()
	print(swr.fromList([['i', 'like', 'myself']]))
	# Should return  [['like']]
