import pandas as pd
from utils import hypergeo, hypergeoNevents, compute_possible_draws

class RampantGrowthManabase():

	def __init__(self, **kwargs):
		self.N = kwargs.get('size_of_deck', 99)
		self.n1 = kwargs.get('number_of_given_card', 1)
		self.n2 = kwargs.get('number_of_lands', 40)
		self.n3 = kwargs.get('number_of_rampant_growths', 1)
		self.bl = kwargs.get('number_of_basic_lands', 12)
		self.K = kwargs.get('initial_hand_size', 7)
		self.k = kwargs.get('cmc_of_given_card', 2)
		self.pa_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_A(self.K+i,self.n1,self.N)] for i in range(0,7)})
		self.pb_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_B(self.k,self.K+i,self.n2,self.n3,self.N)] for i in range(0,7)})
		self.pab_df = pd.DataFrame(data = {f'Draw {i}' : [self.prob_A_and_B(self.k,self.K+i,self.n1,self.n2,self.n3,self.bl,self.N)] for i in range(0,7)})
		self.palb_df = self.pab_df/self.pb_df
		self.pbla_df = self.pab_df/self.pa_df

	def prob_A(self, K, n, N):
		total = 0
		for k in range(1, K + 1):
			p = hypergeo(k, n, K, N)
			total += p
		return total

	def prob_B(self, k, K, n2, n3, N):
		possible_draws = compute_possible_draws(k,[n2,n3],K,N)
		total = 0
		for draw in possible_draws:
			k2 = draw[0][1]
			k3 = draw[1][1]
			p = hypergeoNevents([k2,k3],[n2,n3],K,N)
			m = 1 if k2 >= 2 else 0
			total += m * p
		return total

	def prob_A_and_B(self, k, K, n1, n2, n3, bl, N):
		possible_draws = compute_possible_draws(k,[n2-bl,n3,bl],K,N)
		total = 0
		for draw in possible_draws:
			for k1 in range(1, n1 + 1):
				k2 = draw[0][1]
				k3 = draw[1][1]
				kl = draw[2][1]
				ks = [k1, k2, k3, kl]
				ns = [n1, n2-bl, n3, bl]
				p = hypergeoNevents(ks,ns,K,N)
				m = 1 if k2 + kl >= 2 and k - k2 <= bl else 0
				total += m * p
		return total