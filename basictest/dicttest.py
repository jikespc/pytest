"""
 字典key-value dict 映射类型
"""
adict = dict(name='bob', age=23)  # 映射 {'name' : 'bob','age' : 23}
print(adict)
print('bob' in adict)  # false
print('name' in adict)  # true
adict['email'] = 'bob@tedu.cn'  # 字典中没有key，则添加新项目
print(adict)
adict['age'] = 33  # 字典中已有key，修改对应的value
print(adict)
