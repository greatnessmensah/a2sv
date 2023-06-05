class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        original_num = x
        rev_num = 0
        while x > 0:
            last_digit = x % 10
            x = x // 10
            rev_num = rev_num*10 + last_digit

        return original_num == rev_num
