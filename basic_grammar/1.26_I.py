#下面这个叫做列表，用[]框住列表里的元素
shopping_list = ["apple" , "orange" , "banana"]
shopping_list.append("carrot")
#这个.append叫做方法名，具体使用方式为：对象.方法名(...)
#由append也可以看出，列表是可以变化的，是直接把原来的列表的内容改变，而不是改变出一个新列表。
shopping_list.remove("apple")
print(shopping_list)
#列表里还可以放其他种类的数据
shopping_list.append(11) #pycharm在11下面划了黄线，貌似是不太建议我在列表里放不同种类的数据（尴尬
print(shopping_list)
#与字符串相似，列表也可以用len函数和索引[x]的方式，用来求出列表中元素的数量以及某个位置的元素
print(len(shopping_list))
print(shopping_list[0])
#如果你想改变列表中的某个元素，还可以直接用索引的方式对该元素赋新值就行
shopping_list[0] = "grape"
print(shopping_list)

#对于列表，还有一些函数可以对其进行处理
num_list = [3,2,5,11,7,13]
print(max(num_list))
print(min(num_list))
print(sum(num_list)) #求和
print(sorted(num_list)) #排序，默认按照从小到大
#但这几个函数目前看来好像只对int和float有用，不信的话...
#print(sorted(shopping_list))

#与列表相比，有个很像的东西叫做元组，就是用()框住各个元素
All_Time_First_Team = ("Magic_Johnson","Michael_Jordan","Lebron_James","Tim_Duncan","Shaquille_O'Neal")
print(All_Time_First_Team)
#和列表的区别在于，元组是不可变的.