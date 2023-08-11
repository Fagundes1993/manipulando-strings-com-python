nome = "Matheus"
idade = 29
profissao = "Consultor"
linguagem = "Comex"
saldo = 123.456789

dados = {"nome": "Matheus", "idade": 29}

print("Nome: %s Idade: %d" % (nome, idade))                             #old style

print("Nome: {} Idade: {}" .format (nome, idade))                       #Metodo format

print("Nome: {0} Idade: {1}" .format (nome, idade))                     #Metodo format com indices

print("Nome: {name} Idade: {age}" .format (name=nome, age=idade))       #Metodo format com identificadores

print("Nome: {nome} Idade: {idade}" .format(**dados))                   #Metodo format usando dicionario

print(f"Nome: {nome} Idade: {idade}")                                   #utilizando o fstring

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")                    #Impressaõ de saldo com todas as casas decimais

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")              #exibição de saldo com 2 casas decimais e 10 espaços

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")                #exibição de saldo com 2 casas decimais