# https://leetcode.com/problems/contains-duplicate/
# integer array given
# if duplicates, yes
# if not , false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # visted set
        visited = set()
        # go through the nums, if not visited, add
        # if already visited return true
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False
    
# IO parameters to the function
        
