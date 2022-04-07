import os

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
					continue    # 繼續跳到下一迴圈
			name, price = line.strip().split(',') 
			products.append([name, price])	
	return products


# 讓使用者輸入
def user_input(products):
	while True:
		name = input('起輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		price = int(price)   # 將 price casting 為整數方便日後檔案計算匯總
		products.append([name, price])  # 大清單 products 裝小清單 p (p 包含 name & price)
	print(products)
	return products


# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '價格是', p[1])


# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')  
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')  


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  # 檢查檔案在不在 
		print('找到檔案了！')
		products = read_file(filename)
	else:
		print('找不到檔案！')


	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)   # 用 main def() 作為程式的進入點

main()