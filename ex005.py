print("/tJoão Papo-de-Pescador/n")

peso = float(input("Peso: "))
excesso = 0
multa = 0

if peso <= 50:
    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)
else:
    excesso = peso - 50
    multa = excesso * 4

    print("Excesso: %.2f" %excesso)
    print("Multa: %.2f" %multa)

#Aqui apenas colocamos a condição mediante ao peso seja menor ou igual a 50