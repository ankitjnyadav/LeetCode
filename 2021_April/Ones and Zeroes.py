class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.helper(strs, m, n, 0)
        '''
            l=[]
            for i in strs:
                #while m!=0 and n!=0:
                if i=='0' and m!=0:
                    l.append(i)
                    m-=1
                    print(l)
                elif i=='1' and n!=0:
                    l.append(i)
                    n-=1
                    print(l)
                else:
                    s1=''
                    for x in i:
                        if x=='0' and m!=0:
                            s1+=x
                            m-=1
                        elif x=='1' and n!=0:
                            s1+=x
                            n-=1
                    if len(s1)!=0:  l.append(s1)        
            return len(l)
        '''

    def helper(self, strs, m, n, idx):
        if idx == len(strs):
            return 0
        take_curr_str = -1
        count0, count1 = strs[idx].count('0'), strs[idx].count('1')
        if m >= count0 and n >= count1:
            take_curr_str = max(take_curr_str, self.helper(strs, m - count0, n - count1, idx + 1) + 1)
        not_take_curr_str = self.helper(strs, m, n, idx + 1)
        return max(take_curr_str, not_take_curr_str)