#libreria random
import random

#las siguientes listas tienen el contenido del tablero que se imprime
tablero_n = ("       0      1      2      3      4      5")
tablero_nums = [[0,"-","-","-","-","-","-"],
                [1,"-","-","-","-","-","-"],
                [2,"-","-","-","-","-","-"],
                [3,"-","-","-","-","-","-"],
                [4,"-","-","-","-","-","-"],
                [5,"-","-","-","-","-","-"]]

#el random que genera la lista de listas con los números adentro
list_off = []
for i in range(1,19):
    for o in range(2):
        list_off.append(i)

random.shuffle(list_off)

listas = [[],[],[],[],[],[]]
for x in range(len(list_off)):
    if x >= 0 and x <= 5:
        listas[0].append(list_off[x])
    elif x >= 6 and x <= 11:
        listas[1].append(list_off[x])
    elif x >= 12 and x <= 17:
        listas[2].append(list_off[x])
    elif x >= 18 and x <= 23:
        listas[3].append(list_off[x])
    elif x >= 24 and x <= 29:
        listas[4].append(list_off[x])
    elif x >= 30 and x <= 35:
        listas[5].append(list_off[x])

#se cambia el orden de las listas usando el comando de abajo
random.shuffle(listas)

#se cambia el orden de los números de cada una de las listas
random.shuffle(listas[0])
random.shuffle(listas[1])
random.shuffle(listas[2])
random.shuffle(listas[3])
random.shuffle(listas[4])
random.shuffle(listas[5])

#variables utilizadas dentro del loop
#"i" se usa para hacer el ciclo infinito, "player" para determinar que jugador, y ambos "pairs" para tomar la cuenta de pares acertados 
i = 0
player = 1
pairs_1 = 0
pairs_2 = 0

#varibles usadas para determinar si el juego concluye o no
tabl_check = [[0],[1],[2],[3],[4],[5]]

for a in listas[0]:
    tabl_check[0].append(a)
for b in listas[1]:
    tabl_check[1].append(b)
for c in listas[2]:
    tabl_check[2].append(c)
for d in listas[3]:
    tabl_check[3].append(d)
for e in listas[4]:
    tabl_check[4].append(e)
for f in listas[5]:
    tabl_check[5].append(f)

#función que imprime el tablero 
def tabl():
    print("\n")
    print(tablero_n)
    print(*tablero_nums[0],sep="      ")
    print(*tablero_nums[1],sep="      ")
    print(*tablero_nums[2],sep="      ")
    print(*tablero_nums[3],sep="      ")
    print(*tablero_nums[4],sep="      ")
    print(*tablero_nums[5],sep="      ")

#función que imprime los resultados de ambos jugadores
def resul(pairs_1,pairs_2):
    print("\n")
    print(f"El jugador #1 tuvo  {pairs_1} número de pares \n")
    print(f"El jugador #2 tuvo {pairs_2} número de pares \n")
    if pairs_1 > pairs_2:
        print("¡Ganó el jugador #1! \n")
    elif pairs_1 < pairs_2:
        print("¡Ganó el jugador #2! \n")
    else:
        print("¡Empate!")

#Título
print("------------------Memorama------------------")

