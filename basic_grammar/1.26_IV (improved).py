#对于前面的平均值计算器，在保留我原有思路的前提下，可以美化成以下形式：
print("""This is an average calculator.
Please enter any number of any values.
When you need to calculate the average of all the numbers you have entered, input 0 and press Enter.
""")

num_list = []  # 真正的数据容器：只存“有效数字”

while True:
    x = float(input("Please enter numbers: "))

    if x == 0:
        break  # 一旦输入 0，立刻退出循环

    num_list.append(x)

# 处理特殊情况：用户啥都没输入
if len(num_list) == 0:
    print("Oh, you shouldn’t just enter a single 0!")
else:
    average = sum(num_list) / len(num_list)
    print("The result is: " + str(average))