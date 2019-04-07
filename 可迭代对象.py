from collections import Iterable

"""可迭代对象：可以直接作用于for循环的对象统称为可迭代对象（iterable），可以用isinstance()去判断一个对象是否是Iterable对象
可以直接作用于for的数据类型一般分为两种
1.集合数据类型，如list、tuple、dice、set、string
2.是generator，包括生成器和带yield的generator function

"""
print (isinstance([],Iterable))
print (isinstance((),Iterable))
print (isinstance({},Iterable))
print (isinstance("",Iterable))
print (isinstance((x for x in range(10)),Iterable))
print (isinstance(1,Iterable))

"""
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直达最后抛出一个错误表示无法继续返回下一个值

可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator)

可以使用isinstance()函数判断一个对象是否是Iterator对象

"""

list = (x for x in range(5))
print (next(list))

#转成iter对象
a = iter([1,2,3,4,5])
print (next(a))

