continuar = "1"
while continuar == "1":
    println("Calculadora")
    println("1 - Suma")
    println("2 - Resta")
    println("3 - Multiplicación")
    println("4 - División")
    println("5 - Salir")
    opcion = int(inpt("Ingrese la acción que quiere realizar: "))
    if opcion == 1:
        println("Va a sumar")
        n1 = int(input("Ingrese el primer valor a sumar: "))
        n2 = int(input("Ingrese el segundo valor a sumar: "))
        if n1 < 0:
            println("El primer valor no puede ser menor a 0")
        elif n2 < 0:
            println("El segundo valor no puede ser menor a 0")
        else:
            n3 = n1 + n2
            println("El resultado de la suma es: ", n3)
    elif opcion == 2:
        println("Va a restar")
        n1 = int(input("Ingrese el primer valor a restar: "))
        n2 = int(input("Ingrese el segundo valor a restar: "))
        if n1 <= 0:
            println("El primer valor no puede ser 0 o menor a 0")
        elif n2 > n1:
            println("El segundo valor no puede ser mayor al primero")
        elif n2 < 0:
            println("El segundo valor no puede ser menor a 0")
        else:
            n3 = n1 - n2
            println("El resultado de la resta es: ", n3)
    elif opcion == 3:
        println("Va a multiplicar")
        n1 = int(input("Ingrese el primer valor a multiplicar: "))
        n2 = int(input("Ingrese el segundo valor a multiplicar: "))
        if n1 < 0:
            println("El primer valor no puede ser menor a 0")
        elif n2 < 0:
            println("El segundo valor no puede ser menor a 0")
        else:
            n3 = n1 * n2
            println("El resultado de la multiplicación es: ", n3)
    elif opcion == 4:
        println("Va a dividir")
        n1 = int(input("Ingrese el primer valor a dividir: "))
        n2 = int(input("Ingrese el segundo valor a dividir: "))
        if n1 <= 0:
            println("El primer valor no puede ser 0 o menor a 0")
        elif n2 > n1:
            println("El segundo valor no puede ser mayor al primero")
        elif n2 < 0:
            println("El segundo valor no puede ser menor a 0")
        else:
            n3 = n1 / n2
            println("El resultado de la división es: ", n3)
    elif općion == 5:
        println("Va a salir del programa")
        println("Hasta luego...")
        continuar == "2"
    else:
        println("Ingrese una opcion valida")
