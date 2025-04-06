def menu():
  voltarMenuPrincipal = "s"
  while voltarMenuPrincipal == "s":
        opçao = input(''' 
        ==============================================================
                                   projeto agenda em python
    menu:
    [1]CADASTRAR CONTATO
    [2]LISTAR CONTATO 
    [3]DELEATAR CONTATO
    [4]BUSCAR CONTATO PELO NOME
    [5]ATUALIZAR CONTATO
    [6]SAIR
        ==============================================================
    ESCOLHA UMA OPÇAO ACIMA: 
    ''')
        if opçao == "1":
            CadastrarContato()
        elif opçao =="2":
            listarContato()
        elif opçao =="3":
            deletarContato()
        elif opçao =="4":
            buscarContatopeloNome()
        elif opçao == "5":
            atualizarContato()
        else:
            sair()
        voltarMenuPrincipal = input('Deseja voltar ao menu principal ? (s/n)  ').lower()

def atualizarContato():
    nomeDeletado = input("Digite o nome para ser Atualizado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)

    idContato = input('Escolha o ID do seu contato atualizado: ')
    nome = input('Escreva o nome do seu contato atualizado : ')
    telefone = input('Escreva o telefone do contato atualizado : ')
    email = input('Escreva o email do contato atualizado : ')
    try:
        agenda = open("agenda.txt", "a")
        dados = f"{idContato};{nome};{telefone};{email} \n"
        agenda.write(dados)
        agenda.close()
        print('contato atualizado com sucesso!!!')
    except:
        print('erro na gravação do contato!')


def CadastrarContato():
    idContato = input('Escolha o ID do seu contato: ')
    nome = input('Escreva o nome do seu contato: ')
    telefone = input('Escreva o telefone do contato: ')
    email = input('Escreva o email do contatO: ')
    try:
        agenda = open("agenda.txt", "a")
        dados = f"{idContato};{nome};{telefone};{email} \n"
        agenda.write(dados)
        agenda.close()
        print('contato gravado com sucesso!!!')
    except:
        print('erro na gravação do contato!')

def listarContato():
    agenda = open("agenda.txt","r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!!')
    listarContato()

def buscarContatopeloNome():
    nome = input(f'digite o nome a ser procurado: ').lower()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].lower():
            print(contato)
    agenda.close()
def  sair():
    print(f'ate mais....!!')
    exit()

def main():

    menu()

main()


