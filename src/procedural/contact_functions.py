"""
Funcoes de contatos usando Python basico.

Nesta fase, os contatos serao representados por dicionarios simples.

Exemplo futuro:
{
    "nome": "Marcio",
    "telefone": "21999999999",
    "email": "marcio@email.com",
    "origem": "whatsapp"
}

TODO Fase 1:
- criar funcao para cadastrar contato;
- criar funcao para listar contatos;
- criar funcao para buscar contato por telefone;
- criar funcao para detectar contatos duplicados.
"""
def cadastrar_contato(contatos):
    print("Preciso de apenas 4 itens. Responda abaixo, por favor.")

    while True:
        nome = input("Digite o nome do lead: ")

        if nome == "":
            print("Nome não pode estar vazio.")
            continue

        telefone = input("Digite o numero do lead: ")

        if not telefone.isdigit():
            print("Digite apenas números no telefone.")
            continue

        email = input("Digite o email do lead: ")

        if "@" not in email:
            print("O email precisa ter '@'.")
            continue

        origem = input("Digite a origem do lead: ")

        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "origem": origem,
        }

        contatos.append(contato)
        print("Contato foi adicionado com sucesso!")
        break

def listarContatos(contatos) :
        quantidade_leads = 0

        if len(contatos) < 1 :
            print("Nenhum contato encontrado")
            return
        
        for lead in contatos :
            print(f"Lead : {quantidade_leads + 1 }")
            for chave, valor in lead.items() :
                print(f"{chave} : {valor}")
            quantidade_leads += 1

def buscaLead(contatos) :
    qual_telefone = input("Digite aqui o telefone que você deseja buscar : ")
    resultado = False
    lead_encontrado = None
    for lead in contatos :
        telefone = lead["telefone"]
                    
        if telefone == qual_telefone :
            resultado = True
            lead_encontrado = lead
            break
                
    if resultado is True :
        print("Concluido, o lead foi achado:")
        print(lead_encontrado)
    else :
        print(f"Desculpe não achei nenhum lead com esse telefone : {qual_telefone}")