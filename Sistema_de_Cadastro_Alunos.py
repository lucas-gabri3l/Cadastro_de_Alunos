funcionalidades = int(input("Digite o que você quer fazer!\n 1- Adicionar aluno\n 2- Listar todos os alunos\n 3- Buscar aluno pelo nome\n 4- Remover aluno\n 5- Mostrar média geral das notas\n 6- Sair"))

match funcionalidades:
    case 1:
        #Lista de Alunos
        print("CADASTRO DE ALUNOS")

        lista_de_alunos = []

        while True:
            #Cria o dicionário com aluno = {}
            aluno = {}
            aluno["nome"] = (str(input("Digite o nome do aluno: "))).lower() #Atribui nome, idade e nota.
            aluno["idade"] = (int(input("Digite a idade do aluno: ")))
            aluno["nota"] = (float(input("Digite a nota do aluno: ")))
            lista_de_alunos.append(aluno) #Adiciona a uma lista esse dicionário do aluno.

            escolha=int(input("Você deseja adicionar mais um aluno? (1- Sim, 2- Não): ")) # Pergunta se quer sair ou não

            if escolha == 1:
                continue
            else:
                break

    case 2:
        print("LISTA DE ALUNOS")
        
        if len(lista_de_alunos) > 0: 
            for numero, alunos in enumerate (lista_de_alunos, start=1):
                print(f"{numero} - Aluno\n Nome: {alunos['nome'].title()}\n Idade: {alunos['idade']}\n Nota: {alunos['nota']}\n")
        else:
            print("Não há nenhum aluno cadastrado!")
        
    case 3:
        print("BUSCA DE ALUNOS")

        nome_buscado = str(input("Digite o nome do Aluno que você procura?")).strip().lower()
        encontrou = False

        for aluno in lista_de_alunos:
            if aluno["nome"].strip().lower() == nome_buscado:
                print(f"Aluno Encontrado\n Nome: {aluno['nome'].title()}\n Idade: {aluno['idade']}\n Nota: {aluno['nota']}\n")
                encontrou = True
                break
        if not encontrou:
                print("Aluno não está no sistema.")
        
    case 4:

    case 5:

    case 6:
        print("Você escolheu sair, até breve!")
        break
