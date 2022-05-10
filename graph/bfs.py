## 幅優先探索
# キューによる実装
from collections import deque

# よくあるinput
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

# bfs
que = deque() # 次に見る頂点を格納する
que.append(0) # はじめ，0番頂点をスタートとする
cost = [-1] * n # 各頂点への最短距離
cost[0] = 0 # 頂点0の距離を0とする

while len(que):
    # キューの左端を取り出す
    frm = que.popleft()
    # frmからいける各頂点について
    for to in edges[frm]:
        # 未訪問であれば
        if cost[to] == -1:
            # frmから1手でいけるので，cost++
            cost[to] = cost[frm] + 1
            # 行き先を次のfrmにするためキューの右端へ追加
            que.append(to)