import integer

# 函数 L = (x - 1) / n #
def funcL(x, n):
    return (x - 1) // n

# 产生一个模 n 乘法循环群中的随机元素 #
def sampleGen(n):
    g = integer.random.randint(1, n - 1)
    while integer.gcd(g, n) != 1:
        g = integer.random.randint(1, n - 1)
    return g
# 密钥生成算法 #
'''
input: 大整数 n 的比特长度
output: 公钥(n, g) 和 私钥 (λ, μ)
'''
def keyGen(sbit):
    p = integer.randprime(int(sbit/2))
    q = integer.randprime(int(sbit/2))
    while integer.gcd(p*q, (p-1)*(q-1)) != 1:
        p = integer.randprime(int(sbit/2))
        q = integer.randprime(int(sbit/2))
    n = p * q
    n2 = n * n
    
    lamb = integer.lcm(p - 1, q - 1)
    g = sampleGen(n2)
    while integer.gcd(funcL(integer.fast_pow(g, lamb, n2), n), n) != 1:
        g = sampleGen(n2)
    miu = integer.inverse(funcL(integer.fast_pow(g, lamb, n2), n), n, (p - 1) * (q - 1))
    
    '''
    lamb = (p - 1) * (q - 1)
    g = n + 1
    miu = inverse(lamb, n, lamb)
    '''

    return n, g, lamb, miu
### test keyGen ###
'''
n, g, l, m = keyGen(2048)
print("public key:")
print("n = " + str(n))
print("g = " + str(g))
print("private key:")
print("λ = " + str(l))
print("μ = " + str(m))
'''

# 加密 #
'''
input: 明文消息 m, 公钥 n, g
output: 密文 c
'''
def encrypt(m, n, g):
    if m < 0 or m >= n:
        raise Exception("message m must be not less than 0 and less than n")
    
    r = integer.random.randint(1, n - 1)
    n2 = int(n**2)
    while integer.gcd(r, n2) != 1:
        r = integer.random.randint(1, n - 1)
    
    '''
    r = randprime(int(math.log2(n)))
    while r > n - 1:
        r = randprime(int(math.log2(n)))
    n2 = n * n
    '''
    c = integer.mod(integer.fast_pow(g, m, n2) * integer.fast_pow(r, n, n2), n2)
    return c

# 解密 #
'''
input: 密文 c, 公钥 n, g, 私钥 λ, μ
output: 恢复明文 m_bar
'''
def decrypt(c, n, g, lamb, miu):
    n2 = n * n
    if integer.gcd(c, n2) != 1:
        print("error")
    if c < 1 or c >= n2 or integer.gcd(c, n2) != 1:
        raise Exception("cipher c must be in Group Z_*_n^2")
    m_bar = integer.mod(funcL(integer.fast_pow(c, lamb, n2), n) * miu, n)
    return m_bar

# 密文下的明文相加 #
'''
input: 密文 c1, c2, 公钥 n
output: 相加后的密文 c1 + c2
'''
def plaintextAdd(c1, c2, n, g):
    n2 = n * n
    c_ = integer.mod(c1 * c2, n2)
    return c_

### test paillier cryptsystem ###
'''
n, g, l, m = keyGen(2048)
plaintext1 = 1234
plaintext2 = 4321
c1 = encrypt(plaintext1, n, g)
c2 = encrypt(plaintext2, n, g)
print("c1: " + str(c1))
print("c2: " + str(c2))
c_ = plaintextAdd(c1, c2, n, g)
print("c_: " + str(c_))
m1 = decrypt(c1, n, g, l, m)
print("m1: " + str(m1))
m2 = decrypt(c2, n, g, l, m)
print("m2: " + str(m2))
m_bar = decrypt(c_, n, g, l, m)
print("m_bar: " + str(m_bar))
'''