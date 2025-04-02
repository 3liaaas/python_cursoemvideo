algo = input('digita um bagulho: ')
print('o tipo primitivo deste valor digitado é ', type(algo))
print(f'só tem espaço?', algo.isspace())
print(f'é um número?', algo.isnumeric())
print(f'é alfabético?', algo.isalpha())
print(f'é alfanummérico?', algo.isalnum())
print(f'está capitalizada?', algo.isidentifier())

#