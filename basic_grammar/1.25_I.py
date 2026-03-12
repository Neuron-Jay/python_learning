#逻辑运算符 可以用来表示各个条件之间的关系，有and, or, not

print(5>3 and 5<6)
#对于and运算符，只有每一个条件都是True，输出的布尔值才会是True，否则是False
print(5>3 and 5<4)

print(5>3 or 5<4)
#对于or运算符，只要有一个条件是True，输出的就是True。只有没一个是True，才会输出False
print(5>3 or 5<6)
print(5>6 or 5<4)

#not运算符更像是一个“反义前缀”，在一个条件前面加上not就可以输出与该条件所对应布尔值相反的布尔值
#因为：not的运算优先级是最高的
print(not 5<3  and 5>4)
print(not 5<3  or 5<4)

#这三种逻辑运算符貌似可以让if后面的条件更复杂，从而可以让整体的代码更简洁，逻辑更清晰