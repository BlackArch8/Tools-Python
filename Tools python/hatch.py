from itertools import combinations, combinations_with_replacement
import itertools 
import random  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return set(list(combinations_with_replacement(arr, r)))
  
# Driver Function 
if __name__ == "__main__": 
    arr = [1, 2, 3, 4] 
    r = 2
    print (rSubset(arr, r))

# sub = itertools.combinations_with_replacement('ABCD',2)
# print(sub)