#funcion, squaring the number.
def multiply_two(i):
        return i*i
        
# Main, contains the list,add values at the list  whit not divicibel for tree and prints it. 
def run():
    my_list =[]
    for i in range(1,101):
        if i%3 !=0:
          my_list.append(multiply_two(i))  


    print("first hundred natural numbers squared not divicible in tree: ", my_list) 
if __name__ == "__main__":
    run()