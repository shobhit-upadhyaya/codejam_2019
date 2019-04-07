t = int(input())

for i in range(1,t+1):
    grid = input()
    her_moves = input()
    my_moves = []
    for move in her_moves:
        if move == 'E':
            my_moves.append('S')
        else:
            my_moves.append('E')
    
    my_moves = "".join(my_moves)
    print("Case #"+str(i)+":", my_moves)
