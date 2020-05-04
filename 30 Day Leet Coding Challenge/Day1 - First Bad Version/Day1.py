'''
Problem Statement - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def isBadVersion(n):
        if n >= 4:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1;
        begin = 1
        end = n
        while begin < end:
            mid = begin + (end - begin) / 2
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1
        return int(begin)