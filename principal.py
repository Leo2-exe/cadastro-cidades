from src.classes.cidade import Cidade
import json

sair = False


#arquivo = open(r".src\bd\bd.json", 'r')
with open('./src/bd/bd.json', 'r') as file:
    d1_json = file.read()
    lista_cidades = json.loads(d1_json)
#Imprimi as cidades que já estão na lista
print(lista_cidades)


while not sair:
        
#print("Esta repetindo")

#Recebendo informações da cidade
    nome_cidade = input("Digite o nome da cidade: ")
    populacao_cidade = input("Digite a populção da cidade: ")
    sigla_estado = input("Digite a sigla do estado: ")
    nome_estado = input("Digite o nome do estado: ")    

#Instanciar a cidade
    uf = { "sigla": sigla_estado , "nome": nome_estado }
#Criado o objetivo uf para organizar o codigo)

    nova_cidade = Cidade(nome_cidade, populacao_cidade, uf )

#Adiciona a cidade na lista
    lista_cidades.append({
        "nome": nova_cidade.nome,
        "populacao": nova_cidade.populacao,
        "uf": {
            "sigla": nova_cidade.uf["sigla"],
            "nome": nova_cidade.uf["nome"],
        }
    })

    resposta = input("Deseja cadastrar outra cidade? (S/N)") 
#Verificando resposta correta S ou N 
    #print(resposta.upper())
    resposta_incorreta = resposta.upper() != "S" and resposta.upper() != "N"
    while resposta_incorreta:
        print("A reposta deve ser S ou N. ")
        resposta = input("Deseja cadastrar outra cidade? (S/N) ")
    if resposta.upper() == "N":
            sair = True

#arquivo = open(r".src\bd\bd.json","w")
with open('./src/bd/bd.json', 'w+') as file:
    file.write(json.dumps(lista_cidades))
