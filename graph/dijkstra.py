## ダイクストラ法
# 優先度付きキューを使用するもの(疎グラフ向け)
# O(V+ElogV)
# グラフが単純かつ全頂点へ始点から到達可能と仮定すると
# V-1 <= E <= V(V-1)
from heapq import *

# よくあるinput
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    # 重み付き無向グラフ
    edges[a].append((b, c))
    edges[b].append((a, c))

# ダイクストラ法による単一始点最短経路の算出
def dijkstra(s):
    dist = [float('inf')] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        # スタートからの暫定距離が最も小さいものを取り出すため優先度付きキューを使用する
        dist_to_v, v = heappop(q)
        # ここに入るなら，すでに別の所から来る経路でdistがより短いものが見つかっている
        if dist[v] < dist_to_v: continue
        for to, cost in edges[v]:
            if dist_to_v + cost < dist[to]:
                dist[to] = dist_to_v + cost
                heappush(q, (dist[to], to))
    return dist