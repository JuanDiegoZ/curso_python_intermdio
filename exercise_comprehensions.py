#funcion used comprehensions first 9999 natural numbers multiply for 4,6,9.
def run():
    my_list =[i for i in range (1,9999) if i%36==0 ]
    
    print(my_list)

if __name__ == "__main__":
    run()