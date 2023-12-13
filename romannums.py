class Solution:
    def romanToInt(self, s: str) -> int:
        chars = list(s)
        orders = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        values={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        while len(chars) != 0:
            checking = chars[0]
            if orders.get(checking) == None:
                value = values.get(checking)
                chars.pop(0)
            else:
                if len(chars) > 1:
                    if chars[1] in orders.get(checking):
                        value = values.get(chars[1]) - values.get(checking)
                        chars.pop(0)
                        chars.pop(0)
                    else:
                        value = values.get(checking)
                        chars.pop(0)
                else:
                    value = values.get(checking)
                    chars.pop(0)
            sum += value
        return sum


a = Solution()
print(a.romanToInt('MCMXCIV'))
