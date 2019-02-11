def create_file(name, size):
    from random import randint
    f = open(name, 'w')

    for i in range(size):
        f.write(str(randint(-10 ** 5, 10 ** 5)) + '\n')
        #f.write('a\n')

    f.close()


create_file('unsorted', 100)
