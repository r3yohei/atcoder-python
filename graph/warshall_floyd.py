## ワーシャルフロイド法
# 全点対最短経路問題を解くアルゴリズム
# O(v**3)

# よくあるinput
n, m = map(int, input().split())
INF = 10**18
cost = [[INF] * n for _ in range(n)] # 頂点i,j間のcostをcost[i][j]で持つ
# 自身への距離は0
for i in range(n):
    cost[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # 問題文で与えられるコスト
    cost[a][b] = c
    
# ワーシャルフロイド法
for k in range(n):
    for i in range(n):
        for j in range(n):
            # ij間はkを経由したほうが短いかを調べる
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])