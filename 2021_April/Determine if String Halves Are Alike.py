'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.


'''
class Solution:
    def checkVowel(self,ch: str) -> int:
        if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
            return 1
        else:
            return 0

    def halvesAreAlike(self, s: str) -> bool:
        first_half = []
        second_half = []
        for i in range(len(s)):
            if i < len(s) // 2:
                first_half.append(self.checkVowel(s[i].upper()))
            else:
                second_half.append(self.checkVowel(s[i].upper()))
        if first_half.count(1)==second_half.count(1):
            return True
        else:
            return False

