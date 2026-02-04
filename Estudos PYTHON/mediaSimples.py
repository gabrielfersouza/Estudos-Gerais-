def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))


resul = media(nota1, nota2, nota3)

if(resul >= 6):
    print("Aprovado")
elif(resul < 6):
    print("Recuperaçao")

print(f"A media das suas notas e:{resul:.2f}")
