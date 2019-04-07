
list = []
num = 0  #输入数字的数量
while num < 5:
    val = int(input())
    list.append(val)
    num += 1
print (list)
list.sort()
countnum = list.count(list[-1])
c = 0
while c < countnum:
    list.pop()
    c += 1
print (list[-1])


list = [1,2,3]
errornum = list.index(3)
list[errornum] = int(input('输入一个数字'))
print (list)

