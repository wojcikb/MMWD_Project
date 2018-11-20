
def load_roads(file_roads):
	data = {}
	with open(file_roads) as f:
		for line in f:
			(key,a,b,c,d)  = line.split()
			data[key] = [a,b,c,d]
	return data

if __name__ == '__main__':
	drogi = load_roads("dane_drogi.txt")
	print(drogi)
