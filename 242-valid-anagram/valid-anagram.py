class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char_s in s:
            char_count[char_s] = char_count.get(char_s, 0) + 1
        for char_t in t:
            char_count[char_t] = char_count.get(char_t, 0) - 1
        
        result = all(char == 0 for char in char_count.values())
        return result