"""
使用键-值(key-value)存储，具有极快的查找速度
字典是无序的

key的特性：
1.字典中的key必须唯一
2.key必须是不可变的对象
3.字符串、整数等都是不可变的，可以作为key
4.list是可变的，不能作为key

"""

#元素的访问
#获取元素的值：字典名[key] 返回key的value，没有就报错
#字典名.get(key) 返回key的值，没有返回none
#添加 字典名[newkey] = value
#修改 字典名[key] = newvalue 对已经存在的key进行赋值其实就是修改值
#删除 字典名.pop(key)
#遍历
dict1 = {"A":"aaa","B":"bbb","C":"ccc"}
for key in dict1:
    print (key,dict1[key])  #遍历dict1中所有的key并输出key以及key的值

print (dict1.values())
for value in dict1.values():
    print (value)     #遍历dict1中所有的值并输出

print (dict1.items())
for k,v in dict1.items():
    print (k,v)    #遍历dict1中所有的key-value

for i,v2 in enumerate(dict1):
    print (i,v2)

"""和list的比较
1.查找和插入的速度极快，不会随着key-value的增加而变慢
2.需要占用大量的内存，内存浪费多
"""
"""
list查找和插入的速度会随着数据量的增多而减慢
占用空间小，浪费内存少
"""


dict1 = {"A":"aaa","B":"bbb","C":"ccc"}
dict2 = {"D":"aaa","E":"bbb","F":"ccc"}
dict1.update(dict2)
print (dict1)

name1 = {'name':'xx','age':18}
name2 = {'name':'yyy','age':17}
totalname = [name1,name2]
for new_name in totalname[1:]:
    if new_name['name'] == 'yyy':
        new_name['name'] = 'zzz'
print (totalname)