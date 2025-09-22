# Programa: CalculoDescuentoPython
# Autor: ARTURO GEOVANNY CHALACAN PASPUEL
# Descripción: Calcula el descuento en compras y muestra el monto final a pagar.

def calcular_descuento(monto_compra, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    Parámetros:
        monto_compra (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: Monto del descuento calculado.
    """
    descuento = monto_compra * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primer caso: solo monto (descuento por defecto 10%)
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1

    print("----- Compra 1 -----")
    print(f"Monto de la compra: ${monto1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${total1:.2f}\n")

    # Segundo caso: monto con porcentaje personalizado (15%)
    monto2 = 350.0
    descuento2 = calcular_descuento(monto2, 15)
    total2 = monto2 - descuento2

    print("----- Compra 2 -----")
    print(f"Monto de la compra: ${monto2:.2f}")
    print(f"Descuento aplicado (15%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${total2:.2f}")
