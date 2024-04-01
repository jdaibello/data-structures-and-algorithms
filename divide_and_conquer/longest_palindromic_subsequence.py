def findLongestPalindromicSubsequence(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLongestPalindromicSubsequence(s, startIndex + 1, endIndex - 1)
    else:
        op1 = findLongestPalindromicSubsequence(s, startIndex, endIndex - 1)
        op2 = findLongestPalindromicSubsequence(s, startIndex + 1, endIndex)
        return max(op1, op2)

print(findLongestPalindromicSubsequence("ELRMENMET", 0, 8)) # 5