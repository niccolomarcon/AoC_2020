import Parsing

expr :: Parser Int
expr = do x <- factor
          char '*'
          y <- expr
          return (x * y)
   <|> factor

factor :: Parser Int
factor = do x <- term
            char '+'
            y <- factor
            return (x + y)
   <|> term

term :: Parser Int
term = do char '('
          x <- expr
          char ')'
          return x
   <|> int

strangeMath :: String -> Int
strangeMath = fst . head . parse expr . filter(/=' ')

main = readFile "input.txt" >>= print . sum . map strangeMath . lines
