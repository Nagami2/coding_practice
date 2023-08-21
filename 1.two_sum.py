class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # iterate the items in nums[2,7,11,15] 9
        # find conmplement and see if it is in remaining nums
        
        nums_dict ={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[num] = i
        return []
    