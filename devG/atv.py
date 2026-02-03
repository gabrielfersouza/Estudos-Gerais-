alunos = []
menu = 0

print("Bem vindo ao sistema :")

while menu != 5:
    menu = int(input(
        "\nAperte 1 para cadastrar um aluno"
        "\nAperte 2 para listar alunos"
        "\nAperte 3 para calcular a media dos alunos"
        "\nAperte 4 para buscar aluno pelo nome"
        "\nAperte 5 para sair\n"
    ))

    if menu == 1:
        aluno = {
            "nome": input("Digite o nome do aluno: "),
            "idade": int(input("Digite a idade do aluno: ")),
            "nota": float(input("Digite a nota do aluno: "))
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif menu == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(aluno)

    elif menu == 3:
        if len(alunos) == 0:
            print("Nenhum aluno para calcular média.")
        else:
            soma = 0
            for aluno in alunos:
                soma += aluno["nota"]
            media = soma / len(alunos)
            print(f"Média: {media:.2f}")

    elif menu == 4:
        nome = input("Digite o nome do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"] == nome:
                print(aluno)
                encontrado = True

        if not encontrado:
            print("Aluno não encontrado.")

    elif menu == 5:
        print("Saindo do sistema...")

    else:
        print("Opção inválida!")











