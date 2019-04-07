if True:
    print ('answer')
    print ('True')
else:
    print ('answer')
  print ('False')   #缩进不一致，会导致运行错误

total = item_1 + \
        item_2 + \
        item_3

total = ['item_1','item_2'
         'item_3','item_4']

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

x = 'a'
y = 'b'
#换行输出
print (x)
print (y)

print ('----------')
#不换行输出
print (x,end = " ")
print (y,end = " ")
print ()
print (x,y)

name = input()  #用户输入内容至()内


num = 10
str1 = 'hello'
f = 10.1267
#%d整数类型 %s 字符串类型  %f 浮点数
#            占位符  按顺序 浮点数类型小数几位
print ('num = %d,str1 = %s,f = %.3f' %(num,str1,f))


#\n换行   \t制表符   \\表示\      \'表示'
print ('num = %d\nstr1 = %s,f = %.3f' %(num,str1,f))

print ('tom is a 'good' man')
print ("tom is a 'good' man")
print ('tom is a "good" man')


#eval(str)  功能：将字符串str当成有效的表达式来求值并返回计算结果
numb2 = eval('123')
print (numb2)
numb2 = eval('12+3')
print (numb2)
numb2 = eval('12-3')
print (numb2)
#len(str)
#返回字符串的长度（字符个数）

#str.lower()转换字符串中的大写字母为小写字母
#str.upper()转换字符串中的小写字母为大写字母
#str.swapcase()转换字符串中的小写字母为大写字母，转换字符串中的大写字母为小写字母
#str.captalize()字符串的首个字母大写
#str.title()每个单词的首字母大写

#center(width,fillchar)返回一个指定宽度的居中字符串,fillchar为填充的字符串
#默认是空格填充
str2 = "A is a nice man"
print (str2.center(20,"*"))
#**A is a nice man***

#ljust(width[,fillcha])
#返回一个指定宽度的左对齐字符串，fillchar为填充字符，默认空格填充
print (str2.ljust(40,"$"))
#A is a nice man$$$$$$$$$$$$$$$$$$$$$$$$$

#rjust(width[,fillcha])
#返回一个指定宽度的右对齐字符串，fillchar为填充字符，默认空格填充
print (str2.rjust(40))
#                         A is a nice man

#zfill(width)
#返回一个长度为width的字符串，原字符串右对齐，前面填充0
print (str2.zfill(40))
#0000000000000000000000000A is a nice man

#.count(sub[,start][,end])
#返回字符串中sub出现的次数，可以指定一个范围，默认从头到尾
str3 = "liangge is a very very good man"
print (str3.count("very",15,len(str3)))
#1

#find(str[,start][,end])
#检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，得到的是
# 第一次出现的开始下标，没有返回-1
str4 = "liangge is a very very good man"
print (str4.find("very"))
#13

#rfind(str[,start][,end])
str5 = "liangge is a very very good man"
print (str5.rfind("very"))
#18

#index(str,start=0,end=len(str))
#跟find()一样，只不过如果str不存在的时候会报错

#rindex()

#lstrip()截掉字符串左侧的字符，默认为空格
str6 = "@@@@@@@@@@@@@liangge is a very very good man"
print (str6.lstrip("@"))
#liangge is a very very good man

#rstrip()截掉字符串左侧的字符，默认为空格

#ord()转换字符为ASCII码
#chr()转换ASCII码为字符

#字符串比较大小
#从第一个字符开始比较，谁的ASCII码值大谁就大，如果相等会比较下一个字符的ASCII码
#值大小，那么谁的值大谁就大
print ("bazzzz" > "ba")

#.split(str="",num)以str为分隔符截取字符串，指定num，则仅截取num个字符串
str7 = "abc*xyz*lmn*opq***deg"
print (str7.split("*",3))
#['abc', 'xyz', 'lmn', 'opq***deg']

#.splitlines([keepends])  按照('\r','\r\n','\n')分割，返回一个列表
#keepends == True 会保留换行符

#.join(seq) 以指定的字符串分隔符，将seq中的所有元素组合成一个字符串

#.replace("a","b",n) 用b替换a，替换前n个
str8 = "ace,nice,apple"
str9 = str8.replace("a","x")
print (str9)
#'xce,nice,xpple'

#创建一个字符串映射表，将字符串中对应"a"字符转换成"6"，"c"转换成"5"
t = str.maketrans("ac","65")
str8 = "ace,nice,apple"
str9 = str8.translate(t)
print (str9)
#65e,ni5e,6pple

#startswith(str[,start][,end=len(str)])
#在给定的范围内判断是否以给定的字符串开头，如果没有指定范围，默认整个字符串
#endswith()

#编码
#.encode(enconding='utf-8',errors='strict')
str10 = "liangge jiayou"
#ignore 忽略错误
data = str10.encode("utf-8","ignore")
print (str10)
print (data)

#解码  注意：要与编码时的编码格式一致
str11 = data.decode("utf-8")
print (str11)

#.isalpha() 如果字符串中至少有一个字符且所有字符都为字母，那么返回True，否则返回False
#.isalnum() 如果字符串中至少有一个字符且所有字符都为字母或者数字，那么返回True，否则返回False
#.isupper() 如果字符串中至少有一个英文字符且所有字符都是大写的英文字母，那么返回True，否则返回False
#.islower() 如果字符串中至少有一个英文字符且所有字符都是小写，那么返回True，否则返回False
#.istitle() 如果字符串是标题化的返回True，否则返回False
#.isdigit() 如果字符串只包含数字返回True，否则返回False
#.isnumeric() 如果字符串只包含数字字符（包括中文数字）返回True，否则返回False
"一二三".isnumeric()
True
"一二三".isdigit()
False
#.isdecimal()如果字符串中只包含十进制字符返回True，否则返回False
#.isspace() 如果字符串中只包含空格则返回True，否则返回False






