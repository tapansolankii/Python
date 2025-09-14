from collections import Counter

def count_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    start = 0
    result = 0
    for end in range(len(s)):
        s_count[s[end]]+=1
        if end-start+1 > len(p):
            s_count[s[start]]-=1
            if s_count[s[start]] == 0:
                del s_count[s[start]]
            start+=1
        if (s_count == p_count):
            result+=1
    return result

# Example Usage
s = "cbaebabacd"
p = "abc"
print(count_anagrams(s, p))  # Output: 2