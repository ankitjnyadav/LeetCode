class Solution:
    def isHappy(self, n):
        s = str(n)
        sum = 0
        for i in range(len(s)):
            sum = sum + int(s[i]) ** 2
        print(n, sum)
        if sum == 1:
            return True
        else:
            self.isHappy(sum)


    isHappy(19)