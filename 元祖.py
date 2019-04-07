'''
元组(tuple)
本质：是一种有序集合

特点：
1.与列表非常相似
2.一旦初始化就不能修改
3.使用是小括号()
'''

#创建空的元祖
tuple = ()
print (tuple)
#创建带有元素的元祖
#元祖中的元素的类型可以不同
tuple1 = (1,2,3,"good",True)
print (tuple1)
#定义只有一个元素的元祖
tuple2 = (1,)    #如果不加逗号则为单个变量值
print (tuple2)
print (type(tuple2))


#元祖元素的访问
#格式：元组名[下标]
#下标从0开始
tuple3 = (1,2,3,4,[5,6,7])
print (tuple3[0])
tuple3[-1][0] = 500
print (tuple3)

#删除元组
tuple4 = (1,2,3)
del tuple4
print (tuple4)

t5 = (1,2,3)
t6 = (4,5,6)
t7 = t5 + t6
print (t7)
print (t5,t6)

#元组重复
t8 = (1,2,3)
print (t8 * 3)

#判断元素是否在元组中
t9 = (1,2,3)
print (4 in t9)

#元组的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到结束下标之前
t10 = (1,2,3,4,5,6,7,8,9)
print (t10[2:8])
print (t10[:8])
print (t10[2:])

#二维元组:元素为一维元组的元组
t11 = ((1,2,3),(4,5,6),(7,8,9))
print (t11[1][1])

#元组的方法
t12 = (1,2,3,4,5)
#len() 返回元组中元素的个数
print (len(t12))

#max() 返回元组中的最大值
#min() 返回元组中的最小值
#tuple() 将列表转成元组
list = [1,2,3]
t13 = tuple(list)
print (t13)

#元组的遍历
for i in (1,2,3,4,5)
    print (i)

print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print ("Value of x , y : ", x,y)



