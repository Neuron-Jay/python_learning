#变量名中不能有空格，不能用数字开头，也不能用引号引起来，只能有下划线（否则就是字符串）
#不要拿函数名明明变量
genius = "Jay"
#等号用于给变量赋值。上面给变量genius赋的值是字符串"Jay"
print(genius + " is the Lord.")
#变量的赋值先于变量的使用，否则会报错
God = genius
print(God + " is the world.")
#用另一个变量给原有变量赋值后，原有的变量就可以再拿来赋新的值
genius = "Jay Hu"
print(genius + " is our leader.")
#在有变量的时候，可以用print打印出当前某一变量的值
print("当前genius的值：" + genius)
print("当前God的值：" + God)