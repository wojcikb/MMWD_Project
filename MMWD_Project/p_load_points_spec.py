
def load_points_spec(file_points):
	data = {}
	with open(file_points) as f:
		for line in f:
			(key,s,t,c) = line.split()
			data[int(key)] = [s,t,c]
		return data
		
if __name__ == '__main__':
	punkty = load_points_spec("dane_punkty.txt")
	print(punkty)
