#!/bin/python3

import timeit

def loop():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    ret = []
    for email in emails:
        if email.endswith('@gmail.com'):
            ret.append(email)
    return ret

def list_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return [email for email in emails if email.endswith('@gmail.com')]

def main():
    loop_time = timeit.timeit('loop()',
            setup='from __main__ import loop',
            number = 90_000_0)
  
    comprehension_time = timeit.timeit('list_comprehension()',
            setup='from __main__ import list_comprehension',
            number = 90_000_0)

    if (loop_time < comprehension_time):
        print('it is better to use a loop')
        print(str(loop_time) + ' vs ' + str(comprehension_time))
    else:
        print('it is better to use a list comprehension')
        print(str(comprehension_time) + ' vs ' + str(loop_time))

if __name__ == '__main__':
    main()
