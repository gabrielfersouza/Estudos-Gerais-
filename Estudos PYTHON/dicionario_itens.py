produto = {
   "noteBook" : 3000,
   "carregador" : 50,
   "mouse" : 120,
   "teclado" : 200
}

def total_carrinho(Produtos):
    total = 0
    for produto in Produtos:
        total += Produtos[produto]
  
    return total
print(f"O total do carrinho é: R$ {total_carrinho(produto)}")
