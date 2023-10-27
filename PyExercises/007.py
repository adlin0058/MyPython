
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(needle)
        l2 = len(haystack)
        if needle in haystack:
            for i in range(0, l2 - l1 + 1):
                if haystack[i:i+l1] == needle:
                    return i
        else:
            return -1
