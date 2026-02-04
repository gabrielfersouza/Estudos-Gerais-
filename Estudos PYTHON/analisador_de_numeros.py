def analiNum(lista):
    soma = sum(lista)
    media = soma / len(lista)
    maior = max(lista)
    menor = min(lista)
    return soma , media , maior , menor




lista = []
qt = input("Quantos numeros voce deseja analisar?")
for i in range(int(qt)):
    num = float(input("Digite o numero:"))
    lista.append(num)    
resul = analiNum(lista)
print(f"Os resultados da analise sao:\nSoma: {resul[0]}\nMedia: {resul[1]}\nMaior numero: {resul[2]}\nMenor numero: {resul[3]}")