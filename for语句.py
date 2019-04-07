for 变量名 in 集合:
    语句


逻辑：按顺序取"集合"中的每个元素赋值给"变量"，再执行语句，如此循环往复，直到取完"集合"
中的元素截止


range([start,]end[,step])函数    列表生成器
start为起点，默认为0，end为终点，step为步长，默认为1
功能：生成数列

枚举器
for index,m in enumerate[1,2,3,4,5] #index,m = 下标，元素
    print (index,m)

sum = 0
for n in range(1,101):
    sum += n
print (sum)