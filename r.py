import random
start = input('请输起始数字： ')
start = int(start)
end = input('请输入终止数字： ')
end = int(end)



r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('请输入数字： ')
	num = int(num)
	if num == r:
		print('猜中了！')
		print('这是你猜的', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('这是你猜的', count, '次')