"""
字符串
"""
b = 'hello, world!'
print(len(b))
print(b[0:2])  # 从右向左取0到1，起始下标包含结束下标不包含
print(b[-4:-1])  # 从左向右取rld
####
print(b[2:])  # 从下标为2取到结尾
print(b[:2])  # 从开头取到2之前
print(b[:])  # 取全部
a = '123456'
print(a[::2])  # 步长为2，隔1取 135
print(a[1::2])  # 从1开始步长为2，隔1取 246
print(a[::-1])  # 步长为负，自右向左取 654321
# 常用方法,in
print('124' in a)   # false
print('124' not in a)   # true
print('12' in a)   # true

