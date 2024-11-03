class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        magazine_dict = {}

        for i in ransomNote:
            ransom_dict[i] = ransom_dict[i] + 1 if i in ransom_dict else 1

        for i in magazine:
            magazine_dict[i] = magazine_dict[i] + 1 if i in magazine_dict else 1

        for key in ransom_dict:
            if key not in magazine_dict:
                return False
            if ransom_dict[key] > magazine_dict[key]:
                return False

        return True


ransomNote = "aa"
magazine = "ab"


print(Solution().canConstruct(ransomNote, magazine))
