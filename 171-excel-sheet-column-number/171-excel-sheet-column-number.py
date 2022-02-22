class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for x in range(len(columnTitle)):
            num += (ord(columnTitle[len(columnTitle) - 1 - x]) - 64) * (26**(x))
        return num