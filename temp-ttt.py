# if xstate[0] == 'X': return'X' else if zstate[0]=='O':return'O' else: return 0

def board(xstate, zstate):
    print(f"{'X' if xstate[0] else 'O' if zstate[0] else 1} | {'X' if xstate[1] else 'O' if zstate[1] else 2} | {'X' if xstate[2] else 'O' if zstate[2] else 3}")
    print("--|---|--")
    print(f"{'X' if xstate[3] else 'O' if zstate[3] else 4} | {'X' if xstate[4] else 'O' if zstate[4] else 5} | {'X' if xstate[5] else 'O' if zstate[5] else 6}")
    print("--|---|--")
    print(f"{'X' if xstate[6] else 'O' if zstate[6] else 7} | {'X' if xstate[7] else 'O' if zstate[7] else 8} | {'X' if xstate[8] else 'O' if zstate[8] else 9}")

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    board(xstate, zstate)
    turn = 1 #if 1 then x 0 then O
    print("Welcome to Tic_Tac_Toe 2P Game")
    p1 = input("Please Enter Player1(X) name: ")
    p2 = input("Please Enter Player2(Y) name: ")

    while True:
        if turn == 1:
            print(f"{p1}'s chance")
            value = int(input("Enter a place to mark X: "))
            if xstate[value-1]==0 and zstate[value-1]==0:
                xstate[value-1]=1
            else:
                print("That's already occupided, please try again.")
                continue
        else:
            print(f"{p2}'s chance")
            value = int(input("Enter a place to mark O: "))
            if zstate[value-1]==0 and xstate[value-1]==0:
                zstate[value-1]=1
            else:
                print("That's already occupided, please try again.")
                continue

        turn = 1- turn
        board(xstate,zstate)
        # checkwin(xstate,zstate)
