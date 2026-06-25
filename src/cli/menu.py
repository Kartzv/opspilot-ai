"""
Menu do terminal.

TODO Fase 1:
- mostrar opcoes para o usuario;
- ler a opcao escolhida com input;
- chamar funcoes simples da pasta procedural;
- manter a regra de negocio fora deste arquivo.
"""

from procedural.contact_functions import cadastrar_contato, listarContatos, buscaLead

def iniciarMenu() :
    contatos = []

    while True :
        
        resposta = input("Olá tudo bem seja bem vindo ao menu\n"
                         "1 - Cadastrar Contato\n"
                         "2 - Listar Contatos\n"
                         "3 - Buscar contato por telefone\n"
                         "0 - Sair\n"
                         "Escolha uma opção : "
                         )
        
        opcoes_validas = {0,1,2,3}

        try :
            filtra_resposta = int(resposta)
        except ValueError :
            print("=== Precisa Digitar um número valido ====")
            continue
        
        resposta = filtra_resposta

        if resposta not in opcoes_validas :
            print("=== Desculpe ainda não temos essa opção, use uma valida === ")
            continue
        if resposta == 1 :
            cadastrar_contato(contatos)
            continue
        elif resposta == 2 :
            listarContatos(contatos)
        elif resposta == 3 :
            buscaLead(contatos)
        elif resposta == 0 :
            print("Até mais")
            break