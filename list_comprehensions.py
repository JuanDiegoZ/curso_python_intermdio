#funcion, squaring the number.
def multiply_two(i):
        return i*i
        
# Main_one, contains the list,add values at the list  whit not divicibel for tree and prints it. 
def run_one():
    my_list =[]
    for i in range(1,101):
        if i%3 !=0:
          my_list.append(multiply_two(i))  


    print("first hundred natural numbers squared not divicible in tree: ", my_list) 
        
# Main_two, contains the list,add values at the list  whit not divicibel for tree and prints it.
#USED COMPREHENSIONS!!!.
def run_two():
    my_list =[i**2 for i in range (1,101) if i%3!=3]



    print("first hundred natural numbers squared not divicible in tree: ", my_list) 
if __name__ == "__main__":
    run_two()