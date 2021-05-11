# https://leetcode.com/problems/split-a-string-in-balanced-strings/
def balancedStringSplit(s: str) -> int:
    r = l = 0
    balanced = 0
    for i in s:
        if i == 'R':
            r += 1
        else:
            l += 1
        if l == r:
            balanced += 1
            r = l = 0
    return balanced


# Approach 2 - Using Stack
def balancedStringSplit_2(s: str) -> int:
    stack = []
    result = 0
    for c in s:
        if stack == []:
            stack.append(c)
            result += 1
        elif c == stack[-1]:
            stack.append(c)
        else:
            stack.pop()
    return result


print(balancedStringSplit("RLRRRLLRLL"))
