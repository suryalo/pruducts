products = []
while True:
	name = input('起輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])  # 大清單 products 裝小清單 p (p 包含 name & price)
print(products)