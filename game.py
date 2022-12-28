import random


def pencils_check():
    global pencils
    pencils = input('How many pencils would you like to use:')
    if pencils.isdigit():
        if int(pencils) == 0:
            print("The number of pencils should be positive")
            pencils_check()
    else:
        print('The number of pencils should be numeric')
        pencils_check()


def player_check():
    global player
    if player not in names:
        print(f"Choose between '{names[0]}' and '{names[1]}'")
        player = input()
        player_check()


def turn():
    global player
    print_turn()
    if player == names[0]:
        player = names[1]
        player_take = input()
        take(player_take)
        turn()
    player = names[0]
    player_take = str(jack())
    take(player_take)
    turn()


def print_turn():
    print(player + "'s turn:")


def take(player_take):
    global total_pencils
    possible_values = ['1', '2', '3']
    if player_take not in possible_values:
        print("Possible values: '1', '2' or '3'")
        player_take = input()
        take(player_take)
    elif player_take in possible_values:
        if int(player_take) > total_pencils:
            print('Too many pencils were taken')
            player_take = input()
            take(player_take)
        else:
            total_pencils -= int(player_take)
            if total_pencils == 0:
                winning()
            pencils_print()


def pencils_print():
    print('|' * total_pencils)


def jack():
    player2_take = 0
    if total_pencils % 4 == 1 and total_pencils != 1:
        player2_take = random.randint(1, 3)
    elif total_pencils == 1:
        player2_take = 1
    elif total_pencils % 4 == 2:
        player2_take = 1
    elif total_pencils % 4 == 3:
        player2_take = 2
    elif total_pencils % 4 == 0:
        player2_take = 3
    print(player2_take)
    return player2_take


def winning():
    print(player, 'won!')
    exit()


global pencils
pencils_check()
total_pencils = int(pencils)
names = ['John', 'Jack']
player = input(f'Who will be the first ({names[0]}, {names[1]}):')
player_check()
pencils_print()
turn()
