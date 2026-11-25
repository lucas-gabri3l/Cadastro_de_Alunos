lista_de_alunos = []

#FUNÇÃO PARA CADASTRAR
def cadastro(lista_de_alunos):
    print("CADASTRO DE ALUNOS")
    while True:
        #Cria o dicionário com aluno = {}
        aluno = {}
        aluno["nome"] = (str(input("Digite o nome do aluno: "))).lower() #Atribui nome, idade e nota.
        aluno["idade"] = (int(input("Digite a idade do aluno: ")))
        while True:
            aluno["nota"] = (float(input("Digite a nota do aluno: ")))
            if aluno["nota"] >= 0 and aluno["nota"] <= 10:
                break
            else:
                print("Digite uma nota entre 0 e 10")
                continue
            
        lista_de_alunos.append(aluno) #Adiciona a uma lista esse dicionário do aluno.

        escolha=int(input("Você deseja adicionar mais um aluno? (1- Sim, 2- Não): ")) # Pergunta se quer sair ou não

        if escolha == 1:
            continue
        else:
            break

#FUNÇÃO PARA LISTAR TODOS OS ALUNOS
def lista(lista_de_alunos):
    print("LISTA DE ALUNOS")
        
    if len(lista_de_alunos) > 0: 
        for numero, alunos in enumerate (lista_de_alunos, start=1):
            print(f"{numero} - Aluno\n Nome: {alunos['nome'].title()}\n Idade: {alunos['idade']}\n Nota: {alunos['nota']}\n")
    else:
        print("Não há nenhum aluno cadastrado!")

#FUNÇÃO PARA BUSCAR UM ALUNO
def busca(lista_de_alunos):
    print("BUSCA DE ALUNOS")

    nome_buscado = str(input("Digite o nome do Aluno que você procura?\nAluno: ")).strip().lower()
    encontrou = False

    for aluno in lista_de_alunos:
        if aluno["nome"].strip().lower() == nome_buscado:
            print(f"Aluno Encontrado\n Nome: {aluno['nome'].title()}\n Idade: {aluno['idade']}\n Nota: {aluno['nota']}\n")
            encontrou = True
            break
    if not encontrou:
            print("Aluno não está no sistema.")

#FUNÇÃO PARA REMOVER ALUNO
def remover(lista_de_alunos):
    print("REMOVER ALUNO")
    aluno_removido = input("Digite o nome do aluno que você deseja remover!\n").strip().lower()
    encontrou = False

    for aluno in lista_de_alunos:
        if aluno["nome"].strip().lower() == aluno_removido:
            lista_de_alunos.remove(aluno)
            encontrou = True
            print("Aluno Removido!")
            break
    if not encontrou:
        print("O Aluno não faz parte do Sistema!")

#FUNÇÃO PARA VER A MÉDIA GERAL DAS NOTAS
def media_geral(lista_de_alunos):
    print("MÉDIA GERAL DAS NOTAS")
    for aluno in lista_de_alunos:


while True: 
    funcionalidades = int(input("Digite o que você quer fazer!\n 1- Adicionar aluno\n 2- Listar todos os alunos\n 3- Buscar aluno pelo nome\n 4- Remover aluno\n 5- Mostrar média geral das notas\n 6- Sair"))

    match funcionalidades:
        case 1:
            cadastro(lista_de_alunos)

        case 2:
            lista(lista_de_alunos)
            
        case 3:
            busca(lista_de_alunos)
            
        case 4:
            remover(lista_de_alunos)

        case 5:
            media_geral(lista_de_alunos)

        case 6:
            print("Você escolheu sair, até breve!")
            break
