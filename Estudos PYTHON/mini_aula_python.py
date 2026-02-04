# ====================================================================
# 🐍 MINI AULA DE PYTHON - PARA INICIANTES
# ====================================================================

# ====================================================================
# 1️⃣ VARIÁVEIS E TIPOS DE DADOS
# ====================================================================

# Variáveis armazenam valores na memória
nome = "Gabriel"
idade = 25
altura = 1.75
ativo = True

print("=== EXEMPLO 1: Variáveis ===")
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}")

# Tipos de dados principais:
# - String (texto): "Olá"
# - Integer (número inteiro): 42
# - Float (número decimal): 3.14
# - Boolean (verdadeiro/falso): True, False

print("\n=== Tipos de dados ===")
print(f"Tipo de 'nome': {type(nome)}")
print(f"Tipo de 'idade': {type(idade)}")
print(f"Tipo de 'altura': {type(altura)}")


# ====================================================================
# 2️⃣ OPERAÇÕES MATEMÁTICAS
# ====================================================================

print("\n=== EXEMPLO 2: Operações Matemáticas ===")
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {potencia}")


# ====================================================================
# 3️⃣ ENTRADA DE DADOS (INPUT)
# ====================================================================

print("\n=== EXEMPLO 3: Entrada de Dados ===")
# input() captura dados do usuário como texto (string)
# int() converte para número inteiro
# float() converte para número decimal

# Descomente as linhas abaixo para testar:
# seu_nome = input("Qual é seu nome? ")
# seu_ano_nascimento = int(input("Em que ano você nasceu? "))
# print(f"Olá {seu_nome}! Você tem aproximadamente {2026 - seu_ano_nascimento} anos")


# ====================================================================
# 4️⃣ ESTRUTURAS CONDICIONAIS (IF/ELSE)
# ====================================================================

print("\n=== EXEMPLO 4: Condicionais ===")

nota = 7.5

if nota >= 9:
    print("Nota A - Excelente!")
elif nota >= 7:
    print("Nota B - Bom!")
elif nota >= 5:
    print("Nota C - Satisfatório")
else:
    print("Nota F - Reprovado")

# Comparações:
# == (igual)
# != (diferente)
# > (maior)
# < (menor)
# >= (maior ou igual)
# <= (menor ou igual)

# Operadores lógicos:
# and (e)
# or (ou)
# not (não)

idade = 18
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir ainda")


# ====================================================================
# 5️⃣ LISTAS (ARRAYS)
# ====================================================================

print("\n=== EXEMPLO 5: Listas ===")

frutas = ["maçã", "banana", "laranja", "uva"]
numeros = [10, 20, 30, 40, 50]

print(f"Lista de frutas: {frutas}")
print(f"Primeira fruta: {frutas[0]}")  # Índice começa em 0
print(f"Última fruta: {frutas[-1]}")   # Índice negativo

print(f"Total de frutas: {len(frutas)}")

# Adicionar e remover elementos
frutas.append("melancia")
print(f"Após adicionar melancia: {frutas}")

frutas.remove("banana")
print(f"Após remover banana: {frutas}")


# ====================================================================
# 6️⃣ LOOPS (REPETIÇÕES)
# ====================================================================

print("\n=== EXEMPLO 6: Loop FOR ===")

# Loop for - percorre lista
for fruta in frutas:
    print(f"Fruta: {fruta}")

print("\n=== Loop com range ===")

# range(inicio, fim, passo)
for i in range(1, 6):  # 1 até 5
    print(f"Número: {i}")

print("\n=== Loop WHILE ===")

contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1  # contador = contador + 1


# ====================================================================
# 7️⃣ FUNÇÕES
# ====================================================================

print("\n=== EXEMPLO 7: Funções ===")

# Função simples
def saudacao():
    print("Olá! Bem-vindo ao Python!")

saudacao()

# Função com parâmetros
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

meu_imc = calcular_imc(70, 1.75)
print(f"Seu IMC: {meu_imc:.2f}")

# Função com valor padrão
def criar_mensagem(nome, sobrenome="Silva"):
    return f"Olá {nome} {sobrenome}!"

print(criar_mensagem("João"))
print(criar_mensagem("Maria", "Santos"))


# ====================================================================
# 8️⃣ DICIONÁRIOS
# ====================================================================

print("\n=== EXEMPLO 8: Dicionários ===")

