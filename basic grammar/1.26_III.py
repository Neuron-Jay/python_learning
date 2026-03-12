#for循环可以按照顺序对一些数据里的一个个元素依次做同一件事...
#用人话没法讲清楚，还是用机器话吧

#先来个列表，比如BMI的汇总表，
BMI_list = [17.3,21.4,24.6,22.3,25.8,19.6,30.1,26.3,23.5,22,3]
#for后面的本质上也是对一个变量的命名，只不过这里的变量是拿来迭代的，不是拿来赋值的
for BMI in BMI_list: #和if一样，这里得跟一个冒号
    #瘦了的
    if BMI < 18.5:
        print("Thin")
    #正常的
    elif 18.5<=BMI <24.0:
        print("Healthy")
    #胖了的
    else:
        print("Fat")
    #从第9行到第16行都被缩进了，就是for循环对列表里每个变量依次执行的任务语句。在这个例子里做的是判断符合哪一条件。

#如果想要知道每个BMI对应的人是谁，那就得把操作对象换成字典了。
BMI_dict = {"A":17.3,
            "B":21.4,
            "C":24.6,
            "D":22.3,
            "E":25.8,
            "F":23.5,}
for name,BMI in BMI_dict.items(): #既然想要知道BMI对应的名字，那就得调用所有键值对
    #为什么for后面会跟着name,BMI两个变量呢？
    #因为我们对字典做的是.item()方法，输出的键值对会以元组的形式呈现，
    #而每个元组的第一个元素(A,B,C...)会被赋值为name，第二个元素(每个人的BMI)会被赋值为BMI

    if BMI < 18.5:
        print(name+":")
        print("Thin")
    elif 18.5<=BMI <24.0:
        print(name+":")
        print("Healthy")
    else:
        print(name+":")
        print("Fat")

#如何让你的好兄弟珍藏的美女列表“消失”？
girls_list = ["Lisa","Ashley","Jessica","Lucy","Judy"]
for girl_name in girls_list:
    print(len(girl_name))

#算了，还是干点正经事
total = 0
for num in range(1,101,2):
#等差数列求和，range代表整数序列，
#其中range(1,101,2)中，1和101指的是计数的范围是1到101（不包含101），后面的2指的是每次计数跨几个数字，
#当range起始数字为0时，0不需要打出来；跨1个数字计数时，不需要把1打出来
    total = total + num #其实这一步才能真正体现for的“迭代”的功能，比上面的例子更加能够体现。
                        #因为这一步在不断地把旧的total变成新的total。
                        #怎么变的？就是按照序列里的顺序把一个个元素对应的num用for不停地加到total上去
    print(total)
    #计算结果应该是数列2n-1从n=1到n=50的相加结果，也就是2500

#至此应该可以发现，for循环中的in后面，应该是一个包含多个元素的数据，是一个“能被逐个拿出元素”的东西。

#为了能更好的理解range和for
list1 = ["How","are","you","bro"]
for i in range(len(list1)):
    #len(list1)的结果为4，range(4)的结果为range(0,4)
    #i对应的就是0,1,2,3
    print(list1[i]) #索引list1[i]就是list1中的每个元素，也就是每个字符串
