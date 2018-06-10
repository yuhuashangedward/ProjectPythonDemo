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

# test = input('请输入内容：')
# c1 = 0
# c2 = 0
# val = input(">>>")
# for item in val:
#     if item.isalnum():
#         c1 += 1
#         if item.isalpha():
#             c2 += 1
# print("数字个数:" + str(c1 - c2))
# print("字母个数：" + str(c2))

# input("请输入名字：")
# param1 = input('>>>')
# input("请输入地点：")
# param2 = input('>>>')
# input("请输入爱好：")
# param3 = input('>>>')
# template = "敬爱可亲的{0}，最喜欢在{1}，{2}"
# demo = template.format(param1, param2, param3)
# print(demo)

def check_code():
    import random
    checkcode = ''
    for i in range(4):
        current = random.randrange(0, 4)
        if current != i:
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode += str(temp)
    return checkcode


code = check_code()
print(code)

count = 0

while(True):
    if (count > 5 or 5 - count == 0):
        print("超过次数限制")
        break
    input('用户输入验证码')
    customer_code = input('>>>')
    user_code = customer_code.lower()
    real_code = check_code = code.lower()
    count = count + 1

    if(real_code == user_code):
        print("恭喜你，验证码输入正确！")
        break
    else:
        print("验证码错误，您还有"+str(5-count)+"次机会，请重新输入：")

