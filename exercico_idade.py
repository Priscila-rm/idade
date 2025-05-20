#voce foi contratado para criar um programa  de verificaçao de idade para clientes que consumem bebida alcoolica

#passo 1. nome do cliente 
nome= input("digite o seu nome: ")

#passo 2. idade 
idade = int(input('digite a sua idade: '))

#if é SE em pt-br e else é SENÃO
if idade >= 18:
    print(nome, 'autorizado, maior de idade', idade)
else:
    print(f'{nome} não autorizado, menor de idade : {idade} anos')