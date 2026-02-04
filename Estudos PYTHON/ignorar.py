import json
import os
import sys

DATA_FILE = "alunos.json"

def carregar_alunos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_alunos(alunos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=2)

def ler_int(prompt, minimo=None, maximo=None):
    while True:
        try:
            v = int(input(prompt))
            if (minimo is not None and v < minimo) or (maximo is not None and v > maximo):
                raise ValueError
            return v
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def ler_float(prompt, minimo=None, maximo=None):
    while True:
        try:
            v = float(input(prompt))
            if (minimo is not None and v < minimo) or (maximo is not None and v > maximo):
                raise ValueError
            return v
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 7.5).")

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip()
    idade = ler_int("Digite a idade do aluno: ", minimo=0)
    nota = ler_float("Digite a nota do aluno (0-10): ", minimo=0.0, maximo=10.0)
    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    salvar_alunos(alunos)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for i, a in enumerate(alunos, 1):
        print(f"{i}. {a['nome']} - {a['idade']} anos - Nota: {a['nota']:.2f}")

def calcular_media(alunos):
    if not alunos:
        print("Nenhum aluno para calcular média.")
        return
    media = sum(a["nota"] for a in alunos) / len(alunos)
    print(f"Média da turma: {media:.2f}")

def buscar_aluno(alunos):
    nome = input("Digite o nome do aluno: ").strip()
    encontrados = [a for a in alunos if a["nome"].casefold() == nome.casefold()]
    if not encontrados:
        print("Aluno não encontrado.")
    else:
        for a in encontrados:
            print(f"{a['nome']} - {a['idade']} anos - Nota: {a['nota']:.2f}")

def menu():
    print(
        "\nAperte 1 para cadastrar um aluno"
        "\nAperte 2 para listar alunos"
        "\nAperte 3 para calcular a media dos alunos"
        "\nAperte 4 para buscar aluno pelo nome"
        "\nAperte 5 para sair\n"
    )
    return ler_int("Escolha: ", minimo=1, maximo=5)

def main():
    alunos = carregar_alunos()
    print("Bem vindo ao sistema :")
    try:
        while True:
            opc = menu()
            if opc == 1:
                cadastrar_aluno(alunos)
            elif opc == 2:
                listar_alunos(alunos)
            elif opc == 3:
                calcular_media(alunos)
            elif opc == 4:
                buscar_aluno(alunos)
            elif opc == 5:
                print("Saindo do sistema...")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo...") 
    finally:
        salvar_alunos(alunos)

if __name__ == "__main__":
    main()