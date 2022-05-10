## 繰り返し二乗法
# a**b mod m
# 任意のb = k0*2**0 + k1*2**1 + ... + kn*2**nと書ける(ki = {0, 1})
# bの二進表記は求められるので，それで1が立った桁がki = 1
# 故にki = 1の部分についてのみ，a**(2**i) % mを足し合わせればよい
# O(logb)
def modpow(a, b, m):
    # bを二進数にする
    bin_b = bin(b)
    # 1桁目から見るために反対にする
    re_bin_b = ''.join(list(reversed(bin_b[2:]))) #0bで始まるので[2:]

    ret = 1
    p = a
    for i in range(len(re_bin_b)):
        # i桁目に1が立っていれば，かけ合わせてmodを取る
        if re_bin_b[i] == '1':
            ret *= p
            ret %= m
        # a**(2**i)は，bの二進表記に1が立っているかどうかに関わらず毎回計算しておく．
        #これは，毎回のforループでp *= pとすることに相当する．
        p *= p
        p %= m
            
    return ret % m


# a/b mod m
# modpow()が必要
def division(a, b, m):
    # bのmod mでのモジュラ逆数をフェルマーの小定理により求め，aにかけてmod mを取る
    return (a * modpow(b, m-2, m)) % m