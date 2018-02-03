
# 元组：戴上了枷锁的列表

# 1.创建和访问一个元组
# tuple=(1,2,3,4,5)

# 访问元组元素
# tuple[1:]
# tuple[:5]
# tuple[1]=8  报错，不能直接赋值

# 关键标志是逗号，而非括号
# tuple=(6,) 
# type(tuple)   tuple
# tuple=(8)
# type(tuple)   int

# 空元组：
# tuple=()

# tuple=4,
# 8*8
# 8*(8,)


# 2.更新和删除一个元组(切片方式实现)
# temp=('太平洋','印度洋','北冰洋')
# temp=temp[:2]+('大西洋')+temp[2:]
# temp

# del temp            (python的回收机制)


# 3.元组相关的操作符
# 拼接、逻辑、重复操作符、关系操作符
