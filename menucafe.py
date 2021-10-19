"""
Ximena Islas Berber A01423601 
Proyecto Coffee House python
Menu Cafeteria
El programa muestra el menu de la cafeteria,
el usuario selecciona los servicios que desea solicitar y
el programa realiza la cuenta de lo que el cliente ha solicitado
"""

print("Bienvenido a Coffee House, tu cafeteria local favorita")

print("Ingresa tu nombre")
nombre = str(input())


"""Listas"""

lista_alimentos=[]
lista_bebidas=[]

total_alimentos=[]
total_bebidas=[]





"""Funciones (alimentos):"""

def total_panini(cantidad_panini):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_panini valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de paninis solicitado
    """
    return cantidad_panini*100.0


def total_pan(cantidad_pan):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_pan valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de pan solicitado
    """
    return cantidad_pan*150.0

def total_dona(cantidad_dona):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_dona valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de donas solicitado
    """
    return cantidad_dona*50.0

def cuenta_alimentos(cantidad_panini, cantidad_pan, cantidad_dona ):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_panini valor numérico, cantidad_pan valor numérico, cantidad_dona valor numérico
    manda a llamar las funciones de total_panini(cantidad_panini),total_pan(cantidad_pan) y total_dona(cantidad_dona)
    y suma sus valores
    devuelve: resultado de operación numérico, siendo este 
    la cuenta de los alimentos
    """
    return total_panini(cantidad_panini) + total_pan(cantidad_pan) + total_dona(cantidad_dona)


"""Funciones (bebidas):"""

def total_jugo(cantidad_jugo):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_jugo valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de jugos solicitado
    """
    return cantidad_jugo*30.0

def total_cafe(cantidad_cafe):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_cafe valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de cafe solicitado
    """
    return cantidad_cafe*20.0

def total_malteada(cantidad_malteada):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_malteada valor numérico
    multiplica la cantidad por el valor del producto
    devuelve: resultado de operación numérico, siendo este 
    el precio total de la cantidad de malteadas solicitado
    """
    return cantidad_malteada*50.0

def cuenta_bebidas(cantidad_jugo, cantidad_cafe, cantidad_malteada ):
    """
    (uso de operadores, uso de funciones)
    recibe: cantidad_jugo valor numérico, cantidad_cafe valor numérico, cantidad_malteada valor numérico
    manda a llamar las funciones de total_jugo(cantidad_jugo),total_cafe(cantidad_cafe) y total_malteada(cantidad_malteada)
    y suma sus valores
    devuelve: resultado de operación numérico, siendo este 
    la cuenta de las bebidas
    """
    
    return total_jugo(cantidad_jugo) + total_cafe(cantidad_cafe) + total_malteada(cantidad_malteada)


"""Parte principal del programa"""

entrar_menu= str(input("Ingresa ´entrar´ para obsevar al menú de Coffee House o ingresa otro texto para marcharte del menu: "))

def menu():
    while entrar_menu == "entrar":
        """Se crea un ciclo para que el usuario tenga la posibilidad de observar los menus las veces deseadas, hasta seleccionar la opcion de salir el menu"""

        tipo_menu= int(input("Selecciona el menu de tu preferencia \n 0:alimentos \n 1:bebidas \n 2: total \n 3:salir del menu \n"))


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
            """Si el usuario selecciona la opcion de total"""

            tipo_cuenta= int(input("Introduce el numero de la cuenta que deseas: \n 0:cuenta alimentos \n 1:cuenta bebidas \n 2:cuenta alimentos y bebidas \n "))
                               
            if (tipo_cuenta==0):
                """Si el usuario selecciona la opcion de reflejar el total de la cuenta de los alimentos"""
                
                print(nombre,"el numero de ordenes de alimentos que has solicitado son", numero_alimentos)
                print ("El total de los alimentos es: ",final_alimentos, "pesos")

            elif (tipo_cuenta==1):
                """Si el usuario selecciona la opcion de reflejar el total de la cuenta de las bebidas"""
                
                print(nombre,"el numero de ordenes de bebidas que has solicitado son", numero_bebidas)
                print ("El total de los bebidas es: ",final_bebidas, "pesos")
                


            elif (tipo_cuenta==2):
                """Si el usuario selecciona la opcion de reflejar el total de la cuenta de los alimentos y las bebidas"""
                
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



"""datetime"""

"""
datetime es un módulo de la biblioteca de Python la cual nos
apoya a conocer la fecha y hora actuales.
Decidí agregar esta función ya que no la había ultilizado previamente y
encuentro muy interesante que podemos saber fecha y hora actuales
e imprimirlas en nuestro programa.
Considero que es escencial tener la fecha presente al trabajar en un cafe.

Con datetime.now podemos saber la fecha y hora actuales.
Agregando strftime, se toma como parametro el formato en el
que se desea observar el string de la fecha y hora.
Se cuenta con una gran cantidad de formatos para mostrar estas.
El formato que coloqué fue el que me pareció mÁs correcto y comprensible.
"""

from datetime import datetime

fecha_y_hora_actuales = datetime.now()

fecha_y_hora = fecha_y_hora_actuales.strftime("%d / %m / %Y %H:%M")

"""Formato: %d, día del mes; %m, mes; %Y, año; %H, hora; %M, minutos"""


print(fecha_y_hora)








"""Referencias"""

"""Orestes,Y. (2020). Python datetime:trabajando con fechas. Recuperado de: https://www.aluracursos.com/blog/python-datetime-trabajando-con-fechas"""
"""https://docs.python.org/es/3/library/datetime.html#datetime.datetime"""



