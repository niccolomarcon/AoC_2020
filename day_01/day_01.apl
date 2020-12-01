report ← ⍎¨ ⊃ ⎕NGET 'Desktop/AoC/day_01/input.txt' 1
tuples ← {((≢⍵)*2)⍴⍵∘.,⍵} report
filter ← {{⍵=2020}¨+/¨⍵} tuples
solve ← {×/⊃filter/tuples}
