from util import *

# Add your import statements here
import math



class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1
		num_relevant = 0

		if k > len(query_doc_IDs_ordered):
			print("Error! k is larger than number of documents retrieved")
			return precision

		for id in query_doc_IDs_ordered[:k]:
			if int(id) in true_doc_IDs:
				num_relevant += 1

		precision = num_relevant/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		if len(doc_IDs_ordered) != len(query_ids):
			print("Error! Number of queries is not equal to number of lists of document orders")
			return -1

		meanPrecision = 0
		for i in range(len(query_ids)):
			query_id = int(query_ids[i])
			document_order = doc_IDs_ordered[i]
			
			true_doc_IDs = []
			for d in qrels:
				if int(d["query_num"]) ==  query_id:
					true_doc_IDs.append(int(d["id"]))
			meanPrecision += self.queryPrecision(document_order, query_id, true_doc_IDs, k)

		meanPrecision /=  len(query_ids)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1
		num_relevant = 0

		if k > len(query_doc_IDs_ordered):
			print("Error! k is larger than number of documents retrieved")
			return recall

		for id in query_doc_IDs_ordered[:k]:
			if int(id) in true_doc_IDs:
				num_relevant += 1

		recall = num_relevant/len(true_doc_IDs)

		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		if len(doc_IDs_ordered) != len(query_ids):
			print("Error! Number of queries is not equal to number of lists of document orders")
			return -1

		meanRecall = 0
		for i in range(len(query_ids)):
			query_id = int(query_ids[i])
			document_order = doc_IDs_ordered[i]
			
			true_doc_IDs = []
			for d in qrels:
				if int(d["query_num"]) ==  query_id:
					true_doc_IDs.append(int(d["id"]))
			meanRecall += self.queryRecall(document_order, query_id, true_doc_IDs, k)

		meanRecall /=  len(query_ids)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		if k > len(query_doc_IDs_ordered):
			print("Error! k is larger than number of documents retrieved")
			return recall

		# fscore = -1
		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

		if precision == 0.0 or recall == 0.0:	# when any zero, set fscore 0. Derived from limit of fscore as p,r -> 0
			fscore = 0
		else:
			fscore = (2*precision*recall)/(precision+recall)

		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		if len(doc_IDs_ordered) != len(query_ids):
			print("Error! Number of queries is not equal to number of lists of document orders")
			return -1

		meanFscore = 0
		for i in range(len(query_ids)):
			query_id = int(query_ids[i])
			document_order = doc_IDs_ordered[i]
			
			true_doc_IDs = []
			for d in qrels:
				if int(d["query_num"]) ==  query_id:
					true_doc_IDs.append(int(d["id"]))
			meanFscore += self.queryFscore(document_order, query_id, true_doc_IDs, k)

		meanFscore /=  len(query_ids)

		return meanFscore

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list of dicts
			qrels passed here since we need the relevance scores too.
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		if k > len(query_doc_IDs_ordered):
			print("Error! k is larger than number of documents retrieved")
			return -1

		DCGk,IDCGk=0,0
		doc_rel_scores={}


		for d in true_doc_IDs:
			if int(d["query_num"]) == int(query_id):
				doc_rel_scores[int(d["id"])] = 5 - int(d["position"])

		doc_list=doc_rel_scores.keys()
		rel_values_descending=sorted(doc_rel_scores.values(),reverse=True)
		len_rvd = len(rel_values_descending)
		for i in range(1,k+1):
			if int(query_doc_IDs_ordered[i-1]) in doc_list:
				DCGk += (2 ** doc_rel_scores[query_doc_IDs_ordered[i-1]] - 1) / math.log(i+1,2)
			if i<len_rvd:
				IDCGk += (2**rel_values_descending[i-1]-1) / math.log(i+1,2)

		if IDCGk == 0:
			print("IDCG@k = 0 and hence no relevant documents for given query")
			return -1

		nDCG = DCGk / IDCGk

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		if len(doc_IDs_ordered) != len(query_ids):
			print("Error! Number of queries is not equal to number of lists of document orders")
			return -1

		meanNDCG = 0
		for i in range(len(query_ids)):
			query_id = int(query_ids[i])
			document_order = doc_IDs_ordered[i]

			meanNDCG += self.queryNDCG(document_order, query_id, qrels, k)

		meanNDCG /=  len(query_ids)

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		if k > len(query_doc_IDs_ordered):
			print("Error! k is larger than number of documents retrieved")
			return -1

		avgPrecision = 0
		for i in range(1,k+1):
			avgPrecision += self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, i)

		avgPrecision /= k

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		if len(doc_IDs_ordered) != len(query_ids):
			print("Error! Number of queries is not equal to number of lists of document orders")
			return -1

		meanAveragePrecision = 0
		for i in range(len(query_ids)):
			query_id = int(query_ids[i])
			document_order = doc_IDs_ordered[i]
			
			true_doc_IDs = []
			for d in q_rels:
				if int(d["query_num"]) ==  query_id:
					true_doc_IDs.append(int(d["id"]))
			meanAveragePrecision += self.queryAveragePrecision(document_order, query_id, true_doc_IDs, k)

		meanAveragePrecision /=  len(query_ids)

		return meanAveragePrecision

