
"""
Step-1
[8, 3, 5, 1]

↓

[8, 3]     [5, 1]

↓

[8] [3]    [5] [1]

step-2
[8] + [3]

Compare:

8 vs 3

3 chhota hai → pehle aayega

Result:

[3, 8]

step-3
[5] + [1]

↓

[1, 5]

final merge
[3, 8] + [1, 5]

Compare:

3 vs 1 → 1
3 vs 5 → 3
8 vs 5 → 5
8 bacha → 8

Final:

[1, 3, 5, 8]


"""
