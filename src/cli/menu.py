"""
Menu do terminal.

TODO Fase 1:
- mostrar opcoes para o usuario;
- ler a opcao escolhida com input;
- chamar funcoes simples da pasta procedural;
- manter a regra de negocio fora deste arquivo.
"""

from procedural.contact_functions import cadastrar_contato

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
            print(contatos)
            continue
        elif resposta == 3 :
            
            qual_telefone = input("Digite aqui o telefone que você deseja buscar : ")
            resultado = False
            for lead in contatos :
                telefone = lead["telefone"]
                
                if telefone == qual_telefone :
                    resultado = True
                    break
            
            if resultado is True :
                print("Concluido o lead foi achado\n"
                      f"{lead}"
                      )
                continue
            else :
                print(f"Desculpe não achei nenhum lead com esse telefone : {qual_telefone}")
                continue
        elif resposta == 0 :
            print("Até mais")
            break