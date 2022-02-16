from functools import reduce
import numbers
from tokenize import Number 

list_exe =[2,2,2,2,2,2]

# high order functions vs comprehensions. (filter)
def run_one(list):
    my_list = [i for i in list if i%2 != 0]
    print(my_list)
def run_two(my_list):
    odd = list(filter(lambda x: x%2 != 0, my_list))
    print(odd)

# high order functions vs comprehensions. (map)

def run_tree(list):
    my_list = [i**2 for i in list]
    print(my_list)
def run_four(my_list):
    odd = list(map(lambda x: x**2, my_list))
    print(odd)

# high order functions vs comprehensions. (reduce)

def run_five(list):
    alt_multiplied = 1
    
    for i in list:
        alt_multiplied *= i
    print(alt_multiplied)

def run_six(my_list):
    Number = reduce(lambda a,b: a*b, my_list)
    print(numbers)



if __name__ == "__main__":
    run_six(list_exe)

