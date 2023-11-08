if __name__ == '__main__':
	with open('29服小号书签.txt', 'r+') as f:
		a = f.readlines()
		a = a[0]
		print(type(a))
		f.close()