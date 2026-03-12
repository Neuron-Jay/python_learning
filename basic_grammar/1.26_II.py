#字典可以储存一个数据（键）和另一个数据（值）的对应关系，这两个数据的组合为一个键值对，用{}把各个键值对框起来
users_age = {"jay":19,
             "Neo":24,
             "V":31}
print(users_age)#你会发现，尽管你输入字典键值对的时候是分行的，但最后打印出来是不换行的

#每个键和值之间用冒号连接，每个键值对之间用逗号分隔
#调用字典中某个键对应的值，就在字典名后面用方括号，里面输入想查询的键
print(users_age["jay"])
#但好像不能用值来反过来查键
#print(users_age[19])

#值得一提的是，字典是可变的，但字典中的键必须是是不可变的，也就是说键不能是列表
#所以如果需要，前面提到的元组就可以派上用场，用元组作为键
#不过给字典加新键值对的方式与列表不一样
#users_age.append("Sue":17) NO
users_age["Sue"] = 17
#实际上，对于字典的操作方法有以下三种
print(users_age.keys()) #.key()返回所有键
print(users_age.values()) #.values()返回所有值
print(users_age.items()) #.items()返回所有键值对

#用in可以来判断一个键是否存在于字典里，会输出对应的布尔值
print("jay" in users_age)
print("jayson" in users_age)
#想要删除某个键值对，那就用del
del users_age["V"]
#有没有发现？字典的直接操作很多是针对键，而不是键值对，这也是为什么它叫做“字典”

#再与input与条件结合一下，字典就可以拿给别人用了
#用户输入想要查询的人的名字
Q = input("Whose age do you want to know?")

if Q in users_age:
    print(users_age[Q])
#没这个人的话
else:
    print("###ERROR###")

'''为什么我们要学习这些呢？'''
# 学到NumPy和Pandas会发现，有很多语法组成部分，尤其是很多参数的本质，就是列表或者字典。
# 如果知道了这一点，就可以很好地理解为什么代码要这么写，而不会觉得每种方法都是用自己单独的一种语法规则。