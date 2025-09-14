def longestUnique(myStr):
    mySet = set()
    strLen = len(myStr)
    start = 0
    maxlen = 0
    for end in range(strLen):
        while myStr[end] in mySet:
            mySet.remove(myStr[start])
            start+=1
        mySet.add(myStr[end])
        maxlen = max(maxlen, end-start+1)
    return maxlen

myStr = "absdecchab"
maxLen = longestUnique(myStr)
print(f'{maxLen}')