## 素数にまつわるスクリプト

# 素数判定
# O(√n)
def is_prime(n):
    # 1~√nまででnを割り切るものがあれば素数でない
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True


# 素因数分解
# is_prime()が必要
def prime_factorization(n):
    factor = []
    if is_prime(n):
        factor.append(n)
        return factor
    else:
        for i in range(2, int(n**0.5)+1):
            # 例えば，2で割れるだけ割り，素因数をfactorへ追加
            # こうすることで，次に4を見たときにwhileに入らない
            while n % i == 0:
                n //= i
                factor.append(i)
        
        # forを抜けて残った数が1以外なら，それも素因数なので追加
        if n != 1:
            factor.append(n)
            
        return factor
    

# エラトステネスの篩
# n以下の素数を列挙する
# O(nloglogn)
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    prime = []
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            # iの倍数をすべて消す
            for n in range(i*i, n+1, i):
                is_prime[n] = False
    return prime


# L以上R以下の素数のエラトステネスの篩による列挙
# is_prime[x]: x+Lが素数かどうか
def sieve_of_eratosthenes_from_l_to_r(l, r):
    is_prime = [True] * (r-l+1)
    if l == 1:
        is_prime[0] = False
        
    for i in range(2, int(r**0.5)+1):
        # L以上で最小のiの倍数
        min_value = ((l+i-1) // i) * i
        # L以上R以下のiの倍数すべてを消す
        for j in range(min_value, r+1, i):
            # i自身を直接Falseにしない
            if j == i: continue
            is_prime[j-l] = False
            
    prime = []
    for i in range(r-l+1):
        if is_prime[i]:
            prime.append(i+l)
            
    return prime