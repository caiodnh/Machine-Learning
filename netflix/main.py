import numpy as np
import kmeans
import common
import naive_em
import em

# X = np.loadtxt("toy_data.txt")
X = np.loadtxt("netflix_incomplete.txt")

# seeds = range(5)
# Ks = [1, 12]
# for K in Ks:
#   LLs = []
#   for seed in seeds:
#     mixture, post = common.init(X, K, seed = seed)
#     mix, pos, LL = em.run(X, mixture, post)
#     LLs.append((seed,LL))
#   print(K)
#   print(max(LLs, key = lambda x: x[1]))

K = 12
seed = 1
mixture0, post0 = common.init(X, K, seed = seed)
mixture, post, LL = em.run(X, mixture0, post0)

X_pred = em.fill_matrix(X, mixture)

X_gold = np.loadtxt('netflix_complete.txt')
print(common.rmse(X_gold, X_pred))
breakpoint()
