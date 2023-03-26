"""• Registro de los platillos: El encargado de cocina podrá administrar los platillos del
restaurante segmentados por su tipo: Entradas, platos fuertes, postres y bebidas.
Para lo cual, almacenará el sistema el tipo, descripción y precio SIN IVA.
• Lista de órdenes: El encargado de cocina podrá visualizar todas las ordenes
ejecutadas: Número de orden, usuario que lo solicita y la especificación de los
platillos ordenados. Además, podrá seleccionar una orden y darla por finalizada."""

print("Prueba")
identificacion = int(input("Selecciona tu rol: \n 1- Encargado \n 2- Cliente \n"))
encargado = 1
cliente = 2
if identificacion == 1:

    menu_principal = int(input("Menu principal: \n 1-Administrar platillo \n 2-Lista de ordenes \n"))
    administrar_platillos =1
    Lista_ordenes = 2
    x = 0
    while menu_principal == 1:
        adm = int(input("Elija una opcion: \n 1-Entradas \n 2-Platos fuertes \n 3-Postres \n 4-bebidas \n"))
        if adm == 1:
            entradas = int(input("1-Crema de ayote \n 2-Crema de vegetales \n 3-Ensalada verde \n 4-Crema de Esparrago \n"))
            if entradas == 1:
                print(" Ingredientes \n Ayote partidos en trozos \n 3 tazas de leche \n 1 taza de crenma \n Sal")
            elif entradas == 2:
                print(" Ingredientes \n Cebolla grande \n Zanahorita medidas \n Caldo de verduras \n pimienta y sal \n")
            elif entradas == 3:
                print(" Ingredientes \n lechuga verde \n zanahoria \n tomate \n Maiz Dulce \n")
            elif entradas == 4:
                print(" Ingredientes \n Esparragos \n Leche Evaporada \n 1 lata de Crema \n Cebolla y Sal")
        elif adm == 2:
            plato_fuerte = int(input("1-Casado de pollo \n 2-Casado de pescado \n 3-Casado de chuleta \n 4-Arroz con camarones \n"))
            if plato_fuerte == 1:
                print(" Ingredientes \n Arroz \n Frijoles \n Pollo \n Ensalada \n Vegetales")
            elif plato_fuerte == 2:
                print(" Ingredientes \n Arroz \n Frijoles \n Pescado \n Ensalada \n Vegetales")
            elif plato_fuerte == 3:
                print(" Ingredientes \n Arroz \n Frijoles \n Chuleta \n Ensalada \n Vegetales")
        elif adm == 3:
            postre = int(input("1-Mouse de limon \n 2- Mouse de fresa \n  3- Tarta de piña \n"))
            if postre ==1:
                print(" Ingredientes \n Leche condensada \n Jugo de limon \n Galleta Vainilla \n Mantequilla\n")
            elif postre ==2:
                print(" Ingredientes \n Leche condensada \n Fresas \n Galleta Vainilla \n Mantequilla\n")
            elif postre ==3:
                print(" Ingredientes \n Harina \n Azucar blanca \n Huevos \n Leche fria \n")
        elif adm == 4:
            bebida = int(input("1-Limonada de Hierba buena \n 2-Te Frio \n 3-Te melocoton \n 4-Te chai \n"))
            if bebida == 1:
                print(" Limon \n Hierba buena \n Agua y Sal \n Hielo")
            elif bebida == 2:
                print(" Te \n Limon \n Agua \n Hielo")
            elif bebida == 3:
                print(" Te \n melocoton \n Agua \n Hielo")
            elif bebida == 4:
                print(" Te Chai \n Agua \n Hielo")
        else:
            print(adm)
#x += menu_principal

"""Registro del cliente: Si el cliente no se encuentra registrado aún, deberá ingresar
su correo electrónico, nombre completo y fecha de nacimiento, así como la
información de su tarjeta de crédito, fecha de vencimiento y código de seguridad."""
if identificacion == 2:
    registro =int(input("1-Iniciar sesion \n2-Registrarse"))
    Iniciar = 1
    Registrarse = 2
    if registro == 2:
        correo = input("Correo electrónico: ")
        nombre = input("Nombre completo: ")
        fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
        tarjeta = input("Número de tarjeta de crédito: ")
        vencimiento = input("Fecha de vencimiento de la tarjeta (MM/YY): ")
        codigo = input("Código de seguridad de la tarjeta: ")
        print("Cliente registrado")
        

prueba    
 hola           
