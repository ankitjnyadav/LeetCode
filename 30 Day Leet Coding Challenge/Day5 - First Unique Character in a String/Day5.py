class Solution1:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:    return -1
        for i in range(len(s)):
            flag = False
            count=0
            for j in range(len(s)):
                if s[i] == s[j]:
                    count+=1
                    flag=True
                if(count==1 and j==len(s)-1):
                    return i
            if (not flag and i == len(s) - 1):
                return -1


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        list_ = list(s)

        dict_ = Counter(s)

        for key in dict_.keys():
            if dict_[key] == 1:
                return list_.index(key)

        return -1


# ================================================

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict_ = Counter(s)

        for ind, ch in enumerate(s):
            if dict_[ch] == 1:
                return ind

        return -1

print(Solution.firstUniqChar(Solution,"cc"))
#print(Solution.firstUniqChar(Solution,"loveleetcode"))