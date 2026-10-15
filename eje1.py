tienda = {
    "acción": ["Escape de la prueba de química","Escape de la escuela","Escape de la prueba de programacion"],
    "ciencia ficción": ["RoboBob"],
    "terror": ["La maldición de la escuela técnica"]
}
biblioteca={}
print("BIENVENIDO A LA CONSOLA ETec STATION")
print("ESTOS SON LOS NUEVOS JUEGOS:")
print("-----LISTA DE JUEGOS------")
for genero,juego in tienda.items():
    print(genero,":",juego)
while True:
    menu={
        1:"Comprar juego",
        2:"Ingrese un juego",
        3:"Salir"
    }
    print("------MENÚ-----")
    for key, values in menu.items():
        print(key,":",values)
    op=int(input("Ingrese la opción que desea:"))
    if op == 1:
        elec=input("Ingrese el género del juego que desea comprar:")
        if elec in tienda:
            cont=0
            nombre=""
            for elem in cont:
                print(f"{cont} : {elem}")
                cont =cont + 1
            elec1=int(input("Ingrese el número de juego que quiera:"))
            cont1=0
            biblioteca[cont1]=elec1
        else:
            print("El género no está en la tienda")
    elif op==2:
        agregar=input("Ingrese el género del juego que quiere agregar:")
        if agregar in tienda:
            tienda[key].append(agregar)
            print("Juego agregado correctamente")
            
        else:
            print("El género no está en la lista")
    elif op==3:
        print("Gracias por usar la consola :)")
        break
        