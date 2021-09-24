"""Ximena Islas A01423601 "Coffee House"""


print("Bienvenido a Coffee House, tu cafeteria local favorita")

print("Ingresa tu nombre")
nombre = str(input())



"""Funciones (alimentos):"""

def total_panini(cantidad_panini):
    return cantidad_panini*100.0

def total_pan(cantidad_pan):
    return cantidad_pan*150.0

def total_dona(cantidad_dona):
    return cantidad_dona*50.0

def cuenta_total_alimentos(cantidad_panini, cantidad_pan, cantidad_dona ):
    
    return total_panini(cantidad_panini) + total_pan(cantidad_pan) + total_dona(cantidad_dona)



entrar_menu= str(input("Ingresa ´entrar´ para obsevar al menú de Coffee House o ingresa otro texto para marcharte del menu: "))

def menu():
    while entrar_menu == "entrar":
        """Se crea un ciclo para que el usuario tenga la posibilidad de observar los menus las veces deseadas, hasta seleccionar la opcion de salir el menu"""

        tipo_menu= int(input("Selecciona el menu de tu preferencia, 0:alimentos/ 1:bebidas/ 2:salir del menu "))


        if (tipo_menu == 0):
            """Si el usuario selecciona la opcion de alimentos, el menu de alimentos es mostrado"""
            
            print("Contamos con los siguientes platillos",nombre)
            print("Panini de pollo, $100")
            print("Pan frances, $150")
            print("Dona de chocolate, $50")
            print("¿Cuales alimentos son de tu preferencia?, especifica cantidad")
            cantidad_panini = int(input("¿Cuantas ordenes de panini de pollo te gustaria pedir?"))
            cantidad_pan = int(input("¿Cuantas ordenes de pan frances te gustaria pedir?"))
            cantidad_dona = int(input("¿Cuantas ordenes de dona de chocolate te gustaria pedir?"))

            numero_alimentos = cantidad_panini + cantidad_pan + cantidad_dona

            print(nombre,"el numero de ordenes que has solicitado son", numero_alimentos)

            print("Y será un total de:", cuenta_total_alimentos(cantidad_panini, cantidad_pan, cantidad_dona), "pesos")


        elif (tipo_menu == 1):
            """Si el usuario selecciona la opcion de bebidas, el menu de bebidas es mostrado"""
            """ Posterirmente se agregara la opcion de que el usuario seleccione las bebidas de su preferncia y se reflejara su total, asi como en el menu de alimentos"""
            
            print("Contamos con los siguientes bebidas",nombre)            
            print("Jugo de naranja, $30")
            print("Cafe, $20")
            print("Malteada vainilla, $50")

        elif (tipo_menu == 2):
            """El usuario selecciona salir del menu desde el ciclo, se cierra el programa"""
            return ("¡Gracias por venir, vuelve pronto!")           
            break
      
        else:
            print ("No contamos con ese menu")

    return ("¡Gracias por venir, vuelve pronto!")
    """El usuario selecciona salir, no se entra al ciclo y se cierra el programa """

print(menu())

