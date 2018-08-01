#execricio nascimento

meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")

data_aniversario = input("Insira a data do aniversario: ")

mes_aniversario = data_aniversario[3:5]

mes_aniversario_num = int(mes_aniversario) - 1
        
print("Seu aniversário é no mês: ", meses[mes_aniversario_num])
