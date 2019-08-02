import os # operating system


#读取档案
products = []
if os.path.isfile('products.csv'):
	print('yeah!')
	with open('products.csv','r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('No!')

#让使用者输入
while True:
	name = input('请输入商品名称： ')
	if name == 'q':
		break
	price = input('请输入价格： ')
	price = int(price)
	p = [] # p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

#输出所有产品价格
for p in products:
	print(p[0], '的价格是', p[1])

#写入档案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')