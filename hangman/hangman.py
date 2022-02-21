from imagenes import  *
import random



with open('/home/juandiegozipaquiraa/Documents/Platzi/ingenieria_software/curso_phyto_intermedio/listas_diccionarios_anidados/hangman/data.txt','r') as f:
    list_of_worlds = [i.replace("\n","") for i in f]

#Funcion que elige un palabra aleatoria de la base de datos.
def string(lista):
    random_world = random.choice(lista)
    world = list(random_world)
    return world      

#Funcion que encuenta si la letra ingresada se encuentra en la cadena.

def hadgman(world):
    world_player = str(input("Ingresa la letra: "))
    list =[]
    for i in world:
        if world_player == str(i):
            list.append(i)
        else:
            list.append("_") 
    
       
    return list

#Funcion que imprime la palabra y si falta alguna  

def print_hm(list_world,list_hadgman):

    acierto = False
    for i in range(len(list_world)):
        if list_hadgman[i] != list_world[i] and list_hadgman[i] == "_":
            list_hadgman[i] = list_world[i]
            acierto = True    
        
        print(list_hadgman[i], end =" ")
    
    return acierto

    
    print

def main():
    intentos = 8
    jugador = True
    aciertos = 0
    world = string(list_of_worlds)
    list_hadgman=["_" for i in range(len(world))]
    print(intro())
    for i in list_hadgman:
        print(i,end = " ")
    print(" ")


    while jugador:
        if intentos == 1:
            jugador = False
            print("perdiste!!!")
        elif aciertos == len(world):
            print("ganaste!!!")
            jugador = False

        else:
            intento_palabra = print_hm(hadgman(world),list_hadgman)
            if intento_palabra:
                print(" ","acertaste")
                aciertos += 1
            else:
                intentos -=1
                print(ahorcado()[7 - intentos])      
                print(" ","no tenia esa letra")
        

    




if __name__ == "__main__":
    main()
