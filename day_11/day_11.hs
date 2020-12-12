import Data.List
import qualified Data.Map as M

data Position = Floor | Empty | Occupied deriving Eq
type Coord = (Int, Int)
type Neighbours = M.Map Coord [Coord]
type Ferry = [[Position]]

read' :: Char -> Position
read' '.' = Floor
read' 'L' = Empty
read' '#' = Occupied
read' _ = error "Invalid character"

count :: Eq a => a -> [a] -> Int
count a = length . filter (==a)

head' :: [a] -> [a]
head' a = if null a then a else [head a]

countOccupied :: Ferry -> Int
countOccupied = sum . map (count Occupied)

get :: Ferry -> Coord -> Position
get f (r, c) = (!!c) . (!!r) $ f

maxIndexes :: [[a]] -> (Int, Int)
maxIndexes a = (length a - 1, (length . head) a - 1)

neighs :: Ferry -> Neighbours
neighs f = let (max_r, max_c) = maxIndexes f
               coords = [(r,c) | r <- [0..max_r], c <- [0..max_c]]
           in foldl (visibleNeighs f) M.empty coords

visibleNeighs :: Ferry -> Neighbours -> Coord -> Neighbours
visibleNeighs f n p@(r,c) = M.insert p visible n where
    (max_r, max_c) = maxIndexes f
    dirs = [zip (repeat r) [c+1..max_c] -- right
           ,zip (repeat r) [c-1,c-2..0] -- left
           ,zip [r+1..max_r] (repeat c) -- down
           ,zip [r-1,r-2..0] (repeat c) -- up
           ,zip [r-1,r-2..0] [c-1,c-2..0] -- top left
           ,zip [r-1,r-2..0] [c+1..max_c] -- top right
           ,zip [r+1..max_r] [c-1,c-2..0] -- bottom left
           ,zip [r+1..max_r] [c+1..max_c] -- bottom right
           ]
    visible = foldl1 (++) . map (head' . filter ((/=Floor) . get f)) $ dirs

next :: Neighbours -> Ferry -> Coord -> Position
next n f c = case get f c of
    Floor    -> Floor
    Empty    -> if occupied == 0 then Occupied else Empty
    Occupied -> if occupied >= 5 then Empty else Occupied
    where occupied = count Occupied . map (get f) . (M.!c) $ n

gol :: Neighbours -> Ferry -> Ferry
gol n f = let (max_r, max_c) = maxIndexes f
              next_f = [[next n f (r,c) | c <- [0..max_c]] | r <- [0..max_r]]
          in if f == next_f then f else gol n next_f

part2 :: Ferry -> Int
part2 = countOccupied . (gol <$> neighs <*> id)

main :: IO ()
main = interact $ show . part2 . map (map read') . lines
