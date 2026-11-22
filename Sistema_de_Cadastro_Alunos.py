funcionalidades = int(input("Digite o que você quer fazer!\n 1- Adicionar aluno\n 2- Listar todos os alunos\n 3- Buscar aluno pelo nome\n 4- Remover aluno\n 5- Mostrar média geral das notas\n 6- Sair"))

match funcionalidades:
    case 1:
        #Lista de Alunos
        print("CADASTRO DE ALUNOS")

        lista_de_alunos = []

        while True:
            #Cria o dicionário com aluno = {}
            aluno = {}
            aluno["nome"] = (str(input("Digite o nome do aluno: "))) #Atribui nome, idade e nota.
            aluno["idade"] = (int(input("Digite a idade do aluno: ")))
            aluno["nota"] = (float(input("Digite a nota do aluno: ")))
            lista_de_alunos.append(aluno) #Adiciona a uma lista esse dicionário do aluno.

            escolha=int(input("Você deseja adicionar mais um aluno? (1- Sim, 2- Não)")) # Pergunta se quer sair ou não

            if escolha == 1:
                continue
            else:
                break

    case 2:

    case 3:

    case 4:

    case 5:

    case 6:
        print("Você escolheu sair, até breve!")
        break
