"""
    python练习
"""
# python 中缩进代表代码块，同一代码块中的缩进必须一致
if 3 > 0:
    print('ok')
    print('yes')
# python当中的变量不需要指定其类型
x = 3
y = 4
print(x + y)
# 可以在同一行中定义多个变量
a, b = 1, 2
print(a + b)

# print
print('hello world!')
# 逗号自动添加默认的分隔符：空格
print('hello', 'world!')
# 加号表示字符拼接
print('hello' + 'world!')
# 单词间用***分隔
print('hello', 'world', sep='***')
# *号表示重复50遍
print('#' * 50)
# 默认print会打印回车，end=''表示不要回车
print('how are you?', end='')
print('how are you?')
# 基本运算
print(5 / 2)  # 2.5
print(5 // 2)  # 2 丢弃余数保留商
print(5 % 2)  # 求余
print(5 > 3)  # true
print(5 < 3)  # false
print(20 > 10 > 5)  # python支持连续比较
print(20 > 10 and 10 > 5)  # 相当于上面
print(not 20 > 10)  # 取反
"""
input
"""
print("=" * 50)
# input用于获取键盘输入
number = input("请输入数字：")
print(number)
print(type(int(number)))  # 输入类型 int()将number转为int
print(int(number) + 10)  # 20
print(number + str(10))

username = input("please input:")
print('welcome', username)    # 字符之间默认以空格作为分割符
print('welcome '+username)
