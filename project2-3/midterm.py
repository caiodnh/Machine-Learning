import numpy as np

X = [[0,0], [2,0], [1,1], [0,2], [3,3], [4,1], [5,2], [1,4], [4,4], [5,5]]
Y = [-1,-1,-1,-1,-1, 1, 1, 1, 1, 1]

def phi(point):
  ans = np.array([point[0]**2, np.sqrt(2) * point[0] * point[1], point[1]**2, 1])
  return ans

feature_X = []
for x in X:
  feature_X.append(phi(x))
feature_X = np.array(feature_X)

# M = [[0,0,0,1], [4,0,0,1], [1, 1, 1, 1], [0,0,4,1], [9,9,9,1],
#      [16,4,1,1], [0,0,0,0], [1,4,16,1], [16,16,16,1], [25,25,25,1]]

# print (feature_X)
count = [1, 65, 11, 31, 72, 30, 0, 21, 4, 15]

theta = np.array([0,0,0,0])
for (i, x) in enumerate(feature_X):
  theta += count[i] * Y[i] * X[i]

print(theta)

# M = np.array(M)
# coef = np.array(coef)

# ans = np.array([0,0,0,0])
# for (i,c) in enumerate(coef):
#   ans += c*M[i]
# ans = ans * [1, np.sqrt(2), 1, 1]
# print(ans)

# ans2 = []
# for row in M:
#   temp = np.dot(ans, row).item()
#   if temp <0:
#     temp = -1
#   if temp> 0:
#     temp = +1
#   ans2.append(temp)

# print (ans2)

# print(np.sqrt(2)/2)