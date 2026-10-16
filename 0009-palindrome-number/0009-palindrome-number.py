class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev_num = 0
        while temp > 0:
            dig = temp % 10
            rev_num = (rev_num * 10) + dig
            temp = temp // 10
        if(rev_num  == x):
            return True
        else:
            return False
        