class   Must_read:
    with open("data.csv", 'r')  as data:
        print(data.read(), end='')

if __name__ == '__main__':
    Must_read()
