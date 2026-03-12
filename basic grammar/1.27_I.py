#假如我们要对字符串做批量化的同样处理，我们可以使用字符串格式化，这会比粗暴地直接使用for循环简洁一些
#以前面的BMI评估器为例，如果我们要把结果发送给这些用户
BMI_dict = {"A":17.3,
            "B":21.4,
            "C":24.6,
            "D":22.3,
            "E":25.8,
            "F":23.5,}
for name,BMI in BMI_dict.items():
#虽然可以直接打 print("Hello, " + name + ", your BMI is " + str(BMI))
#但如果我不喜欢print里面的东西被加号隔开呢？
    print("Hello, {0}！Your BMI is {1}.".format(name,BMI)) #使用format的时候，不需要把浮点数BMI转化成字符串
#其中，0的意思是指format里面的第一个元素，也就是变量name；1就是第二个元素，以此类推。

#...说实话感觉这个没什么用