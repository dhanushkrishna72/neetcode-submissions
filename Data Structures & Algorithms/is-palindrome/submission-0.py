class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "".join(char.lower() for char in s if char.isalnum())
        if(newStr[::-1] == newStr):
            return True
        else:
            return False