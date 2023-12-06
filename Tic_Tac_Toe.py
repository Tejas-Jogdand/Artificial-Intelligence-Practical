# if xstate[0] == 'X': return'X' else if zstate[0]=='O':return'O' else: return 0
def sum(a,b,c):
    return a+b+c

def board(xstate, zstate):
    print(f"{'X' if xstate[0] else 'O' if zstate[0] else 1} | {'X' if xstate[1] else 'O' if zstate[1] else 2} | {'X' if xstate[2] else 'O' if zstate[2] else 3}")
    print("--|---|--")
    print(f"{'X' if xstate[3] else 'O' if zstate[3] else 4} | {'X' if xstate[4] else 'O' if zstate[4] else 5} | {'X' if xstate[5] else 'O' if zstate[5] else 6}")
    print("--|---|--")
    print(f"{'X' if xstate[6] else 'O' if zstate[6] else 7} | {'X' if xstate[7] else 'O' if zstate[7] else 8} | {'X' if xstate[8] else 'O' if zstate[8] else 9}")

def checkwin(xstate, zstate):

    wins = [[0,1,2],[3,4,5],[6,7,8],[0,4,6],[2,4,6],[0,3,6],[1,4,7],[2,5,6]]

    for win in wins:
        if sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3:
            print(f"{p1} wins")
            return 1
        elif sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3:
            print(f"{p2} wins")
            return 0
    return -1

if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    board(xstate, zstate)
    turn = 1 #if 1 then x 0 then O
    print("Welcome to Tic_Tac_Toe 2P Game")
    p1 = input("Please Enter Player1(X) name: ")
    p2 = input("Please Enter Player2(Y) name: ")

    for i in range(0,9):
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
        check = checkwin(xstate,zstate)
        board(xstate,zstate)
        if check != -1:
            break
        turn = 1- turn