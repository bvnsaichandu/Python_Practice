l = [10,20,'Bharath', -10,30,5]
print(l)
print(l[3])
print(l[5])
print(l*2)
print(len(l))

l.append(40)
print(l)

l.remove('Bharath')
print(l)

del(l[3])
print(l)

print(max(l))
print(min(l))

l.insert(3,99)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

thislist = ["banana", "apple", "cherry"]
print(thislist)

'''thislist = ["apple", "banana", " cherry"]
           for x in thislist
               print(x)'''

'''thislist = ["banana", "apple", "cherry"]
if "apple" in thislist
    print("Yes") '''



thislist = ["banana", "apple", "cherry"]
mylist = thislist.copy()
print(mylist)

