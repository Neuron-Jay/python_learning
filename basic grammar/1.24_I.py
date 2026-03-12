#str：字符串
#len函数可以输出字符串的长度，其中空格也算一个长度
print(len("bighyj"))
#在字符串后面加入[x]（x为从0开始的整数）可以对字符串做索引，显示该字符串种第x个字符。
#值得注意的是，第一个字符在索引中对应的数为0
print("bighyj"[0])
print("bighyj"[1])
print("bighyj"[2])
print("bighyj"[3])
print("bighyj"[4])
print("bighyj"[5])

# 6 -32 这些为整数 int
# 6.0 4.04 这些为浮点数 float

#布尔类型，只有True和False两种数据
#空值类型，只有None这一种，表示什么都没有
#注意，这两种的首字母都要大写
a = True
b = False
print(a)
print(b)
c = None
print(c)

#如果想要查看某一数据的数据类型，可以调用type函数
print(type(c))
print(type(a))
print(type(1.414))