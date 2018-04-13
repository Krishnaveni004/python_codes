#!/usr/bin/python
import math
# Head ends here
def next_move(posr, posc, board):
    r1=5
    c1=5
    min=1000
    for r in range(0,5):
        for c in range(0,5):
                if(board[r][c]=='d'):
                    if(min > math.sqrt(((r-posr)**2) + ((c-posc)**2))):
                        min=(math.sqrt(((r-posr)**2) + ((c-posc)**2)))
                        r1=r
                        c1=c
    if(r1-posr==0 and c1-posc==0):
        print("CLEAN")
    else:
        if(r1>posr and c1>posc):
            if((r1-posr) > (c1-posc)):
                print("RIGHT")
            else:
                print("DOWN")
        elif(r1>posr and c1<posc):
            if((r1-posr) > (posc-c1)):
                print("LEFT")
            else:
                print("DOWN")
        elif(r1<posr and c1<posc):
            if((posr-r1)>(posc-c1)):
                print("LEFT")
            else:
                print("UP")
        elif(r1<posr and c1>posc):
            if((posr-r1)>(c1-posc)):
                print("RIGHT")
            else:
                print("UP")
        elif(r1==posr):
            if(c1>posc):
                print("RIGHT")
            else:
                print("LEFT")
        elif(c1==posc):
            if(r1>posr):
                print("DOWN")
            else:
                print("UP")
        else:
            print("GARBAGE")

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

