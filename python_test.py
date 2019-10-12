# 字符串倒序
s1 = 'hello word'
print(s1[::-1])

# 标题首字母大写
print(s1.title())

# 去除重复字符
s2 = 'aabbccddeeff'
print("".join(set(s2)))

# 列表生成
print([x for x in range(10)])

# 数值交换
a,b = 10,20
a,b = b,a
print(a,b)

# 字符切片
print('hello world'.split())
print('hello,world'.split(','))

# 异常处理
try:
	print(1/1)
except ZeroDivisionError as e:
	print('error: division zero')
else:
	print('normal')
finally:
	print('completely')

# 列表随机采样
import random
red_ball = [x+1 for x in range(33)]
bull_ball = [x+1 for x in range(12)]
for i in range(10):
	red_ball_list = random.sample(red_ball,5)
	bull_ball_list = random.sample(bull_ball,2)
	red_ball_list.sort()
	bull_ball_list.sort()
	print(red_ball_list,bull_ball_list)
