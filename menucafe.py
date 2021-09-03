#Ximena Islas A01423601 "Coffee House"


print("Bienvenido a Coffee House, tu cafeteria local favorita")

print("Ingresa tu nombre")
nombre = str(input())


tipo_menu= int(input("Selecciona el menu de tu preferencia, 0:alimentos/ *1:bebidas no disponibles*, "))

# Funciones (alimentos)

def total_panini(cantidad_panini):
    return cantidad_panini*100.0

def total_pan(cantidad_pan):
    return cantidad_pan*150.0

def total_dona(cantidad_dona):
    return cantidad_dona*50.0

def cuenta_total_alimentos(cantidad_panini, cantidad_pan, cantidad_dona ):
    
    return total_panini(cantidad_panini) + total_pan(cantidad_pan) + total_dona(cantidad_dona)

if (tipo_menu == 0):
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







