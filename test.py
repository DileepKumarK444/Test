def create_matrix(x_axis,y_axis):
    return ([[x+j for x in range(0,x_axis)] for j in range(0,y_axis)])

def get_cordinates(a,b,s):
    d = create_matrix(a,b)
    d = {'N':'West','S':'East','W':'South','E':'North'}
    D = 'N'
    x = 0
    y = 0
    for i, val in enumerate(s):

        if (x<0 or y <0):
            print('Move out of range')
            break
        if i == 0 and val == 'L':
            print('Not a valid move')
            break

        if i ==0 and val in ['F','R']:
            D = 'E'

        if(val == 'F'):
            if D == 'N':
                x -=1
            if D == 'E':
                y +=1
            if D == 'W':
                y -=1
            if D == 'S':
                x +=1

        elif val =='R':
            if(D =='S'):
                D = 'W'
            elif(D =='W'):
                D = 'N'
            elif(D =='N'):
                D = 'E'
            else:
                D = 'S'

        else:
            if(D =='S'):
                D = 'E'
            elif(D =='E'):
                D = 'N'
            elif(D =='N'):
                D = 'W'
            else:
                D = 'S'

    return [x+1,y+1, d[D]]
R = get_cordinates(5,5,'FFRFLFLF')
print(R)