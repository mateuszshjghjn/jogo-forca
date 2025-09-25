# Definindo o nome do aluno no programa
nome_no_programa = "Joao Silva"

# Definindo o número máximo de tentativas
tentativas_max = 6
tentativas = 0

# Perguntando ao usuário qual modo deseja usar
print("Escolha o modo de verificação:")
print("1 - Digitar o nome completo")
print("2 - Verificar letra por letra")
modo = input("Digite 1 ou 2: ")

if modo == "1":
    # Modo 1: Verificar nome completo
    while tentativas < tentativas_max:
        # Solicitando o nome do usuário
        nome_digitado = input("Digite o nome do aluno: ")
        tentativas += 1

        # Verificando se os nomes são iguais
        if nome_no_programa.lower() == nome_digitado.lower():
            print("Parabéns! O nome digitado é igual ao nome do aluno no programa!")
            print("Você acertou em", tentativas, "tentativa(s)!")
            break
        else:
            print("O nome digitado é diferente do nome do aluno no programa.")
            print("Tentativas restantes:", tentativas_max - tentativas)

    # Verificando se as tentativas acabaram sem acerto
    if tentativas == tentativas_max and nome_no_programa.lower() != nome_digitado.lower():
        print("Você esgotou todas as", tentativas_max, "tentativas.")
        print("O nome no programa era:", nome_no_programa)

elif modo == "2":
    # Modo 2: Verificar letra por letra
    nome_digitado = ""
    print("Digite o nome letra por letra. Digite 'sair' para encerrar a tentativa atual.")
    
    while tentativas < tentativas_max:
        nome_digitado = ""  # Reinicia o nome digitado para cada tentativa
        tentativas += 1
        posicao = 0
        
        # Solicitando letras até o tamanho do nome ou até o usuário sair
        while posicao < len(nome_no_programa):
            letra = input(f"Digite a letra {posicao + 1} (ou 'sair' para encerrar a tentativa): ")
            if letra.lower() == "sair":
                break
            if len(letra) != 1:
                print("Por favor, digite apenas uma letra.")
                continue
            nome_digitado += letra
            posicao += 1

        # Verificando se o usuário saiu da tentativa
        if letra.lower() == "sair":
            print("Tentativa encerrada. Tentativas restantes:", tentativas_max - tentativas)
            continue

        # Verificando se o nome digitado está correto
        if nome_no_programa.lower() == nome_digitado.lower():
            print("Parabéns! O nome digitado é igual ao nome do aluno no programa!")
            print("Você acertou em", tentativas, "tentativa(s)!")
            break
        else:
             print("Modo inválido! Por favor, escolha 1 ou 2.")