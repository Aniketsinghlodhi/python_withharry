
# Assignment Operators
a = 34
b = 2
c = a
c += b
print("Assignment += :", c)          # Assignment +=
# output: Assignment += : 36
c -= b
print("Assignment -= :", c)          # Assignment -=
# output: Assignment -= : 34

c *= b
print("Assignment *= :", c)          # Assignment *=
# output: Assignment *= : 68
c /= b
print("Assignment /= :", c)          # Assignment /=
# output: Assignment /= : 34.0
c %= b
print("Assignment %= :", c)          # Assignment %=
#
c **= b
print("Assignment **= :", c)         # Assignment **=

c //= b     
print("Assignment //= :", c)         # Assignment //=
# output: Assignment //= : 8.0 0 