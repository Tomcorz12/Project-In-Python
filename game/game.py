import random

def runGame():
    
    computerWins = 0
    playerWins = 0
    
    while True:
        roundsPlayed = 1
        print("Bienvenido al juego de Piedra, Papel o Tijera")
        print("----------------------------------------------")
        print(f'Ronda => ', roundsPlayed)
        print("----------------------------------------------")
        
        roundsPlayed += 1

        print(f'Victorias del jugador => {playerWins}')
        print(f'Victorias del computador => {computerWins}')
        
        optionPlayer1, computerOption = selectOptions()
        
        playerWins, computerWins = checkRules(optionPlayer1, computerOption, playerWins, computerWins)
        
                
        if playerWins == 2:
            print('El jugador ganó todas las rondas')
            break
        
        if computerWins == 2:
            print('El computador ganó todas las rondas')
            break

def selectOptions():
    
    options = ('piedra', 'papel', 'tijera')

    optionPlayer1 = input("Insert one option to play => ")
    optionPlayer1 = optionPlayer1.lower()
    
    if not optionPlayer1 in options:
        print("Opción no válida")
        return None, None
        
    computerOption = random.choice(options)
    
    print(f'Player option is => {optionPlayer1}')
    print(f'Computer option is => {computerOption}')
    return optionPlayer1, computerOption

def checkRules(optionPlayer1, computerOption, playerWins, computerWins):
    
    if optionPlayer1 == computerOption:
        print("Empate")
    elif optionPlayer1 == 'piedra':
        if computerOption == 'tijera':
            print("Ganó el jugador")
            playerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
        else:
            print("Ganó el computador")
            computerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
    elif optionPlayer1 == 'papel':
        if computerOption == 'tijera':
            print("Ganó el computador")
            computerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
        else:
            print("Ganó el jugador")
            playerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
    elif optionPlayer1 == 'tijera':
        if computerOption == 'piedra':
            print("Ganó el computador")
            computerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
        else:
            print("Ganó el jugador")
            playerWins += 1
            print(f'Victorias del jugador => {playerWins}')
            print(f'Victorias del computador => {computerWins}')
    return playerWins, computerWins

runGame()