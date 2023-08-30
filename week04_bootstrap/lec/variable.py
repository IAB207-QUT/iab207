#type conversion
print('Float to int conversion ', int(3.45))
print('String multiplication', 'hello ' * 4)
print('String conversion to int and multiplication ', int('3') * 4)

#Int variable change example
a = 10
print(id(a))
x = a
print(id(x))
a = 11
print(id(a))
print('Value of a ', a)
print('Value of x ', x)

#String variable change example
txt = "text"
t = txt.replace('e', 'eee')
print(t)

#String variable change example
p = 'hello'
q = p
p = p.replace('l', 'L')
print('Value of p ', p)
print('Value of q ', q)