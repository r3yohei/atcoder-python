## 01-BFS
# https://betrue12.hateblo.jp/entry/2018/12/08/000020

from collections import deque

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
    
# 01-BFS
dist = [float('inf')] * n
dist[0] = 0
que = deque()
que.append(0)

while len(que):
    # キューの左端を取り出す
    frm = que.popleft()
    for to, cost in edges[frm]:
        d = dist[frm] + cost
        # frmから行ったほうが短いなら更新する
        if d < dist[to]:
            dist[to] = d
            # 辺のコスト1ならば，キューの右端に詰める
            if cost == 1:
                que.append(to)
            # 0ならば，左端に詰める
            else:
                que.appendleft(to)
            # こうすることで，キューの中身の頂点の暫定最短距離が常に(1,1,2,3,4,4,..)
            # のように，左と同じかそれ+1であるように並ぶ
            # 暫定距離が短いものからpopleftしたいのでこうなる
            # ダイクストラでheapqを使うのと同じ気持ち