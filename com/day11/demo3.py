# test = "alex"
# r = test.swapcase()
# print(r,len(r))

# 字母、数字、下划线
# a = "_3563"
# r1 = a.isidentifier()
# print(r1)

# test = "FJSFG"
# r1 = test.islower()
# print(r1)

# test = "#1"
# r1 = test.isdecimal()
# r2 = test.isdigit()
# r3 = test.isnumeric()
# print(r1,r2,r3)

# test = "werfj\tfhg"
# r = test.isprintable()
# print(r)
#
# test = "  skdhfjks"
# r = test.isspace()
# print(r)

# test = "Rskdh sjdkl dlk ld;k "
# r = test.istitle()
# print(r)
# r1 = test.title()
# print(r1)

# test = "你是份儿我是啥"
# print(test)
# t = ' '
# r1 = t.join(test)
# print(r1)

# test = "alex"
# r = test.ljust(20,"*")
# print(r)
# r1 = test.rjust(20, "@")
# print(r1)
# r3 = test.zfill(20)
# print(r3)

# test = " Ale x "
# r1 = test.islower()
# print(r1)
# r2 = test.lower()
# print(r2)

# r1 = test.isupper()
# print(r1)
# r2 = test.upper()
# print(r2)

# # 去除左右空白；换行 \t \n;指定内容
# test = " Ale x "
# r1 = test.lstrip()
# r2 = test.rstrip()
# r3 = test.strip()
# print(r1,r2,r3)

# test = "你是风儿我是沙"
# test1 = "去你妈的风河沙"
# m = str.maketrans(test,test1)
# v = "你是风儿我是沙，缠缠绵绵去你家"
# new_v = v.translate(m)
# print(new_v)

# test = "testsdjfg"
# r1 = test.partition('s')
# r2 = test.rpartition('s')
# r3 = test.split('s')
# r4 = test.rsplit('s',2)
#
# print(r1)
# print(r2)
# print(r3)

# test = "tes\nts\ndjfg"
# v = test.splitlines()
# print(v)

# test = "yheiufyhkhdf"
# r1 = test.startswith('y')
# r2 = test.endswith('k')
# print(r1,r2)

# test = "Alec"
# r = test.swapcase()
# print(r)
#
# test = "郑建文"
# for a in test:
#     continue
# print(a)

# 帮助创建连续的数字，通过设置步长来指定不连续
# v = range(0, 100,5)
# print(v)
#
# for item in v:
#     print(item)

# test = "郑建文有种冲我来"
#
# demo = input('>>>')
# if(test.__contains__(demo)):
#  #   for demo in test:
#     print(demo)
#     print(test.index(demo))
# else:
#     print("输入错误")

test = input(">>>")
print(test)
l = len(test)
print(l)

r = range(0, l)
for item in r:
    print(item, test[item])

str