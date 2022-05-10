## リュカの定理

# p-1C0~p-1Cp-1を動的計画法により求める
# comb[i][j]: iCj mod p (i>=j, i<jの部分は0のまま)
# iCj = i-1Cj-1 + i-1Cj --- (1)
def ncr_mod_p(p):
    comb = [[0] * p for _ in range(p)]
    comb[0][0] = 1
    for i in range(1, p):
        # 各行先頭はp-1C0=1
        comb[i][0] = 1
        # i>=j, j>=1なるjのみについて
        for j in range(i, 0, -1):
            # 定理(1)から二項係数を以下のように計算できる
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % p
    return comb

# リュカの定理によりnCr mod pを求める
# O(p**2 + logp(n))
def ncr_lucas(n, r, p):
    ret = 1
    # あらかじめp-1C0~p-1Cp-1を求めておく(O(p**2))
    comb = ncr_mod_p(p)
    while n > 0:
        ni = n % p
        ri = r % p
        ret *= comb[ni][ri]
        ret %= p
        n //= p
        r //= p
    return ret