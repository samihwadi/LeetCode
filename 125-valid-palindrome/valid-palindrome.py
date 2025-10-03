class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_str = ''.join(x for x in s if x.isalnum()).lower()
        return check_str == check_str[::-1]
        