# importar funcao matematica para fazer contas
import math
math.sqrt(16)

# exercicio
peso1 = float(input ('Digite o peso da primeira nota: '))
nota1 = float(input ('Digite a primeira nota: '))
peso2 = float(input ('Digite o peso da segunda nota: '))
nota2 = float(input ('Digite a segunda nota: '))


notafinal = ((peso1 * nota1) + (peso2 * nota2)) / (peso1 + peso2)

print ('A nota final é: ',notafinal)
if notafinal <=5.0:
 print('Aluno Reprovado!')
else: 
 print('Aluno Aprovado!')

input('Aperte Enter para sair')
