from util import *

# Add your import statements here
import numpy as np

class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.idfs = None

	def cosSim(self,a,b):
		"""
		Finds cosine similarity between two vectors a and b
		represented as dictionaries
		
		Parameters
		----------
		arg1 : dict
			Dict whose key:value = term:tf-idf
		arg2 : dict
			Dict whose key:value = term:tf-idf

		Returns
		-------
		cosSim : float
			Sum of products of tf-idfs of a and b 
		"""

		tot = 0

		moda = 0
		for t in a.keys():
			moda += a[t]**2
		moda = moda ** 0.5

		modb = 0
		for t in b.keys():
			modb += b[t]**2
		modb = modb ** 0.5
		
		for t in a.keys():
			if t in b:
				tot += a[t]*b[t]
		if moda != 0 and modb != 0:
			return tot/(moda*modb)
		else:
			return 0

	def buildIndex(self, tokenizedDocs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = {} 	# = {docID:{term : tf-idf value}}
		
		tfs = {}	# term frequencies = {docID:{term:freq}}
		dfs = {}	# document frequencies = {term:docFreq}
		idfs = {}	# inv doc frequencies = {term:invDocFreq}
		tds = tokenizedDocs
		N = len(docIDs)

		# Compute tf and df
		for i in range(N):
			id = docIDs[i]
			tfs[id] = {}
			index[id] = {}
			sents = tds[i]
			tokens = [] # [doc1, doc2] = [[sent1, sent2], [sent1, sent2]] = [[[token1, token2], [token1,token2]], [[token1, token2], [token1,token2]]]
			for sent in sents:
				tokens += sent
			
			uniqueTokens = set()
			
			# Compute tf
			for t in tokens:
				if t in tfs[id]:
					tfs[id][t] += 1
				else:
					tfs[id][t] = 1
				
				uniqueTokens.add(t)
			
			# Increment dfs
			for t in uniqueTokens:
				if t in dfs:
					dfs[t] += 1
				else:
					dfs[t] = 1
		
		# Compute idf from df
		for t in dfs:
			idfs[t] = np.log10(N/(dfs[t]))	# add 1 in denom to prevent div by 0 (smoothing) #TODO check
		
		# Multiply tf and idf
		for id in tfs.keys():
			for t in tfs[id].keys():
				index[id][t] = tfs[id][t] * idfs[t]
		
		self.tfs = tfs
		self.dfs = dfs
		self.idfs = idfs
		self.index = index

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		# Compute tf-idf representation of queries
		q_ti = {}
		q_tfs = {}
		Q = len(queries)
		print("Query count:", Q)
		ranks = [None for _ in range(Q)]

		for id in range(Q):
			q = queries[id]
			q_ti[id] = {}
			q_tfs[id] = {}
			tokens = []
			for sent in q:
				tokens += sent
			
			# Compute tf
			for t in tokens:
				if t in q_tfs[id]:
					q_tfs[id][t] += 1
				else:
					q_tfs[id][t] = 1
			
			for t in self.idfs:
				if t in q_tfs[id]:
					q_ti[id][t] = q_tfs[id][t] * self.idfs[t]
				else:
					pass
			# Compute tf-idf of queries
			# for t in q_tfs[id].keys():
			# 	if t in self.idfs:	
			# 		q_ti[id][t] = q_tfs[id][t] * self.idfs[t]
			# 	else:
			# 		pass
			# 		# q_ti[id][t] = 0		# if term is absent from documents, give it 0 weight in retrieval
		
		# Find docID ranking for each query
			vq = q_ti[id]
			scores = []
			for d_id in self.index.keys():
				vd = self.index[d_id]
				scores.append([self.cosSim(vq, vd), d_id])
			
			scores.sort(reverse=True)
			ranks[id] = [scores[d_ind][1] for d_ind in range(len(scores))]
		
		docIDsOrdered = ranks
		return docIDsOrdered