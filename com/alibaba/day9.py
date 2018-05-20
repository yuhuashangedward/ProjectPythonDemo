if 1 == 1:
    if 2 == 2:
        print("欢迎进入第一会所1")
        print("欢迎进入第一会所2")
    else:
        print("欢迎进入东京热")
else:
    print("欢迎进入一本道")

inp = input("请输入会员级别：")

if inp == "高级会员":
    print("美女")
elif inp == "白金会员":
    print("达摩")
elif inp == "铂金会员":
    print("一线小明星")
else:
    print("城管")
print("开始服务。。。")