def read():
    with open("./archivos/numbers.txt","r",encoding="utf-8") as read:
        numbers =[int(line) for line in read]

    print(numbers)
def write():
    names = ["Marce","Julia","Pepa","Rocìo"]
    with open("./archivos/names.txt","a",encoding="utf-8") as f:
        names_txt = [f.write(name + "\n") for name in names]

def run():
    read()
    write()


if __name__ == "__main__":
    run()