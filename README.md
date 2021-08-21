# Proyecto Cafetería

## Contexto
La situación actual ha tenido gran impacto en la sociedad, la pandemia ha causado que las personas permanezcan en su hogar y así evitar que el virus se expanda. 
Esto ha traído repercusiones en los establecimientos locales, como las cafeterías. Progresivamente nuestras actividades habituales se reincorporan en nuestro día a día.
Las cafeterías vuelven a abrir y buscan recuperarse, además de adaptarse a la nueva normalidad. Este programa tiene como objetivo apoyar a los cafés para que su servicio sea efectivo, dinámico y adecuado para la circunstancia actual, donde se busca que la interacción entre personas sea mínima para cuidar el bienestar de todos.
A través del programa, el cliente tiene la oportunidad de observar el menú del café, con alimentos y bebidas, al igual que los precios y realizar su pedido. Finalmente el usuario obtendrá su total de los productos que desea consumir.

## Algoritmo

E0=
1. Se imprime el texto de bienvenida al usuario
2. Se imprime el texto solicitando el nombre al usuario
3. El texto introducido se guarda en una variable "nombre"
4. Se imprime el texto de "Introduce la opción de tu preferencia"
5. Se imprime el texto de "alimentos" y "bebidas"
6. Si el usuario introduce "alimentos"
7. Se imprime el texto con los alimentos y precios
8. Los alimentos son establecidos como variables
9. Se imprime el texto de "Cuales alimentos son de tu preferencia, especifica cantidad"
10. Se imprime el texto de "Deseas pedir, alimento1?"
11. Si el usuario introduce "0", se guarda en variable de "cantalimento1"
12. O si el usuario introduce "1", se guarda en variable de "cantalimento1"
13. Se imprime el texto de "Deseas pedir, alimento2?"
14. Si el usuario introduce "0", se guarda en variable de "cantalimento2"
15. O si el usuario introduce "1", se guarda en variable de "cantalimento2"
16. Se imprime el texto de "Deseas otra cosa?"
17. Si el usuario introduce "Sí" ir a paso 18, si introduce "No" ir a paso 32
18. Se imprime el texto de "alimentos" y "bebidas"
19. Si el usuario introduce "bebidas"
20. Se imprime el texto con los bebidas y precios
21. Las bebidas son establecidos como variables
22. Se imprime el texto de "Cuales bebidas son de tu preferencia, especifica cantidad"
23. Se imprime el texto de "Deseas pedir, bebida1?"
24. Si el usuario introduce "0", se guarda en variable de cantbebida1
25. O si el usuario introduce "1", se guarda en variable de cantbebida1
26. Se imprime el texto de "Deseas pedir, bebida2?"
27. Si el usuario introduce "0", se guarda en variable de cantbebida2
28. O si el usuario introduce "1", se guarda en variable de cantbebida2
29. Se imprime el texto de "Deseas otra cosa?"
30. Si el usuario introduce "Sí" 
31. Ir a paso 5
32. Else
33. El programa realiza la multiplicación de la variable de cantalimento1 * precio (cantidad definida por el menú) y se guarda en la variable totalalimento1
34. El programa realiza la multiplicación de la variable de cantalimento2 * precio (cantidad definida por el menú) y se guarda en la variable totalalimento2
35. El programa realiza la multiplicación de la variable de cantbebida1 * precio (cantidad definida por el menú) y se guarda en la variable totalbebida1
36. El programa realiza la multiplicación de la variable de cantbebida2 * precio (cantidad definida por el menú) y se guarda en la variable totalbebida2
37. El programa realiza la suma de la variable totalalimento1 + totalalimento2 y lo guarda en la variable totalalimentos
38. El programa realiza la suma de la variable totalbebida1 +  totalbebida2 y lo guarda en la variable totalbebidas
39. El programa realiza la suma de la variable totalalimentos + totalbebidas y lo guarda en variable total
40. Ef=Se imprime el texto "Su total es:", se imprime la variable total
