"""
Eleven scientists are working on a secret project. They wish to lock up the 
documents in a cabinet so that the cabinet can be opened if and only if six 
or more of the scientists are present. What is the smallest number of locks needed? 
What is the smallest number of keys to the locks each scientist must carry?
"""

from math import comb

# number of locks would be the combination of scientists and the threshold
def calculate_locks(scientists, threshold):
    return comb(scientists, threshold)

# number of keys would be teh combiation of scientists - 1 and threshold -1
def calculate_keys(scientists, threshold):
    return comb(scientists- 1, threshold -1)

scientists = 11 
threshold = 6

locks = calculate_locks(scientists, threshold)
keys = calculate_keys(scientists, threshold)

print(locks, keys)