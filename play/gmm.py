import numpy as np
from scipy.stats import norm

def pdf (mu, sigmaSq):
  return lambda x: norm(mu, np.sqrt(sigmaSq)).pdf(x)

xs = np.array([-1, 0, 4, 5, 6])

def step(pi1, pi2, mu1, mu2, sigmaSq1, sigmaSq2):

  def gamma1 (x):
    return pi1 * pdf(mu1, sigmaSq1)(x) / (pi1 * pdf(mu1, sigmaSq1)(x) + pi2 * pdf(mu2, sigmaSq2)(x))

  def gamma2 (x):
    return 1 - gamma1(x)

  pi1 = np.sum(gamma1(xs)) / len(xs)
  pi2 = np.sum(gamma2(xs)) / len(xs)

  mu1 = np.sum(xs * gamma1(xs)) / np.sum(gamma1(xs))
  mu2 = np.sum(xs * gamma2(xs)) / np.sum(gamma2(xs))

  sigmaSq1 = np.sum((xs - mu1)**2 * gamma1(xs)) / np.sum(gamma1(xs))
  sigmaSq2 = np.sum((xs - mu2)**2 * gamma2(xs)) / np.sum(gamma2(xs))

  return pi1, pi2, mu1, mu2, sigmaSq1, sigmaSq2

theta = 0.5, 0.5, 5, 6, 1, 4
for i in range(5):
  theta = step(*theta)

print(theta)