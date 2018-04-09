import random

def QuickPow(a, b, MOD):
    ret = 1
    tmp = a%MOD
    while b>0:
        if (b&1):
            ret = (ret*tmp)%MOD
        tmp = (tmp*tmp)%MOD
        b >>= 1
    return ret

def Miller_Rabin(a, p): # a^(p-1) = 1 (mod p)
    p1 = p-1
    s2 = p1 & -p1 # fetch the last 1
    x = QuickPow(a, p1//s2, p)
    if x == 1 or x == p1:
        return True
    while s2>1:
        x = (x*x)%p
        if x == 1:
            return False
        if x == p1:
            return True
        s2 >>= 1
    return False

def IsPrime(p, k):
    if p == 2 or p == 3:
        return True
    if p < 2 or (p&1) == 0:
        return False
    for i in range(k):
        if not Miller_Rabin(random.randint(2, p-1), p):
            return False
    return True

n = int(input())
p = int(input())
for i in range(n):
    print('YES' if IsPrime(p, 1) else 'NO')

# http://www.cnblogs.com/Mathics/p/4028819.html
#代码强制被人喜欢，人家人爱，花见花开
