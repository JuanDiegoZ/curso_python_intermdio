from re import I


def run():
    dictionary_squares ={i :i**3 for i in range(1,101) if i%3 !=0 }
    print(dictionary_squares)

if __name__ == "__main__":
    run()