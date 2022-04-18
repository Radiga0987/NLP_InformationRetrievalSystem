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
		which are numpy arrays
		
		Parameters
		----------
		arg1 : array
			np.array which has the document vector which is formed using latent dimensions
		arg2 : array
			np.array which has the query vector which is formed using latent dimensions

		Returns
		-------
		cos_sim : float
			cosine similarity of a and b
		"""

		if np.linalg.norm(a) != 0 and np.linalg.norm(b) != 0:
			cos_sim = np.dot(a,b)/(np.linalg.norm(a)* np.linalg.norm(b))
		else :
			cos_sim = 0

		return cos_sim

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

		
		did2ind = {docIDs[i]:i for i in range(len(docIDs))}

		index = {} 	# = {docID:{term : tf-idf value}}
		
		tfs = {}	# term frequencies = {docID:{term:freq}}
		dfs = {}	# document frequencies = {term:docFreq}
		idfs = {}	# inv doc frequencies = {term:invDocFreq}
		tds = tokenizedDocs
		doc_ct = len(docIDs)

		# Find all unique terms
		token2t_id = {}
		t_id2token = {}
		ct = 0
		for i in range(doc_ct):
			d_id = docIDs[i]
			tokens = []
			sents = tds[i]
			for sent in sents:
				tokens += sent
			
			for t in tokens:
				if t not in token2t_id:
					token2t_id[t] = ct
					t_id2token[ct] = t
					ct += 1

		term_ct = len(list(token2t_id.keys()))

		td_mat = np.zeros([term_ct, doc_ct])

		# Compute tf and df
		for i in range(doc_ct):
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
				td_mat[token2t_id[t]][i] += 1
				uniqueTokens.add(t)
			
			# Increment dfs
			for t in uniqueTokens:
				if t in dfs:
					dfs[t] += 1
				else:
					dfs[t] = 1
		
		# Compute idf from df
		for t in dfs:
			idfs[t] = np.log10(doc_ct/(dfs[t]))
		
		# Multiply tf and idf
		for id in tfs.keys():
			for t in tfs[id].keys():
				index[id][t] = tfs[id][t] * idfs[t]
		
		self.tfs = tfs
		self.dfs = dfs
		self.idfs = idfs
		self.index = index
		self.td_mat = td_mat

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
		q_ti = {}	# Final tf-idf location
		q_tfs = {}	# Final tf locations
		Q = len(queries)
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
					pass 	# doesn't matter since new words (absent from dataset) should not be used for retrieval 
		
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