## ユークリッドの互除法による最大公約数と最小公倍数の算出

# 最大公約数
# O(a+b)
def gcd(a, b):
    while a >= 1 and b >= 1:
        if a < b:
            b %= a
        else:
            a %= b
    if a >= 1:
        return a
    else:
        return b
    

# 最小公倍数
# gcd()が必要
# lcm = a*b//gcd
def lcm(a, b):
    return a * b // gcd(a, b)