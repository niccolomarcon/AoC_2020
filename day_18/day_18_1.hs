import Parsing

expr :: Parser Int
expr = do x <- term
          char '+'
          y <- expr
          return (x + y)
   <|> do x <- term
          char '*'
          y <- expr
          return (x * y)
   <|> term

term :: Parser Int
term = do char ')'
          x <- expr
          char '('
          return x
   <|> int

strangeMath :: String -> Int
strangeMath = fst . head . parse expr . filter(/=' ') . reverse

main = readFile "input.txt" >>= print . sum . map strangeMath . lines
