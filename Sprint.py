
import csv
import os


cadastro = {}

sair = False

def salvar_cadastro():
    
    csv_path = os.path.join(os.getcwd(), 'Pasta1.csv')
    
    
    file_exists = os.path.isfile(csv_path)
    
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Nome', 'Idade', 'Produto', 'Empresa Contratante'], delimiter=';')
        
        if not file_exists:
            writer.writeheader()
        
        for entrada in cadastro.values():
            writer.writerow(entrada)
    print("Dados salvos com sucesso no arquivo Pasta1.csv")




def carregar_cadastro():
    global cadastro
    try:
        with open('Pasta1.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader, start=1):
                cadastro[f"Entrada {i}"] = {
                    'Nome': row['Nome'],
                    'Idade': row['Idade'],
                    'Produto': row['Produto'],
                    'Empresa Contratante': row['Empresa Contratante']
                }
    except FileNotFoundError:
        cadastro = {}

def imprimir_cadastro_csv():
    try:
        with open('Pasta1.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            print("--------------------------------------------------------------------")
            print("| Nome                    | Idade | Produto                     | Empresa Contratante")
            print("--------------------------------------------------------------------")
            for row in reader:
                print(f"| {row['Nome']:<15}   | {row['Idade']:<5} | {row['Produto']:<25}    | {row['Empresa Contratante']}")
            print("--------------------------------------------------------------------")
    except FileNotFoundError:
        print("O arquivo cadastro.csv não foi encontrado.")

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
            salvar_cadastro() 
            return inicio()
        else:
            print("Muito Obrigado pela preferência! Volte sempre")
            sair = True
            salvar_cadastro()
            SystemExit()


    #READ
    elif escolha == 2:
        imprimir_cadastro_csv()
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
                    salvar_cadastro()
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
                    salvar_cadastro()
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
                salvar_cadastro()
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

