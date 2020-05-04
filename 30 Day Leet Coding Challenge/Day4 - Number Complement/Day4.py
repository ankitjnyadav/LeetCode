'''
Problem Statement - https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
'''

def findComplement(num: int) -> int:
    bnum = bin(num).replace("0b", "")
    comp = ''
    for i in bnum:
        if i=='0':
            comp += '1'
        elif i=='1':
            comp += '0'
    comp=int(comp, 2)
    return int(comp)

print(findComplement(5))