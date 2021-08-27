
print("Bienvenido a Coffee House, tu cafeteria local favorita")

print("Ingresa tu nombre")
nombre = str(input())

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

total_panini = 100*cantidad_panini
total_pan = 150*cantidad_pan
total_dona = 50*cantidad_dona

total = total_panini + total_pan + total_dona

print("Y será un total de:", total,"pesos")



