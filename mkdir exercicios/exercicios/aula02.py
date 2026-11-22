# Exercício 1 

number1 = int(input('Digite um número: '))
resto = number1 % 2 

if resto == 0:
    print('The number entered is even!')
else:
    print('The number entered is odd!')

# Exercício 2 

nota = int(input('Digite uma nota de 0 a 10: '))

if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
else:
    print('D')

# Exercício 3

number = int(input('Digite um número: '))

print('---GERADOR DE TABUADA---')

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# Exercício 4

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total = total + i
print(total)

# Exercício 5

secreto = 7
contador = 1

while True:
    palpite = int(input('Adivinhe o número de 0 a 10: '))
    if palpite == secreto:
        print('Acertou!')
        print(f'Você acertou em {contador} tentativa(s).')   
        break
    elif palpite > secreto:
        print('Menor! Tente novamente!')
        contador = contador + 1
    elif palpite < secreto:
        print('Maior! Tente novamente!')
        contador = contador + 1

# Exercício 6

while True:
    nota = float(input('Descubra a regra! Digite uma nota: '))
    if nota >= 0 and nota <= 10:
        print('Parabéns você descobriu a regra, só ganha se a nota estiver de 0 a 10!')
        break
    else:
        print("Você ainda não descobriu a regra. Tente novamente!")
