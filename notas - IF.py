nome = input("Insira o nome: ")
#nota1 = float(input("Insira a nota da primeira nota: "))
#nota2 = float(input("Insira a nota da segunda nota: "))
#falta = int(input("Insira o total de faltas: "))
valida_nota1 = False
valida_nota2 = False
valida_falta = False

while valida_nota1 == False:
    nota1 = input("Insira a primeira nota: ")
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print("Nota deve ser maior ou igual a 0 e menor ou igual a 10.")
        else:
            valida_nota1 = True
    except:
        print("Dado inválido. Favor inserir apenas números. Para decimais, separar com '.'")

while valida_nota2 == False:
    nota2 = input("Insira a segunda  nota: ")
    try:
        nota2 = float(nota2)
        if nota2 < 0  or nota2 > 10:
            print("Nota deve ser maior ou igual a 0 e menor ou igual a 10.")
        else:
            valida_nota2 = True
    except:
        print("Dado inválido. Favor inserir apenas números. Para decimais, separar com '.'")

while valida_falta == False:
    falta = input("Insira o total de faltas: ")
    try:
        falta = int(falta)
        if falta < 0 or falta > 20:
            print("Falta deve ser maior ou igual a 0 e menor ou igual a 10.")
        else:
            valida_falta = True
    except:
        print("Dado inválido. Favor inserir apenas números.")


nota_final = (nota1 + nota2) / 2

presenca = (falta * 100) / 20

print('Nome: ', nome)
print('Nota Final: ', nota_final)
print('Porcentagam de Assiduidade: ', str(presenca)+'%')

              
if falta >= 14:
    print("Reprovado por falta.")
elif falta < 14 and nota_final < 6:
    print("Reprovado por nota.", nota_final)
elif nota_final >= 6:
    print("Aprovado!")

