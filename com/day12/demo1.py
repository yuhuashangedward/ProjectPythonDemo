# a = "abc"
# b = "abc" + "d"
# print(id(a))
# print(id(b))

a = (123, "abc", [(1233, 456)])
print(a[2][0][0])
# a[2][0][0] = 1111
for item in a:
    print(item)

print(id(a))