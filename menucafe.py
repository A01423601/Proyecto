"""Ximena Islas A01423601 "Coffee House"""


print("Bienvenido a Coffee House, tu cafeteria local favorita")

print("Ingresa tu nombre")
nombre = str(input())


lista_alimentos=[]
lista_bebidas=[]

total_alimentos=[]
total_bebidas=[]





"""Funciones (alimentos):"""

def total_panini(cantidad_panini):
    return cantidad_panini*100.0

def total_pan(cantidad_pan):
    return cantidad_pan*150.0

def total_dona(cantidad_dona):
    return cantidad_dona*50.0

def cuenta_alimentos(cantidad_panini, cantidad_pan, cantidad_dona ):
    
    return total_panini(cantidad_panini) + total_pan(cantidad_pan) + total_dona(cantidad_dona)


"""Funciones (bebidas):"""

def total_jugo(cantidad_jugo):
    return cantidad_jugo*30.0

def total_cafe(cantidad_cafe):
    return cantidad_cafe*20.0

def total_malteada(cantidad_malteada):
    return cantidad_malteada*50.0

def cuenta_bebidas(cantidad_jugo, cantidad_cafe, cantidad_malteada ):
    
    return total_jugo(cantidad_jugo) + total_cafe(cantidad_cafe) + total_malteada(cantidad_malteada)




entrar_menu= str(input("Ingresa ´entrar´ para obsevar al menú de Coffee House o ingresa otro texto para marcharte del menu: "))

def menu():
    while entrar_menu == "entrar":
        """Se crea un ciclo para que el usuario tenga la posibilidad de observar los menus las veces deseadas, hasta seleccionar la opcion de salir el menu"""

        tipo_menu= int(input("Selecciona el menu de tu preferencia, 0:alimentos/ 1:bebidas/ 2: total/ 3:salir del menu "))


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

            

            lista_alimentos.append(cantidad_panini)
            lista_alimentos.append(cantidad_pan)
            lista_alimentos.append(cantidad_dona)

            numero_alimentos= sum (lista_alimentos)

            
            
            

            

            print("De esto, será un total de:", cuenta_alimentos(cantidad_panini, cantidad_pan, cantidad_dona), "pesos")

            total_alimentos.append(cuenta_alimentos(cantidad_panini, cantidad_pan, cantidad_dona))

            final_alimentos= sum (total_alimentos)

            


        elif (tipo_menu == 1):
            """Si el usuario selecciona la opcion de bebidas, el menu de bebidas es mostrado"""
            
            print("Contamos con los siguientes bebidas",nombre)            
            print("Jugo de naranja, $30")
            print("Cafe, $20")
            print("Malteada vainilla, $50")
            print("¿Cuales alimentos son de tu preferencia?, especifica cantidad")
            cantidad_jugo = int(input("¿Cuantas ordenes de jugo de naranja te gustaria pedir?"))
            cantidad_cafe = int(input("¿Cuantas ordenes de cafe te gustaria pedir?"))
            cantidad_malteada = int(input("¿Cuantas ordenes de malteada de vainilla te gustaria pedir?"))

            

            lista_bebidas.append(cantidad_jugo)
            lista_bebidas.append(cantidad_cafe)
            lista_bebidas.append(cantidad_malteada)

            numero_bebidas= sum (lista_bebidas)

            
            
            

            

            print("De esto, será un total de:", cuenta_bebidas(cantidad_jugo, cantidad_cafe, cantidad_malteada ), "pesos")


            total_bebidas.append(cuenta_bebidas(cantidad_jugo, cantidad_cafe, cantidad_malteada))
            
            final_bebidas= sum (total_bebidas)

            


        elif (tipo_menu == 2):
            """Si el usuario selecciona la opcion de total, el total sera reflejado"""

            tipo_cuenta= int(input("Introduce el numero de la cuenta que deseas: 0:cuenta alimentos/ 1:cuenta bebidas/ 2:cuenta alimentos y bebidas "))
                               
            if (tipo_cuenta==0):
                print(nombre,"el numero de ordenes de alimentos que has solicitado son", numero_alimentos)
                print ("El total de los alimentos es: ",final_alimentos, "pesos")

            elif (tipo_cuenta==1):
                print(nombre,"el numero de ordenes de bebidas que has solicitado son", numero_bebidas)
                print ("El total de los bebidas es: ",final_bebidas, "pesos")
                


            elif (tipo_cuenta==2):
                print("El numero de ordenes de alimentos que has solicitado son", numero_alimentos)
                print("El numero de ordenes de bebidas que has solicitado son", numero_bebidas)
                print ("El total de los alimentos es: ",final_alimentos, "pesos")
                print ("El total de los bebidas es: ",final_bebidas, "pesos")
                
            

            return ("¡Gracias por venir, vuelve pronto!")           
            break
            

        elif (tipo_menu == 3):
            """El usuario selecciona salir del menu desde el ciclo, se cierra el programa"""
            return ("¡Gracias por venir, vuelve pronto!")           
            break
      
        else:
            print ("No contamos con ese menu")

    return ("¡Gracias por venir, vuelve pronto!")
    """El usuario selecciona salir, no se entra al ciclo y se cierra el programa """

print(menu())

