# プリム法により最小全域木を求める
from heapq import heappush, heappop


# よくあるinput
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))
    
    
# プリム法
# 訪問済み頂点を保存する配列
visited = [False for _ in range(n)]
visited[0] = True
# 重み最小の頂点を取り出すための優先度付きキュー
q = []
# 頂点0に隣接する辺を保存
for to, cost in edges[0]:
    heappush(q, (cost, to))

while q:
    # 最小の重みの辺をheapで取り出す
    cost_frm, frm = heappop(q)

    # 訪問済みならスキップ
    if visited[frm]:
        continue

    # 訪問したことを記録
    visited[frm] = True
    
    # 頂点frmに隣接する頂点について
    for to, cost_to in edges[frm]:
        # 訪問済みならばスキップ
        if visited[to]:
            continue

        heappush(q, (cost_to, to))