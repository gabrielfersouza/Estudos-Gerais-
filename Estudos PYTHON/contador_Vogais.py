def contar_vogais(palavra):
    vogal = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogal:
            contador += 1
    return contador


palavra = str(input("Digite uma palavra:"))
resultado = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {resultado} vogais.")
