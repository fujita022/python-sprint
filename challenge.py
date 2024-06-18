#Abordagem do assunto, e informações sobre a Fórmula E para o nosso usuário:
print(f'A Fórmula E, ou Fórmula Elétrica, é uma categoria de automobilismo que utiliza carros de corrida totalmente elétricos. A Fórmula E foi lançada pela FIA (Fédération Internationale de l Automobile) em 2014 como um campeonato mundial\n de monopostos elétricos, com o objetivo de promover a sustentabilidade e o desenvolvimento de tecnologias de veículos elétricos.\n')
#Pedir nome ao usuário e um nome para chamá-lo durante sua interação com a plataforma:
user = input('Digite um nome de usuário para acessar a plataforma: ')
nome = user[0].upper()+user[1:].lower()
print(f'Seja bem-vindo {nome} é um prazer ter você com a gente! Estamos muito felizes em saber que a Fórmula E está expandindo e chegou até você!\n')
#Interagir com o usuário com seus gostos pessoais sobre a Fórmula E:
print('Que tal você contar para a gente qual sua equipe e pilotos favoritos para receber informações exclusivas!?')
print('Aqui são as equipes e os pilotos:\n')

#Dicionário com listas sobre equipe e pilotos respectivamente:
epformula = {
'1 - Equipe Andretti Autosport' : ['Jake Dennis','Norman Nato'],

'2 - Equipe DS Penske' : ['Stoffel Vandoorne','Jean-Eric Vergne'],

'3 - Equipe ERT Formula E Team' : ['Sergio Camara','Dan Ticktum'],

'4 - Equipe NEOM McLaren' : ['Jake Hughes','Sam Bird'],

'5 - Equipe Maserati Racing' : ['Maximilian Gunther','Jehan Daruvala'],

'6 - Equipe Jaguar Racing' : ['Mitch Evans','Nick Cassidy'],

'7 - Equipe Abt Cupra' : ['Lucas di Grassi','Nico Müller'],

'8 - Equipe TAG HEUER Porsche Team' : ['Pascal Wehrlein','Antonio Felix da Costa'],

'9 - Equipe Mahindra Racing' : ['Edoardo Mortara', 'Nyck De Vries'],

'10 - Equipe Envision Racing' : ['Robin Frijns','Sébastien Buemi'],

'11 - Equipe Nissan Formula E Team' : ['Oliver Rowland', 'Sacha Fenestraz']
}

#Separar equipes e pilotos visualmente para o usuário: 
for equipe, piloto in epformula.items():
  print(f"{equipe}: {', '.join(piloto)}\n")

#Enquanto não for inserido o número desejado o programa não prossegue para a próxima fase, e exibe uma mensagem de erro enquanto não foi inserido:
user_fav = None
while user_fav != 1 or user_fav != 2 or user_fav != 3 or user_fav != 4 or user_fav != 5 or user_fav != 6 or user_fav != 7 or user_fav != 8 or user_fav != 9 or user_fav != 10 or user_fav != 11:
  user_fav = input('Escolha a sua equipe favorita de 1 a 11: ')
