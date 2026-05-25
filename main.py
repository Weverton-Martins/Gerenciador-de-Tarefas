'''
Este aplicativo permitirá que você:
● Adicione novas tarefas com título, descrição e data de conclusão.
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

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo: #puxa o arquivo em modo de leitura 'r'
        #lê o que esta no arquivo e guarda em uma variavel
            return json.load(arquivo)
    else:
        return []
    
def salvar_tarefas():
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo: #cria e abre o arquivo chamado 'tarefa.json' em modo de escrita 'w'
        json.dump(lista_tarefas, arquivo, indent= 4) #despeja minha lista no arquivo
    print('Tarefas salvas com sucesso no disco!')

# Estrutura lógica de uma tarefa, como serão os dicionarios armazenados
'''
tarefa = {
    "id": 1, #Vai ser taribuido de forma automatica
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
    data = input('Data de Conclusão (formato DD/MM/YYYY): ')#passada como str mas alterada quando ordenado por data
    id = len(lista_tarefas) +1
    
    #Criando o dicionario com os valores solciitados
    dicionario_tarefa = {
        'id': id,
        'tarefa': tarefa,
        'descrição': desc,
        'data_conclusão': data,
        'concluida': False
    }
    #adicionando o dicionario na lista
    lista_tarefas.append(dicionario_tarefa)

def listar_tarefas():
    print('\nLista de tarefas:')
    for lista in lista_tarefas:

        print(f'id: {lista["id"]} | status: {'Concluida' if lista.get("concluida") else "Pendente"}')
        print(f'Tarefa: {lista["tarefa"]}')
        print(f'Descrição: {lista["descrição"]}')
        print(f'Data: {lista['data_conclusão']}')
        print("-" * 30)

def marcar_concluida():
    print('Organizando as concluidas e Pendentes:')
    identificador = int(input('Informe o ID que deseja modificar: '))

    tarefa_encontrada = False #marcação pra saber se foi achado o ID

    for lista in lista_tarefas:
        #modificando o ID pra concluido se for encontrado na lista
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
        #se lista encontrada a remove
        if lista['tarefa'] == remove:
            lista_tarefas.remove(lista)
            print('Removida com sucesso!')

def pesquisar_tarefa():
    print('Pesquise tarefas por titulo ou descrição:')
    title = input('Informe qual o titulo ou descrição que deseja procurar: ').lower() #termo a ser pesquisado

    tarefa_encontrada = False #condição se deu certo ou não
    for lista in lista_tarefas:
        #mostra ao usuario apenas a lista desejada
        if (title in lista['tarefa']) or (title in lista['descrição']):
           
            print(f'id: {lista["id"]} | status: {'Concluida' if lista.get("concluida") else "Pendente"}')
            print(f'Tarefa: {lista["tarefa"]}')
            print(f'Descrição: {lista["descrição"]}')
            print(f'Data: {lista['data_conclusão']}')
            print("-" * 30)

            tarefa_encontrada = True
    if not tarefa_encontrada: #caso não encontre o termo continua como false e retorna a mensagem 
        print('Nenhuma tarefa encontrada com esse termo!')

def extrair_datas(tarefa): #função pra 'traduzir' a data pro python, pois esta lendo como str como um texto
    texto_data = tarefa['data_conclusão']
    return datetime.strptime(texto_data, "%d/%m/%Y") #aqui pra saber qual data vem antes e não em alfabetica

def ordenar_pordata():
    print('\n---Ordenando Por Datas---\n')
    
    lista_tarefas.sort(key=extrair_datas) #o key diz pra usarmos nossa função pra pegar a ordem correta
    print('Tarefas ordenadas com sucesso!')

while True:
    print('\n____Menu____')
    print('1 - Adicionar Tarefa')
    print('2 - Listar')
    print('3 - Marcar como Concluida')
    print('4 - Remover')
    print('5 - Pesquisar')
    print('6 - Ordenar Por Data')
    print('7 - Salvar e Sair')

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
        pesquisar_tarefa()
    elif opcao == 6:
        ordenar_pordata()
    elif opcao == 7:
        salvar_tarefas()
        break
    else:
        print('Opção invalida!')