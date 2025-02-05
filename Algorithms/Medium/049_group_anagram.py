class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp: dict = {}

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in mp:
                mp[word].append(strs[i])
            else:
                mp[word] = [strs[i]]

        return list(mp.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs=strs))
