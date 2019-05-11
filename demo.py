from paillier import *

print("Generating key pair...")
n, g, l, m = keyGen(2048)
print("Generated key pair.")
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