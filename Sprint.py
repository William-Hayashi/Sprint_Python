import pickle

sair = False
# Função para salvar o dicionário em um arquivo
def salvar_cadastro():
    with open('cadastro.pkl', 'wb') as f:
        pickle.dump(cadastro, f)

# Função para carregar o dicionário de um arquivo
def carregar_cadastro():
    global cadastro
    try:
        with open('cadastro.pkl', 'rb') as f:
            cadastro = pickle.load(f)
    except FileNotFoundError:
        cadastro = {}


def inicio():
    linha = "____________________________________________________________________\n"
    print(linha)
    print("Bem Vindo a KeepForce o que deseja fazer?")
    print("1 - Deseja criar um novo cadastro?")
    print("2 - Deseja mostrar os cadastros existentes?")
    print("3 - Deseja atualizar os cadastros?")
    print("4 - Deseja excluir um cadastro?")
    print("5 - Sair")
    print(linha)
    meio()


def meio():
    global sair
    while not sair:
        try: 
            global escolha
            escolha = int(input("Digite o número que deseja:"))
            print("O número escolhido foi {}. Executando...\n\n".format(escolha))
            trabalhando_dados(escolha)
        except ValueError:
            print("Oopss! O valor não é um número. Tente de novo")
    
    
cadastro = {}

def trabalhando_dados(escolha):
    global cadastro,sair

    #CREATE
    if escolha == 1:        
        num_entradas = int(input("Digite o número de entradas que deseja adicionar: "))
        for i in range(num_entradas):
            entrada = {}
            for campo in ['Nome', 'Idade', 'Produto', 'Empresa Contratante']:
                valor = input(f"Digite o valor para a entrada {i+1}({campo}): ")
                entrada[campo] = valor
            cadastro[f"Entrada {i+1}"] = entrada
        print("---------------------------------RESULTADO-----------------------------\nCadastro atualizado:\n", cadastro)
        print("")

        repetir = input("Deseja fazer mais alguma ação? Sim ou Não: ")
        repetir = repetir.upper()
        if repetir == "SIM":
            return inicio()
        else:
            print("Muito Obrigado pela preferência! Volte sempre")
            sair = True
            salvar_cadastro()
            SystemExit()


    #READ
    elif escolha == 2:
        for key in cadastro:
            print(f'{key}: {cadastro[key]}')
        repetir = input("Deseja fazer mais alguma ação? Sim ou Não: ")
        repetir = repetir.upper()
        if repetir == "SIM":
            return inicio()
        else:
            print("Muito Obrigado pela preferência! Volte sempre")
            sair = True
            salvar_cadastro()
            SystemExit()


    # UPDATE
    elif escolha == 3:

        escolha_user = input("Você deseja alterar tudo(T) ou somente um item(U), escolha entre essas duas (U/T):")
        escolha_user = escolha_user.upper()
        update_entrada = (input("\nEscolha a entrada que deseja mudar(Digite 'Entrada X'): "))
        

        if escolha_user == 'U':
            update_item = input("Escolha o item que deseja mudar(Nome, Idade, Produto, Empresa Contratante): ")
            new_value = input("Escreva a nova mudança: ")
            if update_entrada in cadastro and update_item in cadastro[update_entrada]:
                cadastro[update_entrada][update_item] = new_value
                print ("---------------------------------RESULTADO-----------------------------\nCadastro atualizado:", cadastro)
                repetir = input("\nDeseja fazer mais alguma ação? Sim ou Não: ")
                repetir = repetir.upper()
                if repetir == "SIM":
                    return inicio()
                else:
                    print("\nMuito Obrigado pela preferência! Volte sempre")
                    sair = True
                    salvar_cadastro()
                    SystemExit()
            else: 
                print("\nNão foi possível achar tente novamente")
                return inicio()
            
        elif escolha_user == 'T':
            if update_entrada in cadastro:
                for campo in ['Nome', 'Idade', 'Produto', 'Empresa Contratante']:
                    valor = input(f"Digite o valor para a entrada ({campo}): ")
                    cadastro[update_entrada][campo] = valor
                    print("---------------------------------RESULTADO-----------------------------\nCadastro atualizado:", cadastro)
                repetir = input("\nDeseja fazer mais alguma ação? Sim ou Não: ")
                repetir = repetir.upper()
                if repetir == "SIM":
                    return inicio()
                else:
                    print("\nMuito Obrigado pela preferência! Volte sempre")
                    sair = True
                    salvar_cadastro()
                    SystemExit()  
            else:
                print("\nA entrada selecionada não existe. Tente novamente.")
                return inicio()

    #DELETE
    elif escolha == 4:
        excluir_entrada = input("Qual entrada deseja entrar para excluir um item (Entrada X): ")
        if excluir_entrada in cadastro:
            try:
                del cadastro[excluir_entrada]
                print("Excluído com sucesso")
                print("---------------------------------RESULTADO-----------------------------\nCadastro atualizado:", cadastro)
            except KeyError:
                print("Entrada não encontrada! Tente novamente")
                return inicio()
        repetir = input("Deseja fazer mais alguma ação? Sim ou Não: ")
        repetir = repetir.upper()
        if repetir == "SIM":
            return inicio()
        else:
            print("Muito Obrigado pela preferência! Volte sempre")
            sair = True
            salvar_cadastro()
            SystemExit()

            

    elif escolha == 5:
        print("Opção escolhida sair do menu. Encerrando...")
        sair = True
        salvar_cadastro()
        SystemExit()
    else:
        print("Tente Novamente, digite um número válido")
        return meio()
    

if __name__ == "__main__":
    
    carregar_cadastro()
    inicio()

