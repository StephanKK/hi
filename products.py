products = []
while True:
	name = input('请输入商品名称： ')
	if name == 'q':
		break
	price = input('请输入价格： ')
	p = [] # p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

for p in products:
	print(p[0], '的价格是', p[1])