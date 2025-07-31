"""
LeetCode: https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Examples:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
"""

class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store value: index

        for i, num in enumerate(nums):
            current = target - num #what number do we need

            if current in num_map: #found 2 nums tht add up to target
                return [num_map[current], i]

            num_map[num] = i #store current num and index

        return[] #if no valid pair found

