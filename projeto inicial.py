# Lista de Tarefas
tarefas = []

def mostrar_tarefas():
    if not tarefas:
        print("\nNão há tarefas pendentes.")
    else:
        print("\nTarefas Pendentes:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")

def adicionar_tarefa():
    descricao = input("\nDigite a descrição da tarefa: ")
    tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def concluir_tarefa():
    mostrar_tarefas()
    if tarefas:
        try:
            indice = int(input("\nDigite o número da tarefa concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]['concluida'] = True
                print(f"Tarefa '{tarefas[indice]['descricao']}' marcada como concluída.")
            else:
                print("Número de tarefa inválido!")
        except ValueError:
            print("Por favor, insira um número válido.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Concluir Tarefa")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_tarefas()
        elif escolha == '2':
            adicionar_tarefa()
        elif escolha == '3':
            concluir_tarefa()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
