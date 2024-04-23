""" 
module providing functions por statistics.
"""
from statistics import *
# when we use "#" we mean that we're gonna import all the modules from statistics

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
