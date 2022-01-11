"""
列表list
"""
alist = [10, 20, 30, 'bob', 'alice', [1, 2, 3]]  # 列表中可以包含各种数据
print(len(alist))
print(alist[-1][1])
print(alist[-2][2])  # 列表倒数第2项是字符串，再取出字符下标为2的字符
print(alist[1:5])
alist[-1] = 100  # 修改最后一项
print(alist)
alist.append(200)  # 追加
print(alist)

