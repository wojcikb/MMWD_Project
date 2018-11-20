from p_load_points import load_points

import random

def initial_solution(vec):
	vec2 = vec[:]
	number_of_points = len(vec)
	number_of_points_for_solution = (3 * number_of_points)/5
	number_of_points_for_solution = round(number_of_points_for_solution)
	first_solution = []
	first_solution.append(0)
	for x in range(number_of_points_for_solution):
		r = random.choice(vec2)
		first_solution.append(r)
		vec2.remove(r)
	first_solution.append(0)
	return first_solution
	 
	


if __name__ == '__main__':
	atr = load_points('points.txt')
	first_solution = initial_solution(atr)
	print(first_solution)
