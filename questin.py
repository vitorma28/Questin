import json

mode = str(input('Qual modo vc deseja?(Jogar / Criar / Remover) '))
if mode.lower() == 'jogar':
    file = open('questions.json')
    jsonf = file.read()
    q = json.loads(jsonf)
    letern = 1
    leter = 'a'
    for i in q:
        print(i['question'])
        print('')
        for opt in i['options']:
            if letern == 1:
                leter = 'a'
            elif letern == 2:
                leter = 'b'
            elif letern == 3:
                leter = 'c'
            elif letern == 4:
                leter = 'd'
            print('{}) {}'.format(leter, opt))
            letern = letern + 1
        answ = str(input("\nResposta: "))
        if answ.lower() == i['answer']:
            print('\nResposta correta!\n')
        else:
            print('\nResposta incorreta.\n')
        letern = 1
    file.close()
elif mode.lower() == 'criar':
    more = True
    print('As opcoes são a, b, c e d.')
    while more:
        file_read = open('questions.json', 'r')
        actual_content_dict = json.loads(file_read.read())
        file_read.close()
        question = str(input('Qual a pergunta: '))
        opta = str(input('Opcao A: '))
        optb = str(input('Opcao B: '))
        optc = str(input('Opcao C: '))
        optd = str(input('Opcao D: '))
        answ = str(input('Resposta(letra): '))
        content = {
            "question": question,
            "options": [
              opta,
              optb,
              optc,
              optd
            ],
            "answer": answ
        }
        actual_content_dict.append(content)
        actual_content_json = json.dumps(actual_content_dict, indent=4)

        file = open('questions.json', 'w')

        file.write(actual_content_json)

        file.close()

        cont = str(input('Continuar(s / n) '))
        if cont.lower() == 'n':
            more = False
else:
    question = str(input('Qual a pergunta: '))

    file_r = open('questions.json', 'r')
    data_str = json.loads(str(file_r.read()))
    file_r.close()

    file = open('questions.json', 'w')
    for quest in data_str:
        if quest['question'] == question:
            data_str.remove(quest)
            file.write(json.dumps(data_str, indent=4))
            print('Pergunta removida com sucesso!')
            break
    file.close()
