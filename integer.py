import math
import random

# 模运算 #
def mod(a, n):
    return int(a%n)

# 快速模指数算法 #
'''
input: 底数 g , 指数 a 和模数 p
output: (g**a)mod p
'''
def fast_pow(g, a, p):
    e = mod(a, p - 1)
    if e == 0:
        return 1
    r = int(math.log2(e))# + 1 - 1
    x = g
    for i in range(0, r):
        x = mod(x**2, p)
        if (e & (1 << (r - 1 - i))) == (1 << (r - 1 - i)):
            x = mod(g * x, p)
    return int(x)
### test fast_pow ###
#print(fast_pow(5, 12, 23))

# Miller-Rabin检测 #
'''
input: 大奇数 u 和大正整数 T
output: 若 u 通过测试则输出 True，否则输出 False
'''
def isPrime_MR(u, T):    
    # 计算 v 和 w ，使得 u - 1 = w * 2^v
    v = 0
    w = u - 1
    while mod(w, 2) == 0:
        v += 1
        w = w // 2
    for j in range(1, T + 1):
        nextj = False
        a = random.randint(2, u - 1)
        b = fast_pow(a, w, u)
        if b == 1 or b == u - 1:
            nextj = True
            continue
        for i in range(1, v):
            b = mod(b**2, u)
            if b == u - 1:
                nextj = True
                break
            if b == 1:
                return False
        if not nextj:
            return False
    return True
### test isPrime_MR ###
#print(isPrime_MR(0xBDB6F4FE3E8B1D9E0DA8C0D46F4C318CEFE4AFE3B6B8551F, 10))
#print(isPrime_MR(23, 10))
#print(isPrime_MR(17, 10))

# 求逆元
def inverse(a, n):
    a_ = fast_pow(a, n - 2, n)
    return a_
### test inverse ###
#print(inverse(3,7))

# 输出一个 'bitlen' 比特长的素数
def randprime(bitlen):
    lowbound = (1 << bitlen) + 1
    upbound = (1 << (bitlen + 1)) - 1
    while(True):
        rint = random.randint(lowbound, upbound)
        if isPrime_MR(rint, 15):
            return rint
### test randprime ###
#print(randprime(1000))

# 交换两个数
def swap(a, b):
    return b, a

# 判断是否为偶数
def is_even(a):
    if (a%2) == 0:
        return True
    else:
        return False

# 输出两个数的最大公因子
# 使用 Stein 算法
def gcd(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        if a != 0:
            a, b = swap(a, b)
        else:
            return 0
    k = 0
    while is_even(a) and is_even(b):
        a /= 2
        b /= 2
        k += 1
    if is_even(b):
        a, b = swap(a, b)
    while True:
        while is_even(a):
            a /= 2
        if a < b:
            a, b = swap(a, b)
        a = (a - b)/2
        if a == 0:
            d = int(b * (2**k))
            return d
### test gcd ###
#print(gcd(1543535,276465))

# 输出两个数的最小公倍数
def lcm(a, b):
    return int((a * b)/gcd(a, b))
### test lcm ###
#print(lcm(142353,65134))