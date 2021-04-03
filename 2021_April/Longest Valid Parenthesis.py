def longestValidParentheses_1( s: str) -> int:
    open_brace = 0
    close_brace = 0
    valid = 0
    for i in s:
        if i == '(':
            open_brace += 1
            # print('IF', open_brace)
        elif i == ')':
            close_brace += 1
            # print('ELIF', close_brace)
    if open_brace >= close_brace:
        valid = min(open_brace,close_brace)*2
    return valid
    # return total
def longestValidParentheses_2( s: str) -> int:
    stack=[]
    max_stack=[]
    count=0
    for i in s:
        if i == '(':
            if len(stack)!=0:
                if stack[-1]=='(':
                    max_stack.append(count)
                    count=0
                    stack.clear()
                    stack.append('(')
            else:
                stack.append('(')
        elif i == ')' and len(stack)!=0:
            stack.pop()
            count+=1
    print(count*2)
    return count*2

def longestValidParentheses(s: str) -> int:
    stack = [-1]
    ans = 0
    for i in range(len(s)):
       if s[i] == "(":
          stack.append(i)
       else:
          if stack and stack[-1]!=-1 and s[stack[-1]] == "(":
             stack.pop()
             ans = max(ans,i - stack[-1])
          else:
            stack.append(i)
    return ans
longestValidParentheses(s="(()")