import numpy as np
from itertools import permutations

# Perform calculation to find optimal solution
def calculate_solution(main_li,x):
  for i in range(len(main_li)):
    sum = 0
    for j in range(len(main_li[i])-1, -1, -1):
      a = x[main_li[i][j-1]][main_li[i][j]]
      sum += a
    result[tuple(main_li[i])] = int(sum)

# Identify the route and min value
def final_route(result):
  min_val = min(result.values())

  for index,val in result.items():
    if val == min_val:
      return index, min_val

if __name__ == '__main__':
  x = np.random.randint(0,20,size=(5,5))
  starting_point = 0
  numbers = np.arange(starting_point, len(x))  # Generate numbers from 1 to 3
  n = 1
  result = {}
  
  print(x, end='\n\n')
  # Generate number of possible routes for n nodes it will be (n-1)!
  for i in range(1,len(numbers)):
    n = n*i

  # Applying permutation to generate all unqiue routes
  main_li = np.array(list(permutations(numbers, len(x))))[:n]
  column_to_add = np.full((main_li.shape[0], 1), starting_point)

  # Concatenate the original matrix with the new column
  main_li = np.concatenate((main_li, column_to_add), axis=1)

  calculate_solution(main_li,x)

  op = final_route(result)
  print(op)