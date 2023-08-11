nome = "mAtHeUs"

print(nome.upper())     #maiusculo
print(nome.lower())     #minusculo
print(nome.title())     #titulo

texto = "   Olá mundo!      "

print(texto + ".")
print(texto.strip() + ".")      #eliminação dos espaços
print(texto.lstrip() + ".")     #eliminação dos espaços da esquerda
print(texto.rstrip() + ".")     #eliminação dos espaços da direita

menu = "Python"

print("####" + menu + "####")       #impressão centralizada por caractere
print(menu.center(14, "#"))         #impressão centralizada pela função center
print("-".join(menu))               #inserção de caractere pelo método join