pessoa = {
    "nome": "Gabriel",
    "idade": 25,
    "cidade": "São Paulo",
    "profissao": "Programador"
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Adicionar novo campo
pessoa["email"] = "gabriel@email.com"
print(f"Pessoa completa: {pessoa}")


# ====================================================================
# 9️⃣ STRINGS - MANIPULAÇÃO DE TEXTO
# ====================================================================

print("\n=== EXEMPLO 9: Strings ===")

texto = "Python é incrível"

print(f"Texto em maiúscula: {texto.upper()}")
print(f"Texto em minúscula: {texto.lower()}")
print(f"Primeira letra maiúscula: {texto.capitalize()}")
print(f"Tamanho do texto: {len(texto)}")
print(f"Contém 'Python'?: {'Python' in texto}")

# Fatiar string (slicing)
print(f"Primeiras 6 letras: {texto[:6]}")


# ====================================================================
# 🎯 ATIVIDADES PRÁTICAS
# ====================================================================

print("\n\n" + "="*70)
print("🎯 ATIVIDADES PARA VOCÊ FAZER!")
print("="*70)

# ====================================================================
# ATIVIDADE 1: Calculadora Simples
# ====================================================================

print("\n📝 ATIVIDADE 1: Criar uma calculadora")
print("""
Crie uma função chamada 'calculadora' que:
- Receba 3 parâmetros: num1, num2, operacao
- operacao pode ser: '+', '-', '*', '/'
- Retorne o resultado da operação

Dica: Use if/elif para verificar qual operação fazer

Exemplo esperado:
calculadora(10, 5, '+')  # retorna 15
calculadora(10, 5, '*')  # retorna 50
""")

# Escreva sua solução abaixo:
def calculadora(num1, num2, operacao):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 2: Verificar Maior Idade
# ====================================================================

print("\n📝 ATIVIDADE 2: Verificar maioridade")
print("""
Crie uma função chamada 'verificar_idade' que:
- Receba um parâmetro: idade
- Retorne "Maior de idade" se idade >= 18
- Retorne "Menor de idade" se idade < 18

Exemplo esperado:
verificar_idade(20)  # retorna "Maior de idade"
verificar_idade(15)  # retorna "Menor de idade"
""")

# Escreva sua solução abaixo:
def verificar_idade(idade):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 3: Contar Vogais
# ====================================================================

print("\n📝 ATIVIDADE 3: Contar vogais em uma palavra")
print("""
Crie uma função chamada 'contar_vogais' que:
- Receba um parâmetro: palavra (string)
- Conte quantas vogais tem na palavra
- Retorne a quantidade

Dica: Use um loop para percorrer as letras
Dica: Vogais são: a, e, i, o, u

Exemplo esperado:
contar_vogais("python")  # retorna 1
contar_vogais("python")  # retorna 1
contar_vogais("aeiou")   # retorna 5
""")

# Escreva sua solução abaixo:
def contar_vogais(palavra):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 4: Listar Números Pares
# ====================================================================

print("\n📝 ATIVIDADE 4: Listar números pares")
print("""
Crie uma função chamada 'numeros_pares' que:
- Receba um parâmetro: numero
- Retorne uma lista com todos os números pares de 1 até numero
- Use um loop para isso

Exemplo esperado:
numeros_pares(10)  # retorna [2, 4, 6, 8, 10]
numeros_pares(5)   # retorna [2, 4]
""")

# Escreva sua solução abaixo:
def numeros_pares(numero):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 5: Inverter Palavra
# ====================================================================

print("\n📝 ATIVIDADE 5: Inverter uma palavra")
print("""
Crie uma função chamada 'inverter_palavra' que:
- Receba um parâmetro: palavra (string)
- Retorne a palavra de trás para frente

Dica: Use slicing de strings [::-1]

Exemplo esperado:
inverter_palavra("python")  # retorna "nohtyp"
inverter_palavra("ola")     # retorna "alo"
""")

# Escreva sua solução abaixo:
def inverter_palavra(palavra):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 6: Média de Notas
# ====================================================================

print("\n📝 ATIVIDADE 6: Calcular média de notas")
print("""
Crie uma função chamada 'calcular_media' que:
- Receba um parâmetro: notas (lista de números)
- Calcule a média das notas
- Retorne a média

Dica: Use sum() para somar e len() para contar

Exemplo esperado:
calcular_media([7, 8, 9])     # retorna 8.0
calcular_media([5, 6, 7, 8])  # retorna 6.5
""")

# Escreva sua solução abaixo:
def calcular_media(notas):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# ATIVIDADE 7: Dicionário de Produtos
# ====================================================================

print("\n📝 ATIVIDADE 7: Criar dicionário de produtos")
print("""
Crie um dicionário chamado 'produtos' com pelo menos 3 produtos.
Cada produto deve ter:
- Nome do produto (chave)
- Preço (valor)

Depois crie uma função 'total_carrinho' que:
- Receba um parâmetro: lista_produtos (lista de nomes)
- Some o preço de todos os produtos da lista
- Retorne o total

Exemplo esperado:
produtos = {"notebook": 3000, "mouse": 50, "teclado": 150}
total_carrinho(["notebook", "mouse"])  # retorna 3050
""")

# Sua solução aqui:
produtos = {
    # SUA SOLUÇÃO
}

def total_carrinho(lista_produtos):
    # SUA SOLUÇÃO AQUI
    pass


# ====================================================================
# 🎓 PRÓXIMOS PASSOS
# ====================================================================

print("\n\n" + "="*70)
print("🎓 PRÓXIMOS PASSOS PARA APRENDER MAIS")
print("="*70)
print("""
✅ Pratique as atividades acima
✅ Tente modificar os exemplos
✅ Quebre coisas e aprenda com os erros!

Conceitos que você pode estudar depois:
- Compreensões de lista (list comprehension)
- Exceções (try/except)
- Módulos e importações
- Orientação a Objetos (classes)
- Leitura e escrita de arquivos
- Bibliotecas populares (numpy, pandas, requests)

Dica: Use a função print() para debugar e entender o que seu código faz!
""")

print("\n" + "="*70)
print("💪 BOA SORTE NOS SEUS ESTUDOS!")
print("="*70)
