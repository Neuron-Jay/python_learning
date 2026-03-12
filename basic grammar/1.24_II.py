#input函数可以让用户自己输入一些数据
user_age = input("Please enter your age: ")
#当然，input函数的计算结果数据类型是字符串，这一点得注意。
#需要的话可以用类型转换函数，比如str, int，直接对应各种数据类型的名称
print("So next year you will be " + str(int(user_age)+1) + " years old, right?")

#来试试用用这个方法来计算BMI
#您的身高（米）
user_height = input("Please enter your height in meters: ")
#您的体重（千克）
user_weight = input("Please enter your weight in kg: ")
#来看看你的BMI
print("Your BMI is: " + str(float(user_weight)/(float(user_height))**2) + ".")