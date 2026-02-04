def inverter_palavra(palavra):
    return palavra[::-1]

palavra = str(input("Digite uma palavra: "))
resultado = inverter_palavra(palavra)
print(f"A palavra invertida é: {resultado}")

