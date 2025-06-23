# Inicialización de las variables
dinero = float(input("Cuanto dinero tiene: "))
dineroini = dinero
total = 0
pedido = []
Pizza_Hawaiana = 15.2
Pizza_Pollo = 10.3
Pizza_Champiniones = 17.35
Queso = 5.4
Jamon = 8.1
Pina = 6.8

# Mensaje inicial
print("Pizzería el Mono")

# Primera parte: Selección de pizza
while True:
    print(f"Pizza Hawaiana cuesta {Pizza_Hawaiana} USD")
    print(f"Pizza de Pollo vale {Pizza_Pollo} USD")
    print(f"Pizza de Champiñones vale {Pizza_Champiniones} USD")
    print("¿Qué desea ordenar?")
    
    eleccion = int(input("Seleccione el tipo de pizza (1, 2, 3): "))
    
    match eleccion:
        case 1:
            print(f"Haz elegido Pizza Hawaiana. Total a pagar {Pizza_Hawaiana} USD.")
            total += Pizza_Hawaiana
            dinero -= Pizza_Hawaiana
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Pizza Hawaiana {Pizza_Hawaiana}")
            break
        case 2:
            print(f"Haz elegido Pizza Pollo. Total a pagar {Pizza_Pollo} USD.")
            total += Pizza_Pollo
            dinero -= Pizza_Pollo
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Pizza Pollo {Pizza_Pollo}")
            break
        case 3:
            print(f"Haz elegido Pizza Champiñones. Total a pagar {Pizza_Champiniones} USD.")
            total += Pizza_Champiniones
            dinero -= Pizza_Champiniones
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Pizza Champiñones {Pizza_Champiniones}")
            break
        case _:
            print("Opción Incorrecta, seleccione una opción del 1 al 3.")

# Segunda parte: Selección de ingredientes extra
while True:
    print(f"1. Queso {Queso} USD")
    print(f"2. Jamon {Jamon} USD")
    print(f"3. Pina en cuadros {Pina} USD")
    print("4. No deseo agregar ingredientes adicionales")
    print("¿Qué desea ordenar?")

    eleccion_ingrediente = int(input("Seleccione ingrediente extra que desea (1, 2, 3, 4): "))
    
    match eleccion_ingrediente:
        case 1:
            print(f"Haz elegido agregar Queso extra. Total a pagar {Queso} USD.")
            total += Queso
            dinero -= Queso
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Queso {Queso}")
            break
        case 2:
            print(f"Haz elegido agregar Jamón extra. Total a pagar {Jamon} USD.")
            total += Jamon
            dinero -= Jamon
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Jamon {Jamon}")
            break
        case 3:
            print(f"Haz elegido agregar Piña en cuadros. Total a pagar {Pina} USD.")
            total += Pina
            dinero -= Pina
            print(f"Te queda {round(dinero, 2)} USD.")
            pedido.append(f"Pina en cuadros {Pina}")
            break
        case 4:
            print("No se agregarán ingredientes extra. Muchas gracias.")
            break
        case _:
            print("Opción Incorrecta, seleccione una opción del 1 al 4.")

# Verificación del dinero
if total <= dineroini:
    print("\nFactura de venta")
    print(f"Su pedido ha costado {total} USD.")
    print(f"Su cambio es de {round(dineroini - total, 2)} USD.")
    for p in pedido:
        print(f"{p}")
    print("Gracias por su compra")
else:
    print("El dinero no te alcanza, ingresa más dinero.")