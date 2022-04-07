products = []
while True:
	name = input('起輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])  # 大清單 products 裝小清單 p (p 包含 name & price)
print(products)

for p in products:
	print(p[0], '價格是', p[1])

# 寫入檔案
with open('procucts.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # \n 為換行