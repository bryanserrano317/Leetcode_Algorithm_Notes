from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # declare a hash map
        for i in range(len(nums)): # iterate through each value in the list
            hashmap[nums[i]] = i # add each value from the list as a key to the hash table and the index as a value
        for i in range(len(nums)): # iterate through each value in the list
            complement = target - nums[i] # check for the last remaining value (j)
            if complement in hashmap and hashmap[complement] != i: # if j is in hashmap and hashmap key is not i (cannot use same val twice)
                return [i, hashmap[complement]]  # return i and j 

# one pass look up (one for loop) (best space complexity)

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # declare a hash map
        for i in range(len(nums)): # iterate through each value in the list
            complement = target - nums[i] # check for the last remaining value (2)
            if complement in hashmap: # if value 2 is in hashmap 
                return [i, hashmap[complement]]  # return i (value 1) and j (value 2)
            hashmap[nums[i]] = i #(value 1)