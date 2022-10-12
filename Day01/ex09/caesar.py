import sys

def ceaser(string, n):
    try:
        string.encode('ascii')
    except UnicodeEncodeError:
        raise Exception("Error. Don't support language")

    low = list('abcdefghijklmnopqrstuvwxyz')
    upp = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ret = ''
    for i in string:
        if i in low:
            ret += low[(low.index(i) + n)%len(low)]
        elif i in upp:
            ret += upp[(upp.index(i) + n)%len(upp)]
        else:
            ret += i
    return ret

if __name__ == '__main__':
    if len(sys.argv) == 4:
        if (sys.argv[1] == 'encode'):
            print(ceaser(sys.argv[2], int(sys.argv[3])))
        elif (sys.argv[1] == 'decode'):
            print(ceaser(sys.argv[2], -int(sys.argv[3])))
        else:
            raise Exception("Error.Don't find parameter encode or decode")
    else:
        raise Exception("Error. Wrong number arguments")
