import sys

def letter_starter(name):
    email = f'Dear {name}, welcome to our team. ' + \
           'We are sure that it will be a pleasure to work with you. ' + \
           'That’s a precondition for the professionals that our company hires.'
    return email


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open('employees.tsv') as input_file:
            flag = True
            for line in input_file.readlines():
                split_line = line.split()
                if split_line[2] == sys.argv[1]:
                    name = split_line[0]
                    flag = False
                    print(letter_starter(name))
                    break
            if (flag):
                print(f"Don't find e-mail {sys.argv[1]} in table")
