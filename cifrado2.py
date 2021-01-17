#____transformamos las letras en numero segun su posicion_________
def transfor(message):
    letter = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",".",","]
    number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    cifrado = []
    for i in range(len(message)):
        for j in range(len(letter)):
            if message[i] == letter[j]:
                cifrado.append(number[j])

    #pull_apart_4(cifrado)
    return cifrado

#_____________calculamos el tamaño del arreglo para asi asignar la separacion __________________
#_____________de matrices con una cantidad de 4 letras___________________________________
def pull_apart_4(message1):
    ty=len(message1)/4
    arr = message1
    flag = False
    sum = len(message1)

    while flag != True:
        if '.0' in str(ty):
            flag = True
        else:
            sum += 1
            for i in range(sum):
                if (len(message1)-1) > i:
                    arr[i] = message1[i]
                else:
                    arr.append(" ")
        ty = len(arr)/4
    return arr
#_____________encriptamos la palabra_________________________________
def encrypt(arr,cifrado):
    crypt = [0]*4
    crypt[0] = (cifrado[0] * arr[0]) + (cifrado[1] * arr[2])
    crypt[1] = (cifrado[0] * arr[1]) + (cifrado[1] * arr[3])
    crypt[2] = (cifrado[2] * arr[0]) + (cifrado[3] * arr[2])
    crypt[3] = (cifrado[2] * arr[1]) + (cifrado[3] * arr[3])
    
    return crypt

#___________________encontramos la determinante____________________________________

def determinante(cifrador):
    det = (cifrador[0] * cifrador[3]) - (cifrador[2] * cifrador[1])
    return det

#__________________se encuentra la determinante_____________________________
def Madjunta(cifrador):
    arr = [0] * len(cifrador)
    arr[0] = cifrador[3]
    arr[1] = cifrador[2] * -1
    arr[2] = cifrador[1] * -1
    arr[3] = cifrador[0] 
    return arr

#__________________se encuentra la transpuesta______________________________
def traspuesta(cifrador):
    arr = [0] * len(cifrador)
    aux = cifrador[1]
    arr[0] = cifrador[0]
    arr[1] = cifrador[2] 
    arr[2] = aux 
    arr[3] = cifrador[3] 
    return arr

#________________se encuentra la inversa________________________
def inversa(det,tras):
    arr = [0] * len(tras)
    arr[0] = int(tras[0]/det)
    arr[1] = int(tras[1]/det)
    arr[2] = int(tras[2]/det)
    arr[3] = int(tras[3]/det)
    return arr

#_________________________________________________________________
#____transformamos las letras en numero segun su posicion_________
def antitransfor(message):
    letter = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",".",","]
    number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    cifrado = []
    for i in range(len(message)):
        for j in range(len(number)):
            if message[i] == number[j]:
                cifrado.append(letter[j])
    return cifrado

#______________imprecion____________________
def imprime(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")

#_______________________main____________________________________
import random
if __name__ == '__main__':
    message = input("Mensaje: ").lower()
    arr1 = []
    crypt = [2,3,1,2]
    arr2 = []
    arr3 = arr2
    flag = False
    for i in message:
        arr1.append(i)
    print("\ntamaño antes:",len(arr1))

    #completamos el arreglo con espacios para calcular cifrado
    res1 = pull_apart_4(arr1)
    imprime(res1)

    #transformamos letras a numero
    print("\n","\ntamaño despues:",len(res1))
    res2 = transfor(res1)
    imprime(res2)
    print("\n")
    
    #cifrador
    print("cifrador")
    imprime(crypt)
    print("\n")

    #pasamos los numero en cuatro numeros en sub arreglos
    #_________________________________________________________
    cont1 = 0
    cont2 = 4
    for i in range(int(len(res2)/4)):
        arr2.append([])
        for j in range(cont1,cont2):
            num = res2[j]
            arr2[i].append(num)
        cont1 = cont2
        cont2 += 4
    #__________________________________________________________

    #encontramos la determinante
    det = determinante(crypt)
    print("determinante:",det)

    #consultamos la determinante si la det = 0 no exixte inversa
    if det != 0:
        for i in range(len(arr2)):   
            arr3[i] = encrypt(arr2[i],crypt)

        #prime la frase ya encriptada
        print("\nencriptado")
        for i in range(len(arr3)):
            for j in range(len(arr3[i])):
                print(arr3[i][j],end=" ")

        #procesos para calcular la inverza
        print("\n___________________________________________\n")
        madj = Madjunta(crypt) #la adjunta
        print("Madjunta:\n",madj,"\n")
        tras = traspuesta(madj) # transpuesta
        print("transpuesta\n",tras,"\n")
        inver = inversa(det,tras) # inverza
        print("inversa\n",inver,"\n")

        #imprime la desencriptacion por medio de punto entre la matris c⁻¹ * D
        des = arr3
        anti = arr3
        print("desencriptado")
        for i in range(len(arr3)):
            des = encrypt(arr3[i],inver)
            anti[i] = antitransfor(des)
            imprime(des)

        # trasforma la desencriptacion de la matris de numeros a letras
        print("")
        print("\nfrase decodificada")
        for i in range(len(anti)):
            for j in range(len(anti[i])):
                print(anti[i][j],end="")
        print("\n")
    # si la matris cifradora su determinante es '0' no se puede calcular la inverza
    else:
        print("la determinante es: ",det,"\n si es igual a '0' no se puede calcular la inverza")