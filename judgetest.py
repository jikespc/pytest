"""
条件判断 if,三目运算符
"""
import random

if 3 > 0:
    print('yes')
    print('ok')

if 10 in [10, 20, 30]:
    print('ok')

if -0.0:
    print('yes')  # 任何值为0的数字都是false

if [1, 2]:
    print('yes')  # 非空对象都是true

if ' ':
    print('yes')  # 空格字符也是字符，条件为true
# 三目运算符
a = 10
b = 20
if a > b:
    smaller = b
else:
    smaller = a
print(smaller)

s = a if a < b else b  # 等价于上面的if-else
print(s)
print('*' * 50)
# 判断练习：用户名和密码是否正确
username = input('username: ')
# 导入getpass模块pc中不能使用
# password = getpass.getpass('password: ')
password = input('password: ')
if username == 'bob' and password == '123456':
    print('login successful')
else:
    print('login incorrect')

# 猜数知道猜对
# num = random.randint(1, 10)
# def test(c):
#     answer = int(input('number= '))
#     if answer > num:
#         print('大了')
#         test(c)
#     elif answer == num:
#         print('猜对了')
#     else:
#         print('猜小了')
#         test(c)
# test(num)

# 猜数直到猜对
num = random.randint(1, 10)
runing = True
while runing:
    answer = int(input('number: '))
    if answer > num:
        print('大了')
    elif answer < num:
        print('小了')
    else:
        print('猜对了')
        runing = False