#el ciclo infinito hasta que se determine un alto
while i < 1:
    #lo siguiente imprime las listas de números
    #esto no se pone en el memorama final, pero se quitan de ser comentarios para saber si el código funciona
    #print(listas[0])
    #print(listas[1])
    #print(listas[2])
    #print(listas[3])
    #print(listas[4])
    #print(listas[5])

    #variables para comparar las elecciones hechas por los jugadores
    choice_1 = 0
    choice_2 = 0

    #función que imprime el tablero
    tabl()

    #checa el turno del jugador y lo imprime al usuario
    if player%2!=0:
        print("\n")
        print("Turno del jugador #1")
    elif player%2==0:
        print("\n")
        print("Turno del jugador #2")

    #inputs hechos por el usuario para determinar la posición de la primera elección
    print("\n")
    pos_y_1 = int(input("Primer renglón de 0 a 5: "))
    pos_x_1 = int(input("Primera columna de 0 a 5: "))
    print("\n")

    #checar si está dentro del rango y si no han sido adivinados
    while pos_y_1 > 5 or pos_y_1 < 0 or pos_x_1  > 5 or pos_x_1 < 0 or tablero_nums[pos_y_1][pos_x_1+1] != "-":
        if pos_y_1 > 5 or pos_y_1 < 0 or pos_x_1  > 5 or pos_x_1 < 0:
            print("Valores elegidos fuera del rango, vuelve a intentarlo")
            print("\n")
            pos_y_1 = int(input("Primer renglón de 0 a 5: "))
            pos_x_1 = int(input("Primera columna de 0 a 5: "))
            print("\n")
        elif tablero_nums[pos_y_1][pos_x_1+1] != "-":
            print("Valores elegidos ya han sido adivinados, vuelve a intentarlo")
            print("\n")
            pos_y_1 = int(input("Primer renglón de 0 a 5: "))
            pos_x_1 = int(input("Primera columna de 0 a 5: "))
            print("\n")
            
    #igualar la primera elección al número de "listas" y mostrar que número se eligió
    choice_1 = listas[pos_y_1][pos_x_1]
    tablero_nums[pos_y_1][pos_x_1+1] = choice_1
    print(f"Elegiste el número {choice_1}","\n")

    #función que imprime el tablero
    tabl()
    
    #inputs hechos por el usuario para determinar la posición de la segunda elección
    print("\n")
    pos_y_2 = int(input("Segundo renglón de 0 a 5: "))
    pos_x_2 = int(input("Segunda columna de 0 a 5: "))
    print("\n")

    #checar si está dentro del rango, si no han sido adivinados y si no son iguales a la elección anterior
    while pos_y_2 > 5 or pos_y_2 < 0 or pos_x_2  > 5 or pos_x_2 < 0 or tablero_nums[pos_y_2][pos_x_2+1] != "-" or pos_y_2 > 5 or pos_y_2 < 0 or pos_x_2  > 5 or pos_x_2 < 0 or (pos_x_2 == pos_x_1 and pos_y_2 == pos_y_1):
        if pos_y_2 > 5 or pos_y_2 < 0 or pos_x_2  > 5 or pos_x_2 < 0:
            print("Valores elegidos fuera del rango, vuelve a intentarlo")
            print("\n")
            pos_y_2 = int(input("Segundo renglón de 0 a 5: "))
            pos_x_2 = int(input("Segunda columna de 0 a 5: "))
            print("\n")
        elif pos_x_2 == pos_x_1 and pos_y_2 == pos_y_1:
            print("Valores elegidos iguales a los anteriores, vuelve a intentarlo")
            print("\n")
            pos_y_2 = int(input("Segundo renglón de 0 a 5: "))
            pos_x_2 = int(input("Segunda columna de 0 a 5: "))
            print("\n")
        elif tablero_nums[pos_y_2][pos_x_2+1] != "-":
            print("Valores elegidos ya han sido adivinados, vuelve a intentarlo")
            print("\n")
            pos_y_2 = int(input("Segundo renglón de 0 a 5: "))
            pos_x_2 = int(input("Segunda columna de 0 a 5: "))
            print("\n")
        
    #igualar la primera elección al número de "listas" y mostrar que número se eligió
    choice_2 = listas[pos_y_2][pos_x_2]
    tablero_nums[pos_y_2][pos_x_2+1] = choice_2
    print(f"Elegiste el número {choice_2}","\n")

    #función que imprime el tablero
    tabl()

    #si los números no son iguales, cambiar el tablero a su valor inicial
    if choice_1 != choice_2:
        tablero_nums[pos_y_1][pos_x_1+1] = "-"
        tablero_nums[pos_y_2][pos_x_2+1] = "-"
            
        #función que imprime el tablero
        tabl()

    #si ambos números adivinados son iguales, se aumenta el valor de "pairs" al respectivo jugador
    if player%2!= 0 and choice_1 == choice_2:
        pairs_1 += 1
    elif player%2== 0 and choice_1 == choice_2:
        pairs_2 += 1

    #input que pregunta al usuario si desea continuar
    print("\n")
    con = input("Desea continuar (s/n)?   ")

    #si se responde que sí, el código continua
    if con == "S" or con == "s":

        #si el jugador acierta, player se queda en el mismo valor
        #pero si falla, el turno pasa al siguiente jugador
        if choice_1 == choice_2:
            continue
        else:
            player += 1

    #si se responde que no, el juego imprime los resultados y acaba con el código
    elif con == "N" or con == "n":
        resul(pairs_1,pairs_2)
        break

    #si todos los números han sido adivinados, se imprimen los resultados y se acaba el código
    if tabl_check == tablero_nums:
        resul(pairs_1,pairs_2)
        break
