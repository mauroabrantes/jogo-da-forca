### Jogo da Forca ###

palavra_secreta = input('Digite a palavra secreta: ')
print('')
palavras_dig = []
n_chances = 3

while True:
    # Mostra quando o player perde o game, gastando todas as chances
    if n_chances <= 0:              
        print(f'Você perdeu! :(, a palavra secreta era {palavra_secreta}')
        break

    # Letra da tentativa no jogo
    letra = input('Digite uma letra: ')
    print('')

    # Verificador caso o player digite mais de uma letra na sua tentativa
    if len(letra) > 1:
        print('Ah, isso não vale, digite apenas uma letra! :D')
        continue

    # Adiciona a letra digitada
    palavras_dig.append(letra)

    # Mostra se o player acertou ou não a letra
    if letra in palavra_secreta:
        print(f'Boa! A letra "{letra}" tem na palavra secreta.')
        print('')
    else:
        print(f'Af, a letra "{letra}" não contém na palavra secreta')
        print('')
        palavras_dig.pop()

    # Adiciona a letra secreta certa no game, caso erre, adiciona *
    secreta_temp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavras_dig:
            secreta_temp += letra_secreta
        else:
            secreta_temp += '*'

    # Mostra quando o player ganha o jogo
    if secreta_temp == palavra_secreta:
        print(f'Você acertou! A palavra secreta era {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim {secreta_temp}')
        print('')

    # Mostra o número restantes de chances
    if letra not in palavra_secreta:
        n_chances -= 1
    print(f'Você tem mais {n_chances} chances!')
    print()
