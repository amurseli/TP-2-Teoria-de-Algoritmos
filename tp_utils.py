def read_input(file):
    file = open(file, 'r')
    line = file.readline() # header

    line = file.readline()
    coins = []
    while line :
        line_numbers = line.strip().split(';')
        coins.extend([int(num) for num in line_numbers])
        line = file.readline()
    
    file.close()
    return coins