a,b = eval(input("请输入两个数："))
x = []
y = []
for m in range(1,1000):
    if a % m == 0:
        x.append(m)
    if b % m == 0:
        y.append(m)
if x[-2] in y:
    print (x[-2])
elif y[-2] in x:
    print (y[-2])
else:
    print ('没有公约数')


#len(str)
#返回字符串的长度（字符个数）
#ord()转换字符为ASCII码
#chr()转换ASCII码为字符
#字符串比较大小
#从第一个字符开始比较，谁的ASCII码值大谁就大，如果相等会比较下一个字符的ASCII码
#值大小，那么谁的值大谁就大
print ("bazzzz" > "ba")