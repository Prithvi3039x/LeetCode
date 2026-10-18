class Solution(object):
    def lengthOfLastWord(self, s):
        n = s.strip
        k = s.split()
        j = k[len(k) - 1]

        return len(j)
        