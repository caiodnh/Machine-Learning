pdf :: Floating a => a -> a -> a -> a
pdf mu sigmaSq x = exp (-(x - mu)^2 / (2 * sigmaSq)) / sqrt (2 * pi * sigmaSq)

xs :: Floating a => [a]
xs = [-1, 0, 4, 5, 6]

step :: Floating a => (a, a, a, a, a, a) -> (a, a, a, a, a, a)
step (pi1, pi2, mu1, mu2, sigmaSq1, sigmaSq2) = (pi1', pi2', mu1', mu2', sigmaSq1', sigmaSq2')
  where
    n1 x = pdf mu1 sigmaSq1 x
    n2 x = pdf mu2 sigmaSq2 x
    gamma1 x = pi1 * n1 x / (pi1 * n1 x + pi2 * n2 x)
    gamma2 x = 1 - gamma1 x
    gamma1s = gamma1 <$> xs
    gamma2s = gamma2 <$> xs
    n = fromIntegral $ length xs
    pi1' = sum gamma1s / n
    pi2' = sum gamma2s / n
    mu1' = sum (zipWith (*) xs gamma1s) / sum gamma1s
    mu2' = sum (zipWith (*) xs gamma2s) / sum gamma2s
    squares1 = map ((^2) . subtract mu1) xs
    squares2 = map ((^2) . subtract mu2) xs
    sigmaSq1' = sum (zipWith (*) squares1 gamma1s) / sum gamma1s
    sigmaSq2' = sum (zipWith (*) squares2 gamma1s) / sum gamma2s

theta :: Floating a => (a, a, a, a, a, a)
theta = (0.5, 0.5, 5, 6, 1, 4)

iter :: Floating a => Int -> (a, a, a, a, a, a)
iter n = last $ take (n+1) $ iterate step theta