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
        'Tarefa': tarefa,
        'Descrição': desc,
        'data_conclusão': data_formatada,
        'concluida': False
    }
    #adicionando o dicionario na lista
    lista_tarefas.append(dicionario_tarefa)
#fazer ainda função listar,remover,status etc

while True:
    print('\n____Menu____')
    print('1 - Adicionar Tarefa')
    print('2 - Listar')
    print('3 - Sair')

    opcao = int(input('Escolha uma opção: \n'))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        print(lista_tarefas)
    elif opcao == 3:
        break