# Exercicio Dicionario

colors ={"vermelho": "red","azul": "blue","verde": "green", "preto": "black"}



cor = input("Insira o nome da cor que será traduzida: ").lower()


print(colors.get(cor, "Essa cor não está listada"))
