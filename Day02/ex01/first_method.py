class Research:
    def file_reader():
        with open("data.csv", 'r') as data:
            return data.read()

if __name__ == '__main__':
    a = Research
    print(a.file_reader(), end='')
