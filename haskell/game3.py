import numpy as np

# states from 0 to 5
# actions 0 (C) and 1 (M)

# transition matrix
transition = np.zeros((6,2,6))

transition[0,0,0] = 1
transition[0,1,0] = 1
for i in [1,2,3]:
  transition[i,1,i-1] = 1
  transition[i,0,i+2] = 0.7
  transition[i,0,i] = 0.3
for i in [4,5]:
  transition[i,1,i-1] = 1
  transition[i,0,i] = 1

#reward matrix
def r(s0: float, a: float, s1:float) -> float:
  if (s0 - s1) != 0:
    return np.abs(s0 - s1)**(1/3)
  else:
    if s0 != 0:
      return 1/np.sqrt(s0 + 4)
    else:
      return 0

reward = np.empty((6,2,6))
# fromfunction(lambda x, y, z: r(x,y,z), (6,2,6))

iter = np.ndindex(6,2,6)
for idx in iter:
  reward[idx] = r(*idx)


# gamma
gamma = 0.6

# Q and V
def newQ(V):
  def f(s0, a):
    # temp = reward[s0, a] + gamma * V
    # return transition[s0, a] @ temp.T
    ans = 0
    s0 = s0
    a = a
    for s1 in range(6):
      ans += transition[s0, a, s1] * (reward[s0, a, s1] + gamma * V[s1])
    return ans
  return f

def update(Q):
  V = np.amax(Q, axis=1)
  Q = np.empty((6,2))
  iter = np.ndindex(6,2)
  for idx in iter:
    Q[idx] = newQ(V)(*idx)
  return Q


Q = np.zeros((6,2))
for i in range(1000):
  Q = update(Q)

print(Q)