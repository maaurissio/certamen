from os import system
from funciones import *
system("cls")

pedidos = [{
    "ID pedido": 56348,
    "Nombre": "Mauricio",
    "Apellido": "Gajardo",
    "Direccion": "Coronel 1067",
    "Sector": "Concepción",
    "Disp.6lts": 5,
    "Disp.10lts": 2,
    "Disp.20lts": 1
}]

sectores = ("Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro")

def imprimir_ruta(pedidos):
    system("cls")
    sector_buscado = input("Ingrese un sector para imprimir (Concepción, Chiguayante, Talcahuano, Hualpén, San Pedro): ")
    if sector_buscado in sectores:
        for pedido in pedidos:
            archivo = open(f"pedido{pedido["Sector"]}.csv", "w")
            archivo.write("IDpedido;Nombre;Apellido;Direccion;Sector;Disp.6lts;Disp.10lts;Disp.20lts")
            archivo.write(f"\n{pedido["Nombre"]};{pedido["Apellido"]};{pedido["Direccion"]};{pedido["Sector"]};{pedido["Disp.6lts"]};{pedido["Disp.10lts"]};{pedido["Disp.20lts"]}\n")
            archivo.close()
    else:
        print("Sector no valido")


while True:
    print("""
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
        """)
    op = input("Ingrese una opcion: ")
    match op:
        case"1":
            registro_pedido(pedidos)
        case"2":
            listar(pedidos)
        case"3":
            imprimir_ruta(pedidos)
        case"4":
            buscar_pedido(pedidos)
        case"0":
            break
        case other:
            print("Opcion invalida, por favor ingrese una opcion valida")