## 深さ優先探索
# 再帰関数による実装
# 再帰上限解放
import sys
sys.setrecursionlimit(10**7)

# よくあるinput
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

# dfs
# n: 頂点数
# edges: 頂点と辺の隣接リスト表現
visited = [False] * n
def dfs(x):
    # xに訪問できるので書き換える
    visited[x] = True
    # xから行ける頂点のうち，未訪問のものへ行く
    for to in edges[x]:
        if not visited[to]:
            dfs(to)