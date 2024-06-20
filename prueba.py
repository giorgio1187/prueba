sectores = ['centro', 'norte', 'sur']

pedidos = []

#registrar
def registrar_pedido():
    nombre = input("Ingrese nombre y apellido del cliente: ")
    direccion = input("Ingrese direccion de cliente: ")
    sector = input("Ingrese sector de la entrega (norte/ centro/ sur): ").lower()
    while sector not in sectores:
        print("Ingrese zona válida de envio y/o reparto")
        sector = input("Ingrese sector de la entrega (norte/ centro/ sur): ").lower()


    paq_peq = int(input("Ingrese cantidad de paquetes pequeños: "))
    while paq_peq <0 or paq_peq >15:
        print("Ingrese cantidad dentro del rango... ")
        paq_peq = int(input("Ingrese cantidad de paquetes pequeños: "))

    paq_med = int(input("Ingrese cantidad de paquetes medianos: "))
    while paq_med <0 or paq_med >15:
        print("Ingrese cantidad dentro del rango... ")
        paq_med = int(input("Ingrese cantidad de paquetes medianos: "))

    paq_gra = int(input("Ingrese cantidad de paquetes grandes: "))
    while paq_gra <0 or paq_gra >15:
        print("Ingrese cantidad dentro del rango... ")
        paq_gra = int(input("Ingrese cantidad de paquetes grandes: "))

    pedido = {
        'nombre': nombre,
        'direccion': direccion,
        'sector' : sector,
        'paq_peq' : paq_peq,
        'paq_med' : paq_med,
        'paq_gra' : paq_gra
    }

    pedidos.append(pedido)

#listar
def listar_pedido():
    print("Listar pedidos: ")
    for pedido in pedidos:
        print(f"Cliente: {pedido['nombre']}, Direccion: {pedido['direccion']}, Sector: {pedido['sector']}")
        print(f"Paq. Peq: {pedido['paq_peq']}, Paq. Med: {pedido['paq_med']}, Paq. Gra: {pedido['paq_gra']}")

#imprimir
def imprimir_ruta():
    sector = input("Ingrese el sector para entrega: (Norte/ Centro/ Sur): ").lower()
    for sector in sectores:
            print("Ruta impresa...")

'''with open(f"archivo_ruta{pedido}.txt", "w") as f:
        
        f.write(f"Cliente: {pedido['nombre']}, Direccion: {pedido['direccion']}, Sector: {pedido['sector']}\n")
        f.write(f"Paq. Peq: {pedido['paq_peq']}, Paq. Med: {pedido['paq_med']}, Paq. Gra: {pedido['paq_gra']}\n")'''


    



#main
def main():
    while True:
        print("+-----Bienvenido PaqExpress-----+")
        print("1. Registrar pedido. ")
        print("2. Listar los pedidos. ")
        print("3. Imprimir hoja de ruta. ")
        print("4. Salir del programa. ")

        opc = int(input("Ingrese opcion que desea ejecutar: "))

        if opc == 1 :
            registrar_pedido()
        elif opc == 2 :
            listar_pedido()
        elif opc == 3 :
            imprimir_ruta()
        elif opc == 4 :
            print("Saliendo del menu....")
            break
        else:
            print("Ingrese opcion válida: ")


if __name__ == '__main__':
    main()
