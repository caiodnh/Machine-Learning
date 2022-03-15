module Perceptron where

import           Data.Monoid

type Vector = (Int, Int)
type Sign = Int
type TrainingPoint = (Vector, Sign)
type TrainingSet = [TrainingPoint]
type Hyperplane = (Vector, Int)

plus :: Vector -> Vector -> Vector
plus (x, y) (x', y') = (x + x', y + y')

times :: Int -> Vector -> Vector
times n (x, y) = (n*x, n*y)

dot :: Vector -> Vector -> Int
dot (x, y) (x', y') = x*x' + y*y'

update :: Hyperplane -> TrainingPoint -> ([Vector], Hyperplane)
update hp@(omega, omega_0) tp@(v, sign) = if pointOk
               then
                 return hp
               else
                 ([v], newHP)
                where
                  pointOk = sign * ((omega `dot` v) + omega_0) > 0
                  newHP = (omega `plus` (sign `times` v), omega_0 + sign)

train :: (Hyperplane, TrainingSet) -> ([Vector], (Hyperplane, TrainingSet))
train (hp, ts) = do
  hp' <- update hp (head ts)
  return (hp', tail ts)

ts :: TrainingSet
ts = cycle [((-4, 2), 1), ((-2, 1), 1), ((-1, -1), -1), ((2,2), -1), ((1, -2), -1)]

initial :: (Hyperplane, TrainingSet)
initial = (((0, 0), 0), ts)

trainN :: Int -> (Hyperplane, TrainingSet) -> ([Vector], (Hyperplane, TrainingSet))
trainN n (hp, ts) = do
  if n == 0
    then return (hp, ts)
  else do
    (hp', ts') <- train (hp, ts)
    trainN (n-1) (hp', ts')
