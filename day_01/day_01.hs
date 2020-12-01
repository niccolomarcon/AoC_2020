import Control.Monad (replicateM)

solve :: [Int] -> Int
solve = product . head . filter ((==2020) . sum) . replicateM 3

main :: IO ()
main = readFile "input.txt" >>= print . solve . map read . lines
