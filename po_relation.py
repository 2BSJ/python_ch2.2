a = 6
print( 0 < a and a < 10)
print(0 < a < 10)

print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] < [1, 2, 0])

#error
#print([1, 3, 2] < (1, 2, 0))
print([1, 3, 2] < list((1, 2, 0)))

# 동질성 비교: == 동일성 비교: is
a = 10
b = 20
c = a
d = 10
print(a == b)
print(a is b)
print(a is c)
print(a == c)
print(a == d)
print(a is d)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)
print(l1 is l2)

# 논리의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'operator')
print('' and 'operator')
print('ok')

def f(msg=None):
    msg and print(msg)

f()
f('hello world')