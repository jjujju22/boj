while 1:
    N = input()
    if N == '0':
        break
    
    p = N[::-1]
    if N == p:
        print('yes')
    else:
        print('no')