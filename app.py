# Adicionar tarefas 
# Lista de tarefas
# Marcar como concluídas
# Excluir tarefas
# Sair

import json
import os

#lista de tarefas serão armazenadas
tarefas = []

# Caminho do aquivo onde vamos salvar as tarefas
ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva as tarefas no arquivo JSON."""
    with open(ARQUIVO, 'w', encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)
        
def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    data = input("Digite a data da tarefa (dd/mm/aaaa): ")
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data": data,
        "concluida": False
    }   
    
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")
    
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i + 1}. {tarefa['titulo']} - {status} - {tarefa['data']}")
    print("")
    
def concluir_tarefas():
    listar_tarefas()
    
    try:
        indice = int(input("Digite o número da tarefa a ser concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída com sucesso!")
        else:
            print("Tarefa inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        
def excluir_tarefa():
    listar_tarefas()
    
    try:
        indice = int(input("Digite o número da tarefa a ser excluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print("Tarefa excluída com sucesso!")
        else:
            print("Tarefa inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            concluir_tarefas()
        elif opcao == '4':
            excluir_tarefa()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            
terfas = carregar_tarefas()
menu()