class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Cleanup string
        clean_str = "".join(x for x in s if x.isalnum()).lower()
        length = len(clean_str)
        mid = (length // 2)
        # Have Two Pointers in the middle of the string
        i, j = 0, 0
        # If even, start at mid and mid - 1
        if length % 2 == 0:
            i = mid
            j = mid - 1
        # If odd length, pointers start at same position
        else:
            i, j = mid, mid
        
        while i < length:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1
        return True
        