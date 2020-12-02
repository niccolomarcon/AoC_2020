input ← ⊃ ⎕NGET 'Desktop/AoC/day_02/input.txt' 1
sample ← ⊃ input
read ← {2 (⍎¨⍤↑ , ↓) ⍵ (~⍤∊ ⊆ ⊣) '-: '}
count ← {+/ 3 (⊃ = ⊃⍤↓) ⍵}
old_valid ← {(⊣{(1⌷⍺)≤⍵∧(2⌷⍺)≥⍵}count) read ⍵}
P1 ← {+/old_valid¨⍵}
