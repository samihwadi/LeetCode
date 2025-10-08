class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits))) + 1
        result = []
        for d in str(num):
            result.append(int(d))
        return result