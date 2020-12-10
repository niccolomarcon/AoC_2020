import Data.List
import qualified Data.Map as M

prepare :: [Integer] -> [Integer]
prepare ns = sort $ 0 : maximum ns + 3 : ns

count :: [Integer] -> M.Map Integer Integer
count = M.fromListWith (+) . flip zip (repeat 1)

diffs :: [Integer] -> [Integer]
diffs ns = zipWith (-) (tail ns) ns

part1 :: [Integer] -> Integer
part1 = ((*) <$> (M.!1) <*> (M.!3)) . count . diffs

valid :: Integer -> (Integer, Integer) -> Bool
valid n = (<= n + 3) . fst

magik :: [(Integer, Integer)] -> Integer -> [(Integer, Integer)]
magik [] n = [(n, 1)]
magik stack n = (n, sum . map snd . filter (valid n) . take 3 $ stack) : stack

part2 :: [Integer] -> Integer
part2 = snd . head . foldl magik [] . reverse

main :: IO ()
main = interact $ show . part2 . prepare . map read . lines
