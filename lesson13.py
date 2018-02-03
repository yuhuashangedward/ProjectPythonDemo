
# 列表的一些常用操作符

# 比较操作符
# 逻辑操作符
# 连接操作符
# 重复操作符
# 成员关系操作符

# 单个元素列表比较大小
# list1=[123]
# list2=[456]
# list1>list2

# 多个元素列表比较大小（仅比较第0个）
# list1=[123,456]
# list2=[456,123]
# list1>list2

# 逻辑操作符
# list3=[123,456]
# (list1<list2) and (list1==list3)

# 列表的组合
# list4=list1+list2

# 重复操作符（*）
# list3*3
# list3*=5

# 成员关系操作符(in,not in)
# 123 in list1
# '太平洋' not in list1

# 列表的二维形式
# list5=[123,['小甲鱼','牡丹']，456]

# '小甲鱼' in list5
# False

# 适用于一层关系
# '小甲鱼' in list5[1]

# list5[1][1]



# 列表的小伙伴们：
# 1.获取方式：（内置方法）
# dir(list)
# count   (出现的次数)
# index   (参数在列表中位置)
# reverse (列表翻转)
# sort    (对列表中数据进行排序，默认升序  三个参数)


# list3.count(123)
# list3.index(123)
# 0
# list3.index(123,4,7)
# 4
# list3.reverse()
# list6=[4,2,6,8,2,4,56]
# list6.sort()

# sort(fun,key,reverse) reverse默认为false
# list6.sort(reverse=True)

# 作业要点：
# 使用分片创建列表的“拷贝”

# list7=list6[:]
# list8=list6

# 两者区别通过reverse演示
# list6.sort()

# list8==list6   True
# list7==list6   False

# 分片“拷贝”概念的补充
# list11       [1,3,2,8,7,9]      list13

# list12       [1,3,2,8,7,9]

# 分片“拷贝”：list11==》list12的过程是真正重新建立一个一模一样的列表
# “赋值”形式：list11==》list13的过程并不创建列表，只是多了一个指向原列表的标签，随原列表改变而变

