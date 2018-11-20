
def load_roads(data):
	with open("dane_drogi.txt") as f:
		for line in f:
			(key,a,b,c,d)  = line.split()
			data[key] = [a,b,c,d]
	
