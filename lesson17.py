
# 序列！序列！

# 列表、元组和字符串的共同点
# -都可以通过索引得到每一个元素
# -默认索引值总是从0开始
# -可以通过分片的方法得到一个范围内的元素的集合
# -有很多共同的操作符（重复操作符、拼接操作符、成员关系操作符）

# 1.list()把一个可迭代对象转换为列表
# help(list)

# a = list()

# b = 'I love fishC.com'
# b = list(b)

# c = (1,1,2,3,5,8,13,21,34)
# c = list(c)


# 2.tulple()把一个可迭代对象转换为元组
# help(tulple)


# 3.str(obj)把obj对象转换为字符串


# 4.len(sub)
# len(a)
# len(b)


# 5.max() 返回序列或者参数集合中的最大值
# max(1,2,3,4,5)
# max(b)
# memebers = [1,2,3,1,2,4,5,-87,23,45]
# max(memebers)


# 6.min() 返回序列或者参数集合中的最小值
# min(memebers)

# chars = '1234567890'
# min(chars)

# tulple = (1,2,3,4,5,6,7,8,9,0)
# max(tulple)

# 作用的对象只能有一种数据类型

# memebers.append('a')
# memebers
# max(memebers)    --报错

# 实现原理：

# max = tulple[0]

# for each in tulple:
#     if each > max:
#     	max = each

# return max


# 7.sum(iterable[, start=0]) 返回序列iterable和可选参数start的总和

# tulple2 = (3.1,2.3,3.4)
# sum(tulple2)

# memebers.pop()   --去掉'a'

# sum(memebers)
# sum(memebers,8)


# 8.sorted()    作用同list.sort()
# sorted(memebers)

# 9.reversed()
# reversed(memebers)    返回一个迭代器对象
# list(reversed(memebers))

# 10.enumerate()     --枚举
# enumerate(memebers)
# list(enumerate(memebers))
# --每一个元素前加上索引


# 11.zip()    压缩
# a = [1,2,3,4,5,6,7]
# b = [2,3,6,8,0]
# zip(a,b)
# list(zip(a,b))        --成对打包，一个里面多的不算

