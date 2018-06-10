'''test = "李杰"
for item in test:
    print(item)
'''

# test = 5
# bit_len = test.bit_length()
# print(bit_len)
#
# a = "alex"
# b = a.capitalize()
# print(a)
# print(b)

# name = " aleX"
# a = name.strip()
# print(a, len(a))

# name = " aleX"
# a = name.startswith('al')
# print(a)

# name = " aleX"
# a = name.endswith('X')
# print(a)

# name = " aleX"
# a = name.replace('l', 'p')
# print(a)

# name = " aleX"
# # 不包含被切割元素, 得到list[集合]
# a = name.split('l')
# # 包含切割元素, 得到tuple[元组]
# b = name.partition('l')
# print(a, type(a))
# print(b, type(b))

# name = " aleX"
# a = name.upper()
# print(a)

# name = " aleX"
# a = name.lower()
# print(a)

# name = " aleX"
# for item in name:
#
#     print(item)

# name = " aleX"
# a = name.index('a')
# print(a)

# name = " aleX"
# a = name[1]
# print(a)

# name = " aleX"
# a = name[0:3]
# print(a)

# name = " aleX"
# length = len(name)
# print(length)
# a = name[length-2:length]
# print(a)

# name = " aleX"
# a = name.index('e')
# print(a)

# name = " aleX"
# a = name[0:-1]
# print(a)

# name = " aleX"
# for i in name:
#     print(i)

# li =  ['alex', 'eric', 'rain']
# t = '_'
# r = t.join(li)
# print(r)

# test = "Hello World!"
# r = range(0, 10, 2)
# for i in r:
#     print(i, type(r))
# print(r)



# name = " aleX"
# # print(name[])
# for i in range(len(name)):
#     print(name[i])



# content = input('请输入内容：')
# print(content)
# num = content.split("+")
# sum = 0
# for i in range(len(num)):
#     sum = sum + int(num[i])
# print(sum)

# content = input('请输入内容')
# print(content)
# num1, num2 = content.split('+')
# num1 = int(num1)
# num2 = int(num2)
# sum = num1 + num2
# print(sum)

test = input('请输入内容：')
c1 = 0
c2 = 0
val = input(">>>")
for item in val:
    if item.isalnum():
        c1 += 1
        if item.isalpha():
            c2 += 1
print("数字个数:" + str(c1 - c2))
print("字母个数：" + str(c2))
