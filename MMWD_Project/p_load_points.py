#from p_load_points_spec import load_points_spec

def load_points(file_points):
	with open(file_points) as f:
		for line in f:
			data = line.split()
	return data
	
if __name__ == '__main__':
	atrakcje = load_points('points.txt')
#	points = load_points_spec('dane_punkty.txt')
	print(atrakcje)
#	print(points)
