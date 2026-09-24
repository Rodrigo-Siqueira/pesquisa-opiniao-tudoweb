# Variaveis de controle
total_opiniao_excelente = 0
total_opiniao_ruim = 0

# Painel
print('-' * 60)
print('Pesquisa de Satisfação do Cliente - TudoWeb')
print('-' * 60)

for cliente in range(50):
    print(f"\n--- Entrevistado {cliente + 1} ---")

    # Entrada de Dados
    nome = input('Digite seu Nome: ').strip().upper()

    # Enquanto não for digitado a idade corretamente continue.
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            if idade > 0:
                break

            print('A idade deve ser maior que Zero.')
        except ValueError:
            print("Erro: Por favor, digite uma idade válida.")

    # Enquanto não for digitado a opinião corretamente continue.
    while True:
        print("\nQual sua opinião sobre nosso atendimento?")
        print('1: EXCELENTE')
        print('2: BOM')
        print('3: RUIM')
        try:
            opiniao = int(input('Digite: 1 - Excelente, 2 - Bom, 3 -Ruim: '))
            if opiniao in [1, 2, 3]:
                break

            print('Digite uma opinião que esteja entre: 1, 2 ou 3.')
        except ValueError:
            print("Erro: Por favor, digite uma opinião válida.")

    match opiniao:
        case 1:
            total_opiniao_excelente += 1
        case 3:
            total_opiniao_ruim += 1

# Painel de Saída
print('\n' + '*' * 60)
print("Resultado da Pesquisa")
print('*' * 60)
print(f"Total de respostas \"EXCELENTE\": {total_opiniao_excelente}")
print(f"Total de respostas \"RUIM\": {total_opiniao_ruim}")
print('*' * 60)

