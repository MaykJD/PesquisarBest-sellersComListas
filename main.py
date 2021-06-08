# O 1° Para o cabecalho, É o 2° Para as 4 FUNÇOES basicas do codigo
# As funçoes são por_intervalo_ano(),por_mes(),por_autor_string(),por_titulo().
lista_livros =[]

def arqExiste(): #Verificar Se o arquivo existe
    while True:
        try: #tratamento
            arquivo = open('bestsellers.txt', 'r')
            for line in arquivo:
                line = line.strip().split('\t')
                lista_livros.append(line)
        except FileNotFoundError as erro:
            print('\033[1;31mOlá infelizmente a lista o não pode ser construida ERRO: {} !'.format(erro))
            raise SystemExit
        else:
            return True

def por_intervalo_ano(): #Procurar arquivo em intervalo de ano
    try:
        ano_inical = int(input('Ano inicial: '))
        ano_final = int(input('Ano final: '))
    except(ValueError ,TypeError,KeyboardInterrupt, KeyError):
        print(f'Erro Não consegui fazer o que você me disse ! D')
    else:
        mainMenu() # -> Adiciona linhas para ficar minmamente ORGANIZADO o codigo
        print('{:<30} {:<2}'.format('Livro','Ano').strip())
        mainMenu()
        teste = True
        for itens in lista_livros:
            data = itens[3].split('/')
            ano = int(data[2])
            if ano_inical == None or ano_final == None:
                print('Ei nada digitado !')
                break
            elif ano>= ano_inical and ano <= ano_final:
                teste = False
                print('{:<30}{}'.format(itens[0], itens[3]))
        if teste == True:
            print('Desculpe Nada encontrado D:')

def por_mes(): #Procurar arquivo por mês
    print('Se liga (: Mês esta em formato numérico -> 1,2,3,4.. OK ?')
    mes_usuario = str(input('Qual mês ? : '))
    ano_usuario = str(input('Qual ano ? : '))
    mainMenu()
    print('{:<34} {:>3} {:>6}'.format('Livro','Mês','Ano').strip())
    mainMenu()
    teste = True
    for meses in lista_livros:
        mes_exp = str(meses[3][0].strip().rjust(10,' '))
        if not ano_usuario and not mes_usuario:
            print('Nada digitado!')
            break
        if mes_usuario in mes_exp and ano_usuario in meses[3]:
            teste = False
            print(' {:<32}  {:>3}  {:>5} '.format(meses[0],meses[3][0],meses[3]).strip().upper())
    if teste == True:
        print('Desculpe Nada encontrado D:')

def por_autor_string(): #Procurar por Autor/String
    user_string = str(input('Digite uma String ou um Autor: ')).upper().strip()
    print('Infelzimente Não possivel achar o que você procura !')
    mainMenu()
    print('{:<10}{:>36}'.format('Livro','Autor'))
    mainMenu()
    teste = True
    for string in lista_livros:
        if not user_string :
            print('Ei Nada foi digitado ! D: ')
            break
        elif user_string in string[1]:
            teste = False
            print('{:<10} {:6>} {:>3}'.format(string[0],'AUTOR-->',string[1]).strip().rjust(10,' '))
    if teste == True:
        print('Desculpe Nada encontrado D:')

def por_titulo(): #Procurar por titulo
    user_string1= input('Digite uma String ou um Livro: ').upper().strip()
    #true e que passou e tem letra
    #false e que nao tem a letra
    mainMenu()
    print('{:<10}{:>40}'.format('Livro', 'Autor').strip())
    mainMenu()
    teste = True

    for string1 in lista_livros:
        srt = str(string1[0]).upper()
        if  not user_string1:
            print('Nada digitado')
            break
        elif user_string1 in srt:
            teste = False
            print('{} de {}'.format(string1[0],string1[1]).strip().rjust(10))

    if teste == True:
        print('Desculpe Nada encontrado D:')

#----------------------------------------------------------------

def tratar(msg): #Tratamento
    while True:
        try:
            n = (input(msg))
        except (ValueError ,TypeError,KeyboardInterrupt, KeyError) as erro:
            print(f'ERRO: D: Desculpe isso não e uma opção valida {erro}')
        except (KeyboardInterrupt, KeyError):
            print('ERRO: Usuario não digitou qualquer numero')
            continue
        else:
            return n

def linha(tam = 50):
    return '\033[1;97m'	  '-' * 50

def linha1(tam = 70):
    return '\033[1;97m'	  '-' * 90

def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(lista):
    cabecalho('BEST SELLERS MAIS VENDIDO NEW YORK TIMES')
    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[31m - \033[34m{item}\033[31m')
        c += 1
    print('\033[1;97m'+linha())
    opc = tratar('\033[32mSua Opção: ')
    return opc


def mainMenu(tam = 50):
    print(linha1())


arqExiste() #Verificar existencia de arquivo - (Func struct.py)

print('OK arquivo construido')
while True:
    resposta = menu(['Exibir livros em um invtervalo de ano',
                    'Exibir livros em um mês é ano especifico',
                    'Pesquise um autor',
                    'Pesquise um titulo',
                    'Sair do sistema Press 5 OR S'])
    if resposta == '1':
        por_intervalo_ano()
    elif resposta == '2':
        por_mes()
    elif resposta == '3':
        por_autor_string()
    elif resposta == '4':
        por_titulo()
    elif resposta == '5' or resposta =='s' or resposta == 'S':
        print('Saindo do sistema')
        break
    else:
        print('OPÇÃO INVALIDA ! Por favor digite uma opção valida da lista')

#----------------------------------------------------------------