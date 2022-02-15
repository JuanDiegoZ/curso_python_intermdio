#Ejercice comprehensions in dictionaries, square root on first one thousand natural numbers.
def run():
    dictionary_squares ={i :round(i**(1/2),3) for i in range(1,1001)}
    print(dictionary_squares)

if __name__ == "__main__":
    run()