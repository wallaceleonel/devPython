def validar_idade (idade):
    if idade < 18:
       print('sorry,voce nao pode tirar a carta,',nome)
       return False
    else:
       print('\n OTIMO podemos processeguir,',nome)
       return True

def escolher_carta():
    print("digite uma das opcoẽs abaixo:")
    print("1-carro\n2 -moto\n3 -carro e moto")
    return int(input())


def calcular_preco(escolha):
    valor_carro = 1500
    valor_moto = 1000
    if escolha ==1:
        return valor_carro
    elif escolha ==2:
        return valor_moto
    else:
        return valor_moto+valor_carro

def desconto(valor):
    return valor -(valor * 0.10)

    nome = input('digite seu nome:')   
idade =int(in  put('digite sua idade'))

if validar_idade(idade):
    escolha = escolher_carta()

    print ('\nPerfeito! Vou calcular o valor')
    valor= calcular_preco(escolha)

    print('\n '+nome,'o valor total e de ',valor,'reais')
   
    print('mas vou ver com o meu gerente se posso da um desconto....')
    valor = desconto(valor)


    print('\ncom desconto consigo fazer por',valor,'reais.')

    print('te insteressa?\n1 -sim\n2 -não')
    interesse = int(input())
   
    if interesse == 1:
        print('\nPerfeito!Começaremos amanha')
    else:
        print('\nTudo bem:(\n me avise se mudar de ideia ')
