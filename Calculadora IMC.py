#Função para calcular o IMC
def calcular_imc (peso, altura):
    imc = peso / (altura **2)
    return imc

#Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif imc < 30:
        classificacao = "Peso adequado"
    elif imc < 35:
        classificacao = "Obesidade grau I"
    elif imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    return classificacao

#Solicitar ao usuário peso e altura
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

#Calcular e classificar o IMC
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

#Exibir o resultado e a classificação
print("Seu IMC é {:.2f}".format(imc))
print("Sua classificação é", classificacao)