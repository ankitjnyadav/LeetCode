'''
Problem Statement - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
'''


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            for j in J:
                if (i == j):   count += 1
        return count
