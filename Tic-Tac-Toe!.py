print("Tic-Tac-Toe Board")
board=[1,2,3,4,5,6,7,8,9]
while True:
    print("   ",board[0]," | ",board[1]," | ",board[2])
    print("  -----------------")
    print("   ",board[3]," | ",board[4]," | ",board[5])
    print("  -----------------")
    print("   ",board[6]," | ",board[7]," | ",board[8])
    print("")
    p1=int(input("Player 1 move: "))
    board[p1-1]='X'
    print("")
    print("   ",board[0]," | ",board[1]," | ",board[2])
    print("  -----------------")
    print("   ",board[3]," | ",board[4]," | ",board[5])
    print("  -----------------")
    print("   ",board[6]," | ",board[7]," | ",board[8])
    print("")
    p2=int(input("Player 2 move: "))
    board[p2-1]='0'
    print("")
    print("   ",board[0]," | ",board[1]," | ",board[2])
    print("  -----------------")
    print("   ",board[3]," | ",board[4]," | ",board[5])
    print("  -----------------")
    print("   ",board[6]," | ",board[7]," | ",board[8])
    print("")
    if board[0]==board[1]==board[2] and board[0] in ['X','0']:
        if board[0]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[3]==board[4]==board[5] and board[3] in ['X','0']:
        if board[3]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[6]==board[7]==board[8] and board[6] in ['X','0']:
        if board[6]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[0]==board[4]==board[8] and board[0] in ['X','0']:
        if board[0]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[2]==board[4]==board[6] and board[2] in ['X','0']:
        if board[2]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[0]==board[3]==board[6] and board[0] in ['X','0']:
        if board[0]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[1]==board[4]==board[7] and board[1] in ['X','0']:
        if board[1]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break
    elif board[2]==board[5]==board[8] and board[2] in ['X','0']:
        if board[2]=='X':
            print('')
            print('Player1 is the Winner')
            break
        else:
            print('')
            print('Player2 is the Winner')
        break

