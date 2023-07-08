matriz_frutas = []
lista_frutas = []
for c in range (5):
    nome = str(input("Insira o nome da fruta: "))
    qntd = int(input("Insira a quantidade referênte a fruta: "))
    linha = [nome,qntd]
    matriz_frutas.append(linha)
print(matriz_frutas)
maiorqnt = 0.1
nome = ""
for linha in matriz_frutas:
    if linha [1] > maiorqnt:
        maiorqnt = linha [1]
        nome = linha [0]
        linha[1]
        lista_frutas.append(linha[1])
        soma = 0
    for total in lista_frutas:
        soma = soma + total
media = soma/len(matriz_frutas)
print("O/A",nome,"foi a fruta adquirida em maior quantidade, pois obteve",maiorqnt,"Und.")
print("A quantidade total de frutas foi: ",soma,"Und.")
print("A média geral foi de : ",media,"und.")