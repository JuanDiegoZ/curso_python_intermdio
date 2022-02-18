def divisors(num):
    divisors = [i for i in range(1,num + 1) if num%i == 0]
    return divisors


def run():
    try:
        
        num = int(input('Ingresa un número: '))
        try:
            if num <= 0:
                raise ValueError("Debe ser un numero mayor que cero!.")
            print(divisors(num))
            print("Terminó mi programa")
    
        except ValueError as ve:
            print(ve)
    
    except ValueError:
        print("Debes ingresar un valor numerico.")

if __name__ == '__main__':
    run()