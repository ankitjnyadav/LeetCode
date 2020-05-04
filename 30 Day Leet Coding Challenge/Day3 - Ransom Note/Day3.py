'''
Problem Statement - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
'''

'''

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''
class Solution:
    def canConstruct(self,ransomNote: str, magazine: str) -> bool:
        '''
        ransomNoteStack = []
        magazineStack = []
        for i in ransomNote:
            ransomNoteStack.append(i)
        for j in magazine:
            magazineStack.append(j)
        for i in range(len(ransomNoteStack)):
            if len(magazineStack) != 0:
                for j in range(len(magazineStack)):
                    print('Checking {}=={}'.format(ransomNoteStack[i],magazineStack[j]))
                    if ransomNoteStack[i]==magazineStack[j]:
                        magazineStack.pop(j)
                        ransomNoteStack.pop(i)
                        print(ransomNoteStack, len(ransomNoteStack))
                        print(magazineStack, len(magazineStack))

        print(ransomNoteStack,len(ransomNoteStack))
        print(magazineStack, len(magazineStack))
        if len(ransomNoteStack) == 0:
            return True
        else:
            return False
        '''
        """
                :type ransomNote: str
                :type magazine: str
                :rtype: bool
                """
        cnt = dict([])
        lr = list(ransomNote)  # convert into str
        lm = list(magazine)  # convert into str
        for i in range(len(lm)):
            if lm[i] in cnt.keys():
                cnt[lm[i]] += 1  # count letter times
            else:
                cnt[lm[i]] = 1
        for i in range(len(lr)):  # check if letter times is able to construct ransomNote.
            if lr[i] not in cnt.keys() or cnt[lr[i]] == 0:
                return False
            cnt[lr[i]] -= 1
        return True

print(Solution.canConstruct(Solution,"b",""))
print(Solution.canConstruct(Solution,"bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
