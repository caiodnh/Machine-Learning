data Action = Stay | GoLeft | GoRight deriving (Eq, Ord, Enum, Bounded, Show)
data State = One | Two | Three | Four | Five deriving (Eq, Ord, Enum, Bounded, Show)
-- type Prob = Double

-- instance Bounded State where
--   minBound = State 1
--   maxBound = State 5

-- instance Enum State where
--   toEnum n
--     | State n <= minBound = minBound 
--     | State n >= maxBound = maxBound
--   fromEnum (State n) = n

inner :: State -> Bool 
inner s = s /= minBound && s /= maxBound

t :: State -> Action -> State -> Double 
t s Stay s'
  | s == s'                                   = 0.5
  | inner s && (s' == pred s || s' == succ s) = 0.25
  | s == minBound && s' == succ s             = 0.5
  | s == maxBound && s' == pred s             = 0.5
  | otherwise                                 = 0

t s GoLeft s'
  | s == minBound = t s Stay s'
  | s' == pred s  = 1/3
  | s == s'       = 2/3
  | otherwise     = 0

t s GoRight s'
  |s == maxBound  = t s Stay s'
  | s' == succ s  = 1/3
  | s == s'       = 2/3
  | otherwise     = 0

r :: State -> Action -> State -> Double
r s a s'
  | s == maxBound = 1
  | otherwise     = 0

gamma :: Double
gamma = 0.5

type ValueMap = [Double]

q :: ValueMap -> State -> Action -> Double 
q v s a =  sum $ zipWith f (enumFrom minBound) v
  where
    f s' vs' = t s a s' * (r s a s' + gamma * vs')

updateV :: ValueMap -> ValueMap
updateV v = f <$> enumFrom (minBound :: State)
  where
    f s = maximum $ q v s <$> enumFrom (minBound :: Action)

vzinho n = last $ take (n + 1) $ iterate updateV (0 <$ enumFrom (minBound :: State))
