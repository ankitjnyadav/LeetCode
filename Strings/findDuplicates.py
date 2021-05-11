def printDups(s='GeeksForgeeks TemP'):
    mydict={}
    for i in s:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i] = 1
    for k,v in mydict.items():
        if v>1:
            print(k,end='')