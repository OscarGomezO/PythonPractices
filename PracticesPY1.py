var = int(input("Por favor ingrese el valor de la cuenta: "))

descuento = ""

if var <= 50:
    monto_final = var - (var * 0.0)
    descuento = 0
elif var <= 100:
    monto_final = var - (var * 0.10)
    descuento = 10
elif var <= 200:
    monto_final = var - (var * 0.20)
    descuento = 20
else:
    monto_final = var - (var * 0.30)
    descuento = 30

print("\n Monto de consumo: ", var, "$" )
print("--Porcentaje de descuento aplicado: ", descuento, "%")
print("--Monto final: ", monto_final, "$")