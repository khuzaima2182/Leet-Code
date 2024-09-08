class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #The dictionary of Roman Counting Letters
        roman_Letters = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        result = 0 #The final result(Counting Number) from the Roman letters

        for i in range(len(s)):
            if i < len(s) - 1 and roman_Letters[s[i]] < roman_Letters[s[i+1]]:
                result-=roman_Letters[s[i]]
            else:
                result+=roman_Letters[s[i]]

        return result

solution = Solution()
print(solution.romanToInt("IV"))
        
        