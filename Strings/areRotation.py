def areRotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        temp=str1+str1
        if str2 in temp:
            return True
        else:
            return False


print(areRotation('ABCD','ADBC'))