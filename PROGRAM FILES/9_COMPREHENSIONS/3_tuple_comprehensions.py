x = tuple(x for x in range(10))
print(x)

x = tuple(x for x in range(1, 11) if x%2==0)
print(x)

x = tuple(x for x in range(1, 11) if x%2==1)
print(x)

x = tuple(x*x for x in range(10))
print(x)

