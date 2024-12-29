from math import comb

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        return m * pow(m - 1, n - k - 1, mod) * comb(n - 1, k) % mod

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return m

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD

        # (100/5) %7 = 6
        # (100%7) * (5^(-1)%7) = 6
        # x = 5^(-1)%7 means 5*x % 7 == 1 (5 and 7 has to be coprime)
        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in reversed(range(n)):
            invfact[i] = invfact[i+1] * (i+1) % MOD

        def C_n_r(n, r):
            if r < 0 or r > n:
                return 0
            return (fact[n] * invfact[r] % MOD) * invfact[n-r] % MOD
        
        # 111 22222 33
        # runs = n - k
        
        # 插空法
        choose = C_n_r(n-1, k)    

        # 添色问题
        return (choose * m % MOD) * pow(m-1, n-k-1, MOD) % MOD