class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            sorted_s = "".join(sorted(word))
            res[sorted_s].append(word)
        return list(res.values())