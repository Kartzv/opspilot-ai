"""
Menu do terminal.

TODO Fase 1:
- mostrar opcoes para o usuario;
- ler a opcao escolhida com input;
- chamar funcoes simples da pasta procedural;
- manter a regra de negocio fora deste arquivo.
"""

while True :
    
    resposta = input("Olá tudo bem seja bem vindo ao menu\n1 - Cadastrar Contato\n2 - Listar Contatos\n3 - Buscar contato por telefone\n0 - Sair\nEscolha uma opção : ")
    opcoes_validas = {0,1,2,3}
    try :
        filtra_resposta = int(resposta)
    except ValueError :
        print("=== Precisa Digitar um número valido ====")
        print(resposta)
        continue
    
    resposta = filtra_resposta

    if resposta not in opcoes_validas :
        print("=== Desculpe ainda não temos essa opção, use uma valida === ")
        continue
    if resposta == 1 :
        print("Cadastrar Contato")
        continue
    elif resposta == 2 :
        print("Listar Contatos")
        continue
    elif resposta == 3 :
        print("Buscar contato por telefone")
        continue
    elif resposta == 0 :
        print("Até mais")
        break