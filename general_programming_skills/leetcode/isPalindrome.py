class Solution:
    def isPalindrome(self, x: int):

        new = str(x)
        if new == new[::-1]:
            return True
        else:
            return False


output = Solution()
print(output.isPalindrome(1576521))




