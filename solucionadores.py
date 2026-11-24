from modelos import ISolucionador
class DP(ISolucionador):
    def __init__(self, paquetes): self.t = [p.viajes for p in paquetes]
    def resolver(self, n):
        dp, e = [0] + [99] * n, [0] * (n + 1)
        for i in range(1, n + 1):
            for p in self.t:
                if p <= i and dp[i - p] + 1 < dp[i]: dp[i], e[i] = dp[i - p] + 1, p
        r, i = [], n
        while i > 0: r.append(e[i]); i -= e[i]
        return dp[n], r
    
class Greedy(ISolucionador):
    def __init__(self, paquetes): 
        self.t = sorted((p.viajes for p in paquetes), reverse=True)
    def resolver(self, n):
        r = []
        for p in self.t:
            while n >= p: r.append(p); n -= p
        return len(r), r
