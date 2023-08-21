# https://leetcode.com/problems/contains-duplicate/
# integer array given
# if duplicates, yes
# if not , false

class solution:
    def contains_duplicates():
        unique_nums = set()

        for num in nums:
            if num in unique_nums:
                return ("true")
            unique_nums.add(num)
        return("false")
