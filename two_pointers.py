## 尺取法
# while1重尺取法
# https://zenn.dev/luke256/articles/0d60a95fd86ffa

# 雛形
'''
n = int(input())
l = 0
r = 0
while l < n:
    if r == n or '条件を満たさない':
        # 処理a
        l += 1
    else:
        # 処理a'
        r += 1
    # 処理b
'''
    

# 具体例
# https://atcoder.jp/contests/abc032/tasks/abc032_c
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

# コーナーケース対処
# k=0なら，要素に0があれば最長でも満たすのでn
# 0がなければどんな長さでも満たさないので0
if k == 0:
    if 0 in set(s):
        print(n)
        exit()
    else:
        print(0)
        exit()

l = 0
r = 0
# 暫定的な積
product = 1
ans = 0
while l < n:
    # rが最後の要素を指す，もしくは積が条件を満たしていないとき
    if r == n or product > k:
        # 左端の要素を積から除外し
        product //= s[l]
        # 左端をひとつ右にずらす
        l += 1
    else:
        # 条件を満たしているときは，右端をひとつ右に進める
        product *= s[r]
        r += 1
        
    # 今見ている範囲の長さが大きいならmaxを更新する
    if product <= k:
        # ここに来るとき，右端がインクリメントされた状態でくるので，
        # r-l+1でなくてよい
        ans = max(ans, r-l)
        
    # 積が0になることがあれば最長でも満たすのでnを出力して終了する
    if product == 0:
        print(n)
        exit()

print(ans)