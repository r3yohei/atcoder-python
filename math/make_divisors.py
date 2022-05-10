## 約数列挙

# nの約数を列挙する
# O(√n)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        # 約数でないなら飛ばす
        if n % i != 0:
            continue
        # 約数を追加
        divisors.append(i)
        # さらに，n//iも約数になるので追加
        # i == n//iは，16=4*4などの平方根のときに成り立つ
        if i != n//i:
            divisors.append(n//i)
    
    divisors.sort()
    return divisors

# nをn=div_1*div_2なる(div_1, div_2)の組で表す
def make_pair_of_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        div_1 = 0
        div_2 = 0
        if n % i == 0:
            div_1 = i
            if i != n // i:
                div_2 = n // i
                divisors.append((div_1, div_2))
            else:
                divisors.append((div_1, div_1))
                
    divisors.sort()
    return divisors