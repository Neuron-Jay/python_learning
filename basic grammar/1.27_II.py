#我们可以用def来定义自己的函数，这样就可以把某一串代码整合为一个函数名，调用更方便，代码也更简洁
def bmi(height,weight):
    # BMI的计算公式
    user_bmi = weight/(height**2)
    print("Your BMI is {0}.".format(user_bmi)) #pycharm貌似建议函数名和变量都用小写字母
    if user_bmi < 18.5:
        print("THIN")
    elif 18.5<= user_bmi <24.0:
        print("NORMAL")
    else:
        print("FAT")
    return user_bmi #这一步是给整个函数返回了一个值，
                    #这使函数在被调用后不但会被执行函数中的语句，而且使得被调用的函数可以作为一个值
                    #在这个例子里，就是让bmi(,)函数不但可以执行计算语句，还可以代表user_bmi这个计算结果


result_1 = bmi(1.75,65)
result_2 = bmi(1.95,65)
result_3 = bmi(1.55,65)
print(result_1) #如果你前面没有return，那这里打印出来的是None，因为函数bmi(,)没有返回出任何值


