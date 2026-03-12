#让我们针对前面的BMI计算评估器进行一些改良，让代码更好看一些
"""
先把原来的代码展示一下
user_height = input("Please enter your height in meters: ")
user_weight = input("Please enter your weight in kg: ")
BMI = float(float(user_weight)/(float(user_height))**2)
if 18.5<= BMI <= 24.0 :
    print("Oh, you are pretty healthy!")
else :
    print("Oh, you need to pay more attention to your body!")
"""
#主要的改进部分，为4-6行的对各个变量的赋值工作上
user_height = float(input("Please enter your height in meters: "))
user_weight = float(input("Please enter your weight in kg: "))
#在给变量赋值的时候就直接把它变为浮点数

BMI = user_weight / (user_height ** 2)
#因为两个浮点数相除的计算结果就已经是浮点数了，所以就不需要再用一个float赋值为浮点数
print ("Your BMI is: "+ str(BMI))

if 18.5<= BMI < 24.0 :
    print("Oh, you are pretty healthy!")

#如果if后面的条件不满足，则可以用elif来进行下一个条件的判断。
#如果这个elif的条件还不满足，就进入下一个elif的条件判断，直到else.
#你可以用很多个elif，但是python只会执行第一个符合条件的执行语句，后面的elif的条件哪怕也是复合的，也不会执行它后面的语句。
elif BMI < 18.5 :
    print("Oh, you must be afraid of wind.")
    print("Why? Because You \'ll be BLOWN AWAY!")
#如果这个第二个print执行语句没有缩进，那就会报错。但是报错的会是else那一行。为什么呢？
#因为如果你没有缩进，那么if函数就已经被这个print结束了，后面的else就脱离if单独存在了，而这是不被允许的。

else : #BMI >= 24
    print("Oh, you should stay away from McDonald and KFC!")