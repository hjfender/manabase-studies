import pandas as pd
from utils import hypergeo, hypergeoNevents

class BasicManabase():

	def __init__(self, **kwargs):
		self.N = kwargs.get('size_of_deck', 99)
		self.n1 = kwargs.get('number_of_given_card', 1)
		self.n2 = kwargs.get('number_of_lands', 40)
		self.K = kwargs.get('initial_hand_size', 7)
		self.k = kwargs.get('cmc_of_given_card', 2)
		self.pa_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_A(self.K+i,self.n1,self.N)] for i in range(0,7)})
		self.pb_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_B(self.k,self.K+i,self.n2,self.N)] for i in range(0,7)})
		self.pab_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_A_and_B(self.k,self.K+i,self.n1,self.n2,self.N)] for i in range(0,7)})
		self.palb_df = self.pab_df/self.pb_df
		self.pbla_df = self.pab_df/self.pa_df

	def prob_A(self, K, n, N):
		total = 0
		for k in range(1, K + 1):
			p = hypergeo(k, n, K, N)
			total += p
		return total

	def prob_B(self, k, K, n, N):
		total = 0
		for j in range(k, K + 1):
			p = hypergeo(j, n, K, N)
			total += p
		return total

	def prob_A_and_B(self, k, K, n1, n2, N):
		total = 0
		for k2 in range(k, K + 1):
			for k1 in range(1, n1 + 1):
				ks = [k1, k2]
				ns = [n1, n2]
				p = hypergeoNevents(ks,ns,K,N)
				total += p
		return total