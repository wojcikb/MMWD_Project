from p_initial_solution import initial_solution
from p_load_points import load_points

from itertools import combinations

def neighborhood_combination(vec):
	vec2 = vec[:]
	vec2.remove(0)
	vec2.remove(0)
	comb = combinations(vec2,2)
	comblist = list(comb)
	return comblist
	
	




if __name__ == '__main__':
	atr = load_points('points.txt')
	first_solution = initial_solution(atr)
	print(first_solution)
	neigh_comb = neighborhood_combination(first_solution)
	print(neigh_comb)

