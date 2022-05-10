## 階乗
# n!まですべて求める
def factorial(n):
    factorial = [1] * (n+1) # 1-indexとして使えるようにするため
    for i in range(1, n):
        factorial[i+1] = ((i+1) * factorial[i])
        
    return factorial