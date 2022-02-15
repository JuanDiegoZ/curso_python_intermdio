def multiply_two(i):
        return i*i
        
# Main, contains the list and dictionary in the exercise. 
def run():
    my_list =[]
    for i in range(0,101):
        my_list.append(multiply_two(i))

    print("first hundred natural numbers squared: ", my_list)

if __name__ == "__main__":
    run()