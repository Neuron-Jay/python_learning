print("Hello"+" World"+"!")
#单双引号转义
#外为单引号，内部的双引号里的World会被识别为字符串内容
print('Hello "World"')
#在引号前加\，可以让引号被识别为字符串，\为转义符
print("Come on, Let\'s go!")
#在字符串中用\n可以让字符串内容换行
print("Hello!\nI\'m Jay!")
#用三个引号也可以实现换行，这样python会把字符串中换行的内容识别为换行，而不会识别为中断并报错
print('''O Romeo, Romeo! Wherefore art thou Romeo?
Deny thy father and refuse thy name;
Or, if thou wilt not be but sworn my love,
And I\'ll not longer be a Capulet.
----Romeo and Juliet''')