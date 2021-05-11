def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    #Approach 1
    s[:] = s[::-1]
    #Approach 2
    i = 0
    for c in s[::-1]:
        s[i] = c
        i = i + 1



reverseString(["h","e","l","l","o"])