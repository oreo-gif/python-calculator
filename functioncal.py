def add(x , y):
    z = x + y
    return z
def sub(x , y):
    a = x - y
    return a
def div(x , y):
    b = x/y
    return b
m = input("enter 1st number  :")
n = input("enter 2nd number  :")
x = float(m)
y = float(n)
s = input("enter operator  :")
if s == '+':
    u = add( x , y)
    print(u)
if s == '-':
    v = sub(x ,y)
    print(v)
if s == '/':
    g = div(x, y)
    print(g)
    quit()
