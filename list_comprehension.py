# list comprehension

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

a = [1, 2, 3, 4, 5]
b = [i**2 for i in a]

print(x)
print(y)

a = [1, 2, 3, 4, 5]
b = [i**2 for i in a]
c = [i for i in a if i%2==1]

print(x)
print(y)
print(c)
