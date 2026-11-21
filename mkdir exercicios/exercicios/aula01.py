# Exercício 1

print(7 / 2) # 3.5
print(7 // 2) # 3
print(7 % 2) # 1
print('3' + '4') # 34
print('3' * 3) # 333
print(type(7 / 2)) #float
print(2 ** 10) # 1024

# Exercício 2

nome = input('Qual é o seu nome?')
idade = int(input('Qual é a sua idade?'))
idade_ano_que_vem = idade + 1

print(f'Olá, {nome}! Ano que vem você terá {idade_ano_que_vem} anos.')

# Exercício 3 

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')

print(f'Média: {media:.2f}')

# Exercício 4

nome = 'Aline'
print(nome)

idade = int(input('idade: '))
print(idade + 1)

numero1 = 5
print(numero1)