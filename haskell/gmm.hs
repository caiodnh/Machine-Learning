n :: Double -> Double -> Double -> Double
n mu sigmaSq x = exp(-1 * (x - mu)^2 / (2 * sigmaSq)) / sqrt (2 * pi * sigmaSq)

p1 = 0.5
p2 = 0.5
mu1 = -3
mu2 = 2
sigmaSq1 = 4
sigmaSq2 = 4

x1 = 0.2
x2 = -0.9
x3 = -1
x4 = 1.2
x5 = 1.8

xs = [x1, x2, x3, x4, x5]

ps1 = map ((p1 *) . n mu1 sigmaSq1) xs
ps2 = map ((p2 *) . n mu2 sigmaSq2) xs

ps1' = zipWith (/) ps1 $ zipWith (+) ps1 ps2
