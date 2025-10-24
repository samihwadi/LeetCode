class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {}
        romans["I"] = 1
        romans["V"] = 5
        romans["X"] = 10
        romans["L"] = 50
        romans["C"] = 100
        romans["D"] = 500
        romans["M"] = 1000

        result = 0

        for i in range(len(s)):
            if i+1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                result -= romans.get(s[i])
            else:
                result += romans.get(s[i])
        return result
