from paillier import *
import time

print("Generating key pair...")
n, g, l, m = keyGen(2048)
print("Generated key pair.")
plaintext1 = 1234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234123412341234
plaintext2 = 4321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321432143214321
tstart = time.time()
c1 = encrypt(plaintext1, n, g)
c2 = encrypt(plaintext2, n, g)
tend = time.time()
print("c1: " + str(c1))
print("c2: " + str(c2))
print("average time: " + str((tend - tstart) / 2))
c_ = plaintextAdd(c1, c2, n, g)
tstart = time.time()
m1 = decrypt(c1, n, g, l, m)
m2 = decrypt(c2, n, g, l, m)
m_bar = decrypt(c_, n, g, l, m)
tend = time.time()
print("c_: " + str(c_))
print("m1: " + str(m1))
print("m2: " + str(m2))
print("m_bar: " + str(m_bar))
print("average time: " + str((tend - tstart) / 3))