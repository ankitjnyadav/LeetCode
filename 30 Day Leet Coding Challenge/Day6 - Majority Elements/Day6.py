'''
Problem Statement - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
'''

from collections import Counter

class Solution:
    def majorityElement_slow(self, nums: List[int]) -> int:
        #O(n^2)
        track = {}
        isMajorityElement = len(nums) / 2
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    track.update({nums[i]: count})
        for k, v in track.items():
            if v >= isMajorityElement:
                return k

    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) // 2
        majority = nums[0]

        for key in counter.keys():
            if counter[key] > n and counter[key] > counter[majority]:
                majority = key
        return majority
