from typing import List
# Answers are returned in the format that is accepted by leetcode

"""
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""

nums = [8, 1, 2, 2, 3]


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # make an empty list for the output
        results = []
        # lopp through each number
        for x in nums:
            # count the number of ints < current, append it to the list
            results.append(sum([y < x for y in nums]))
        return results


# ------------------------------------------------------------------------------
"""
Given a non-empty array of integers, 
every element appears twice except for one.
Find that single one.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # make an empty list to hold the odd number
        odd_one_out = []
        # loop through your list of numbers and add the any number not already in list
        for i in nums:
            if i not in odd_one_out:
                odd_one_out.append(i)
            # remove numbers if they are found more than once
            else:
                odd_one_out.remove(i)
        # return the 1st element, should be only element in list
        return odd_one_out[0]
