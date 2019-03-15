import sys

if __name__ == '__main__':
    if len(sys.argv) ==1:
        print('Es necesario un argumento')
    else:
        if sys.argv[1] == 'help':
            print('Contactame...')
