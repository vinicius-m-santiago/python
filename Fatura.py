repetir = 's'
fatura = []
total = 0
valida_preco = False

while repetir == 's':
    produto = input("Nome do produto: ")

    while valida_preco == False:
        preco = input("Preço do produto: ")
        try:
            preco = float(preco)

            if preco <= 0:
               print("Preço deve ser maior ou igual a 0.")
            else:
                valida_preco = True

        except:
            print("Dado inválido. Favor inserir apenas números. Para decimais, separar com '.'")
    
    
    fatura.append([produto,preco])
    total += preco
    valida_preco = False
    repetir = input("Deseja comprar algo mais? (s/n): ").lower()

for i in fatura:
        print("Produto:", i[0],"- Preço:", i[1])
print("Valor total da compra é:", total)

   
   