#Condições de acordo com a opção escolhida pelo usuário: 
  if user_fav == '1':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/0a33d76e-64e6-4823-b70b-27b79a48679c/andretti-formula-e ')
    print('Você escolheu a equipe Andretti Autosport com os pilotos:')
    print(epformula["1 - Equipe Andretti Autosport"])
    break
  elif user_fav == '2':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/e05ede6d-d065-497b-a298-85afeeeb2ab1/ds-penske')
    print('Você escolheu a equipe DS Penske com os pilotos:')
    print(epformula["2 - Equipe DS Pensake"])
    break
  elif user_fav == '3':   
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/5ac8091a-b415-4abb-a7ef-fb5511e545d5/ert-formula-e-team')
    print('Você escolheu a equipe ERT Formula E Team com os pilotos:')
    print(epformula["3 - Equipe ERT Formula E Team"])
    break
  elif user_fav == '4':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/0176f3e2-1247-494d-9a8d-b0950437ee8f/neom-mclaren-formula-e-team')
    print('Você escolheu a equipe McLaren com os pilotos:')
    print(epformula["4 - Equipe  NEOM McLaren"])
    break
  elif user_fav == '5':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/19821c93-f115-41fb-af4f-80831a91afef/maserati-msg-racing')
    print('Você escolheu a equipe Maserati Racing com os pilotos:')
    print(epformula["5 - Equipe Maserati Racing"])
    break
  elif user_fav == '6':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/05dab754-2899-411b-9c4e-72311a36cc9c/jaguar-tcs-racing')
    print('Você escolheu a equipe Jaguar Racing com os pilotos:')
    print(epformula["6 - Equipe Jaguar Racing"])
    break
  elif user_fav == '7':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/c57e46c4-8163-44f6-9c0d-b74579d51000/abt-cupra-formula-e-team')
    print('Você escolheu a equipe Abt Cupra com os pilotos:')
    print(epformula["7 - Equipe Abt Cupra"])
    break
  elif user_fav == '8':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/feb6762c-ae66-4c8e-a892-f958d6f7e774/tag-heuer-porsche-formula-e-team')
    print('Você escolheu a equipe Porsche Team com os pilotos:')
    print(epformula["8 - Equipe TAG HEUER Porsche Team"])
    break
  elif user_fav == '9':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/fa97d2e7-02ca-4983-a930-4fdaa245a852/mahindra-racing')
    print('Você escolheu a equipe Mahindra Racing com os pilotos:')
    print(epformula["9 - Equipe Mahindra Racing"])
    break
  elif user_fav == '10':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/c63aedad-a141-4ebc-9794-41a37909ef0c/envision-racing')
    print('Você escolheu a equipe Envision Racing com os pilotos:')
    print(epformula["10 - Equipe Envision Racing"])
    break
  elif user_fav == '11':
    print(f'\nObrigado {nome} por ter nos escolhido! Estamos super ansiosos com você ao nosso lado e nos apoiando!\nAcesse mais sobre nossa equipe: https://www.fiaformulae.com/pt-br/teams/c63aedad-a141-4ebc-9794-41a37909ef0c/envision-racing')
    print('Você escolheu a equipe Nissan Formula E Team com os pilotos:')
    print(epformula["11 - Equipe Nissan Formula E Team"])
    break
#Volta para o usuário afirmando o erro de input(Número não desejado inserido):
  else:
    print('Digite um número corresponde!')
#Divulgar a Fórmula E e a empresa parceira:   
print('\nAcesse ao site oficial da Fórmula E:\nhttps://www.fiaformulae.com/pt-br.\nConheça também a Mahindra Racing! Nossa equipe da Fórmula E: \nhttps://www.mahindraracing.com/\n')

#Função para jogar um Quiz:
def mostrar_perguntas(perguntas):
#Definir variável para iniciar com 0 pontos:
    pontuacao = 0
#Função para perguntas e enumerar de acordo com quantas perguntas houverem:
    for i, pergunta in enumerate(perguntas):
        print(f"\nPergunta {i + 1}: {pergunta['pergunta']}")
        for j, opcao in enumerate(pergunta['opcoes']):
            print(f"{j + 1}. {opcao}")
#Exibir para o usuário inserir sua resposta desejada:
        resposta = int(input("Sua resposta (1-4): "))
#Condição para caso o usuário acerte ou erre a pergunta:
        if pergunta['opcoes'][resposta - 1] == pergunta['resposta_correta']:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Errado! A resposta correta é: {pergunta['resposta_correta']}")
#Volta o valor da pontuaçãoo do usuário:
    return pontuacao

#Função para fazer as perguntas ao usuário:
def main():
#Perguntas que serão feitas ao usuário e gabarito abaixo(Não será exibida enquanto não for respondida a pergunta):
    perguntas = [
        {
            "pergunta": "Qual é a Fórmula que utiliza carros elétricos?",
            "opcoes": ["Fórmula 1", "Fórmula 3", "Fórmula E", "Fórmula Truck"],
            "resposta_correta": "Fórmula E"
        },
        {
            "pergunta": "Qual dessas empresas está na Fórmula E?",
            "opcoes": ["RedBull", "Mahindra", "Amazon", "Nubank"],
            "resposta_correta": "Mahindra"
        },
        {
            "pergunta": "Em qual ano surgiu a Fórmula E?",
            "opcoes": ["2014", "2010", "2009", "2022"],
            "resposta_correta": "2014"
        },
        {
            "pergunta": "Qual dessas alternativas é uma das causas da Fórmula E?",
            "opcoes": ["Aumentar a emissão de carbono", "Ajudar o planeta a aumentar o aquecimento global", "Emitir CO2 para melhorar o nosso planeta.", "Novas tecnologias necessárias para um futuro elétrico e de baixo carbono"],
            "resposta_correta": "Novas tecnologias necessárias para um futuro elétrico e de baixo carbono"
        }
    ]
#Mensagem de exibição inicial e final:
    print("Bem-vindo ao Quiz!\n")
    pontuacao = mostrar_perguntas(perguntas)
    print(f"\nSua pontuação final é: {pontuacao}/{len(perguntas)}")

#Iniciar o quiz
if __name__ == "__main__":
    main()

















