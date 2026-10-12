opiniao_excelente = 0
opiniao_bom = 0
opiniao_ruim = 0

for i in range (1,11):
    nome = input("Digite o seu nome:")
    idade = int(input("Digite sua idade:"))
    print("Considere: 1 - Excelente; 2 - Bom; 3 - Ruim")
    opiniao = int(input("Qual é sua opinião sobre o atendimento:"))

    if opiniao == 1:
        opiniao_excelente = opiniao_excelente + 1
    elif opiniao == 2:
        opiniao_bom = opiniao_bom + 1
    elif opiniao == 3:
        opiniao_ruim = opiniao_ruim + 1
    else:
        print("Opção inválida! Sua resposta não foi contabilizada")


print("Quantidade de respostas 'Excelentes': ", opiniao_excelente)
print("Quantidade de respostas 'Bom': ", opiniao_bom)
print ("Quantidade de respostas 'Ruim': ", opiniao_ruim)