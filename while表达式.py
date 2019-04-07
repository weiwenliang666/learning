"""
while 表达式：
    语句
逻辑：当程序执行到while语句时，首先计算表达式的值，如果“表达式”的值为假，那么结束\n
整个while语句。如果“表达式”的值为真，则执行“语句”，并在执行完“语句”后重复计算表达式\n
的值，直到“表达式”的值为假，结束while循环。
"""

num = 100
while num < 1000:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if num == a**3 + b**3 + c**3:
        print (num)
    num += 1



num = int(input())
if num ==2:
    print("是质数")
index = 2
while index < num - 1
    if num % index == 0:
        print ("不是质数")
    index += 1
if index == num:
    print("是质数")

#嵌套最好不要超过3层


