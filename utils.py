from scipy.special import comb
from collections import defaultdict

def hypergeo(k,n,K,N):
    return comb(n,k)*comb(N-n,K-k)/comb(N,K)

def hypergeoNevents(ks,ns,K,N):
    if len(ks) != len(ns):
        raise Exception("Input list sizes do not agree")
    result = comb(N-sum(ns),K-sum(ks))
    for i in range(0,len(ns)):
        k = ks[i]
        n = ns[i]
        result = result*comb(n,k)
    return result/comb(N,K)

def distribute_k_over_n(k, l):
    result = []
    if k == 0:
        result.append(l)
    else:
        for i in range(0,len(l)):
            new_l = l.copy()
            new_l[i] += 1
            result.extend(distribute_k_over_n(k-1,new_l))
    return result

def compute_possible_draws(k,ns,K,N):
    possible_draws = {}
    for j in range(k,K+1):
        draws = [0 for _ in ns]
        draws = distribute_k_over_n(j, draws)
        for draw in draws:
            possible_draws[str(draw)] = draw
    return [list(zip(ns,list(l))) for _, l in possible_draws.items()]

def analyze_manabase(manabase):
    counts = defaultdict(int)
    for card in manabase:
        counts[card.name] += 1
        for supertype in card.supertypes:
            counts[supertype.name] += 1
        for cardtype in card.types:
            counts[cardtype.name] += 1
        for subtype in card.subtypes:
            counts[subtype.name] += 1
    return counts

def compute_prob(N, K, cmc, manabase):
    counts = analyze_manabase(manabase)
