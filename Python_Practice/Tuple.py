tp1 = (40, 50, 40, "xyz")
print(tp1)
print(type(tp1))

print(tp1[1])
print(tp1*3)
print(tp1.count(40))
print(tp1.index(50))

# Convert to List to Tuple

l = [40,50,60]
print(type(l))
print(l)
tp2 = tuple(l)
print(type(tp2))
print(tp2)

print(len(tp2))