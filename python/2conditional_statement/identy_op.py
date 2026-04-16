a=10
b=20
c=a
d=10
e=10
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
print(a is b)
print(a is c)
print(a is d)
print(a is not e)


c = [1, 2, 3]
print("a is b =", a is b)       # True (same object)
print("a is c =", a is c)       # False (different object)
print("a == c =", a == c)       # True (same value)
print("a is not c =", a is not c)