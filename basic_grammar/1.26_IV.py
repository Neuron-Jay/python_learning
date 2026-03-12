#while循环是可以跟着条件的循环，有点像if和for的合体版
#以前面的最后一段代码为例：
list1 = ["How","are","you","bro"]
for i in range(len(list1)):
    print(list1[i])
#用while循环可以写成：
i=0
while i<len(list1): #while后面的条件可以直接是布尔值
    print(list1[i])
    i=i+1
    #这一步得出新的i值后就再次回到while后面进行条件检验，
    #如果依然符合条件就进入执行语句，继续输出新的i值，循环往复，直至条件不符合，就退出循环

#我们试着用while循环写一个可以求任意数量的任意数字的平均值的计算器
print("""This is an average calculator.
Please enter any number of any values.
When you need to calculate the average of all the numbers you have entered, input 0 and press Enter.""")

x = float(input("Please enter numbers: "))
num_list = [0]
num_list.append(x)
while x != 0:
    x = float(input("Please enter numbers: "))
    num_list.append(x)
#难免会有些调皮的用户只输入一个0（恼
if len(num_list)-2 == 0:
    print("Oh, you shouldn\'t just enter a single 0!")
else:
    print("The result is: "+ str(sum(num_list)/(len(num_list)-2))) #这里的-2，减去了最开始列表里的0元素和最后确认求值时用户输入的0
#虽然这个平均值计算器是我第一次独立构思出来的，但还是有美化的空间

