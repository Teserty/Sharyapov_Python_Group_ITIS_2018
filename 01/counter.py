if __name__ == "__main__":   
	d = {}
	a = open("1.txt")
	for i in a:
		if i in d:
			d[i] = d[i]+1
		else:
			 d[i]=1
	print(d)         