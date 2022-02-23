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

		stopwordRemovedText = None

		#Fill in code here

		stopwordRemovedText = []
		for sent in text:
			new_sent = []
			for token in sent:
				if token not in self.sw_set:
					new_sent.append(token)
			stopwordRemovedText.append(new_sent)

		return stopwordRemovedText

if __name__ == '__main__':
	# Testing
	swr = StopwordRemoval()
	print(swr.fromList([['i', 'like', 'myself']]))


	