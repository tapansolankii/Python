def convert(s:str, n:int) -> str:
    if(len(s)<=n or n==1):
        return s
    direction = 1
    row = 0
    rows = [""]*n
    for c in s:
        # print(c)
        rows[row] += c
        if(row==0):
            direction=1
        if(row == n-1):
            direction=0
        if(direction):
            row+=1
        else:
            row-=1
    # print(rows[0])
    # print(rows[1])
    # print(rows[2])
    answer = ""
    for a in rows:
        answer += a
    # print(answer)
    return answer



# Example usage
s1 = "PAYPALISHIRING"
numRows1 = 3
print(convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

s3 = "A"
numRows3 = 1
print(convert(s3, numRows3))  # Output: "A"