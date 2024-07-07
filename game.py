#Iniciar juego
colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[0m',
}

def color_letter(letter, color):
    return colors[color] + letter + colors['ENDC']

win = False
word = 'audios'
board = []

for i in range(6):
    board.append(['_' for l in range(6)]) #va a poner _ en 6x6 (los dos for)

cont = 0
while (not win) and (cont < len(word)):
    text = input('Dime una palabra de 6 letras: ')
    while len(text) != len(word):
        if len(text) != len(word):
            print(f'La palabra no tiene {len(word)} letras')
            text = input('Dime una palabra de 6 letras: ')

    # Lógica
    if word == text:
        board[cont] = [l for l in text]
        win = True

    # letra en palabra
    else:
        test_line = []
        for j in range(len(word)):
            if text[j] == word[j]:
                test_line.append(color_letter(text[j], 'green'))
            elif text[j] in word:
                test_line.append(color_letter(text[j], 'yellow'))
            else:
                test_line.append(color_letter(text[j], 'red'))

            board[cont] = test_line


    #Tablero dibujado
    for i in range(6):
        print(' '. join(board[i]))

    cont += 1

    if win:
        print('¡Ganaste!')
    else:
        print('¡Perdiste!')