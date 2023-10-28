class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = 0
        np = 0
        for i in range(1, n + 1):
            flag = 0
            for j in range(2, int(i**0.5)+1):
                if (i % j == 0):
                    np += 1
                    flag = 1
                    break
            if not flag:
                prime += 1
        prime = prime -1
        res = math.factorial(prime) * math.factorial(n-prime)
        return( res % (10 ** 9 + 7))
