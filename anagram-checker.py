# Sorting Method, time complexity is O( n log n )

# def is_anagram(s1: str, s2:str) -> bool :
#     s1 = "".join(sorted(s1))
#     s2 = "".join(sorted(s2))

#     return True if s1 == s2 else False

# Dictionary Method
# def is_anagram(s1: str, s2:str) -> bool :
#     dt1 = dict()
#     for c in s1:
#         if c in dt1:
#             dt1[c] += 1
    
#         else:
#             dt1[c] = 1.............

# 

# Using Default dict 

# from collections import defaultdict

# dt1 = defaultdict(int)
# for c in s1:
#     dt1[c] += 1..........

# Counter Method

from collections import Counter

def is_anagram(s1:str, s2:str) -> bool:
    return Counter(s1) == Counter(s2)