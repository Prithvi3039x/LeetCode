class Solution(object):
    def isPalindrome(self, s):
        n = "".join(ch.lower() for ch in s if ch.isalnum())
        return n == n[::-1]
        