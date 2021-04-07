'''

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.



'''

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # total = (2i+1 for i in xrange(n)) = n^2
        # left_half_total = (2i+1 for i in xrange(n//2)) = (n//2)^2
        # result = (n//2) * (total//n) - left_half_total = (n//2)*(n-n//2) = (n//2)*((n+1)//2)
        return (n//2)*((n+1)//2)