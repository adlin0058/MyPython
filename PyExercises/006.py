import collections


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    return not collections.Counter(ransomNote) - collections.Counter(magazine)


ransomNote = "aa"
magazine = "aab"
print(collections.Counter(ransomNote))
print(collections.Counter(magazine))
