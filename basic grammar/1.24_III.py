#数据的比较
# == 用于判断两边的两个数据是否相等，相等输出布尔值True，否则输出False
print(3==3)
print(3==4)
# != 用于判断两个数据是否不相等，和 == 是反过来的
print(3!=3)
print(3!=4)
#依据数学知识，比较运算符还有：>, >=, <, <=.
print(3<6<5)
print(3<6<=6)
#还可以进行连续比较运算

#比较运算可以作为if条件语句的条件
#if后面的条件得是被赋值为布尔值的变量

#来让刚刚的BMI计算器具备评价用户是否健康的功能
#您的身高（米）
user_height = input("Please enter your height in meters: ")
#您的体重（千克）
user_weight = input("Please enter your weight in kg: ")
#您的BMI指数为
BMI = float(float(user_weight)/(float(user_height))**2)
#因为后面的条件语句中要拿BMI和其他两个浮点数作比较，所以这里就把BMI赋值为浮点数，而不是像上一个BMI计算器里一样赋值为字符串

if 18.5<= BMI < 24.0 :   #if函数后面要跟一个冒号，别忘了。下面的else也是
    print("Oh, you are pretty healthy!")
#if跟着的执行语句要空四个空格，但专业叫法是”缩进四个空格“。为什么要叫“缩进”这个意思相反的词呢（疑惑

#如果条件不符合if里得到条件时你希望能执行其他语句，还可以用else语句
else :
    print("Oh, you need to pay more attention to your body!")