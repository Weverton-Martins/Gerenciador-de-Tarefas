#Este aplicativo permitirá que você:
'''
Adicione novas tarefas com título, descrição e data de conclusão.
● Listar todas as tarefas, categorizando-as como pendentes ou concluídas.
● Marcar tarefas como concluídas.
● Remover tarefas.
● Salvar e carregar tarefas de um arquivo para garantir persistência de dados entre
execuções.
● Pesquisar tarefas por título ou descrição.
● Ordenar tarefas por data de conclusão.'''

import json
import os
from datetime import datetime

# Estrutura lógica de uma tarefa, como serão os dicionarios armazenados
'''
tarefa = {
    "id": 1,
    "titulo": "Estudar Python",
    "descricao": "Focar em funções e dicionários",
    "data_conclusao": "25/05/2026",
    "concluida": False  # Toda tarefa nova nasce como False (pendente)
}'''

lista_tarefas = []

#Primeiro adicionar tarefa
def adicionar_tarefa():
    print('Adicione a tarefa desejada:')
    tarefa = input('Tarefa: ')
    desc = input('Descrição: ')
    data = input('Data de Conclusão (formato DD/MM/YYYY): ')
    data_formatada = datetime.strptime(data, "%d/%m/%Y")#Formatar a data
    id = len(lista_tarefas) +1
    
    #Criando o dicionario com os valores solciitados
    dicionario_tarefa = {
        'id': id,
        'tarefa': tarefa,
        'descrição': desc,
        'data_conclusão': data_formatada,
        'concluida': False
    }
    #adicionando o dicionario na lista
    lista_tarefas.append(dicionario_tarefa)

def listar_tarefas():
    print('Lista de tarefas:')
    for lista in lista_tarefas:
        data_bonita = lista['data_conclusão'].strftime("%d/%m/%Y")

        print(f'id: {lista["id"]} | status: {'Concluida' if lista.get("concluida") else "Pendente"}')
        print(f'Tarefa: {lista["tarefa"]}')
        print(f'Descrição: {lista["descrição"]}')
        print(f'Data: {data_bonita}')
        print("-" * 30)

def marcar_concluida():
    print('Organizando as concluidas e Pendentes:')
    identificador = int(input('Informe o ID que deseja modificar: '))

    tarefa_encontrada = False #marcação pra saber se foi achado o ID

    for lista in lista_tarefas:
        if lista["id"] == identificador:
            lista["concluida"] = True
            print('Status modificado com sucesso')
            tarefa_encontrada = True
            break

        if not tarefa_encontrada:
            print('Nenhuma tarefa com esse ID enconmtrada!')

def remover_tarefa():
    print('Removendo Tarefas')
    remove = input('Informe qual tarefa deseja remover: ').lower()
    for lista in lista_tarefas:
        if lista['tarefa'] == remove:
            lista_tarefas.remove(lista)
            print('Removida com sucesso!')

while True:
    print('\n____Menu____')
    print('1 - Adicionar Tarefa')
    print('2 - Listar')
    print('3 - Marcar como Concluida')
    print('4 - Remover')
    print('5 - Sair')

    opcao = int(input('\nEscolha uma opção: '))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        marcar_concluida()
    elif opcao == 4:
        remover_tarefa()
    elif opcao == 5:
        break