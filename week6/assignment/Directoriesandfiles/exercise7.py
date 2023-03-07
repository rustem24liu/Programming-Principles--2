with open('Hagrid.txt', 'r') as to_read:
    with open('B.txt', 'w') as write:
        for x in to_read.read():
            write.write(x)