
def calc(num1, num2, op):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    return num1 / num2

  else:
    return 'Operação inválida'


num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
op = input("DIgite a operaçao(+,-,*,/):")


resultado = calc(num1,num2,op)

print(f"O resultado é:{resultado:.2f}")



