#Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        start = 0
        current_sum = 0
        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target:
                current_length = end - start + 1
                min_length = min(min_length, current_length)
                current_sum -= nums[start]
                start+=1
            current_length = end - start + 1
        if min_length == math.inf:
            return 0
        else:
            return min_length