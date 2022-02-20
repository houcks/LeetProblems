class Solution:
    def sumZero(self, n: int) -> List[int]:
        sumZero = []
        tempNum = 0;
        if(n == 0):
            return []
        if(n % 2 == 1):
            sumZero.append(0)
            for i in range (1, n):
                if(i % 2 == 1):
                    sumZero.append(i)
                else:
                    sumZero.append(-(i - 1))
        else:
            for i in range (1, n + 1):
                if(i % 2 == 1):                
                    sumZero.append(i)
                else:
                    sumZero.append(-(i - 1))
        return sumZero