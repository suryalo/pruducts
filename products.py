# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue    # 繼續跳到下一迴圈
		name, price = line.strip().split(',') 
		products.append([name, price])

			#先用strip()把換行符號去掉
			#再用‘,'當作切割的基準
		
print(products)


# 讓使用者輸入
while True:
	name = input('起輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	price = int(price)   # 將 price casting 為整數方便日後檔案計算匯總
	products.append([name, price])  # 大清單 products 裝小清單 p (p 包含 name & price)
print(products)


# 印出所有購買紀錄
for p in products:
	print(p[0], '價格是', p[1])


# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')  
		
		# 在 for loop 開始前先寫入標題欄	
		# 但在寫入標題時會有中文亂碼問題，使用 encode = 'utf-8' 這個編碼（encoding)來解決
	
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  

		# \n 為換行
		# 因為前面有將 price 轉換成整數，這邊加號只能做「字串」的相加
		# 故要把 p[1] 轉換為 string(字串)